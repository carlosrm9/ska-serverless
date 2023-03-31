from flask import request
import requests
import os
import json
import casatasks as ct
import subprocess

SERVER_URL = 'http://192.168.100.70:10000'
UPLOAD_ENDPOINT = '/upload'
DOWNLOAD_ENDPOINT = '/download'

def upload_file(filepath):
    url = SERVER_URL + UPLOAD_ENDPOINT
    with open(filepath, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
    return response.text

def download_file(filename, save_path):
    url = SERVER_URL + DOWNLOAD_ENDPOINT + '/' + filename
    response = requests.get(url)
    if response.status_code == 404:
        return 'File not found'
    else:
        with open(os.path.join(save_path, filename), 'wb') as f:
            f.write(response.content)
        return filename +' ' + 'downloaded!'

def main():
    # Get tclean parameters as the json body of a POST request:
    param = request.get_json()
    # Define input file and outfile names:
    input = param["Input-MS"]
    inputtar = param["Input-MS"] + ".tar.gz"
    response = download_file(inputtar, '/tmp/')
    subprocess.run(["tar", "xf", "/tmp/" + inputtar, "-C", "/tmp/"])
    input = input + ".ms" 
    output = param["Output-MS"]
    del param["Input-MS"] 
    del param["Output-MS"]
    # Download the input file to the cluster where Fission is running:
    inpath = '/tmp/' + input
    outpath = '/tmp/' + output
    ct.tclean(vis = inpath, imagename= outpath, **param)
    # Retrieve the result of tclean out of the cluster
    for file in os.listdir('/tmp/'):
        if file.startswith(output):
            if not os.path.isdir(file):
                upload_file('/tmp/' + file)
            else:
                subprocess.run(["tar","cf", "/tmp/"+ file + ".tar.gz", "/tmp/" + file])
                upload_file("/tmp/"+ file + ".tar.gz")
    return 'Done!\n'
