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
    param = request.get_json()
    input = param["Input-MS"]
    output = param["Output-MS"]
    response = download_file('NGC5921.fits', '/tmp/')
    inpath = '/tmp/' + input
    outpath = '/tmp/' + output
    fitsdata='/tmp/NGC5921.fits'
    ct.importuvfits(fitsfile = inpath, vis = outpath)
    subprocess.run(["tar", "-czf", outpath + ".tar.gz", outpath])
    response2 = upload_file(outpath + ".tar.gz")
    return 'Done'
