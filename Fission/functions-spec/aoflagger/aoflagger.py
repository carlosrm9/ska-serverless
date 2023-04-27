from flask import request
import requests
import os
import json
import subprocess

def main():
    # Get tclean parameters as the json body of a POST request:
    param = request.get_json()
    # Define input file and outfile names:
    input = param["Input-MS"]
    del param["Input-MS"]
    # Download the input file to the cluster where Fission is running:
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
    subprocess.run(["aoflagger"] + parameters_str.split() + [inpath])
    # Retrieve the result of wsclean out of the cluster
    return 'Done!\n'
