from flask import request
import requests
import os
import json
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
    del param["Input-MS"]
    # Download the input file to the cluster where Fission is running:
    inpath = '/tmp/' + input
    result = []
    for key, value in param.items():
        if key == "update-model":
            if value:
                result.append(f"-{key}"+"-required")
            else:
                result.append("-no"+f"-{key}"+"-required")
        elif key == "reorder":
            if value:
                result.append(f"-{key}")
            else:
                result.append("-no"+f"-{key}")

        elif type(value) == list:
            result.append(f"-{key}")
            for item in value:
                result.append(str(item))
        else:
            result.append(f"-{key} {value}")
    parameters_str=" ".join(result)
    subprocess.run(["wsclean"] + parameters_str.split() + [inpath])
    # Retrieve the result of wsclean out of the cluster
    for file in os.listdir('/app/'):
        if file.startswith("wsclean"):
                upload_file('/app/' + file)
    return 'Done!\n'
