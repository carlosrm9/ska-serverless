from flask import request
import requests
import os
import json
import subprocess

def main():
    param = request.get_json()
    input = param["Input-MS"]
    inpath = '/app/data/' + input
    subprocess.run(["aoflagger"] + [inpath])
    return 'Done!\n'
