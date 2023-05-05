from flask import request
import requests
import os
import subprocess
import json

def main():
    param = request.get_json()
    input = param["Input-MS"]
    del param["Input-MS"]
    inpath = '/app/data/' + input
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
    fits_files = [f for f in os.listdir('/app') if f.endswith('.fits')]
    for fits_file in fits_files:
        subprocess.run(['mv', '/app/' + fits_file, '/app/data/'])
    return 'wsclean done\n!'
