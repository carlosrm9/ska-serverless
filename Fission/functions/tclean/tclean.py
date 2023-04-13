from flask import request
import requests
import os
import json
import casatasks as ct
import subprocess

def main():
    # Get tclean parameters as the json body of a POST request:
    param = request.get_json()
    input = param["Input-MS"]
    output = param["Output-MS"]
    del param["Input-MS"]
    del param["Output-MS"]
    inpath = '/app/data/' + input
    outpath = '/app/data/' + output
    ct.tclean(vis = inpath, imagename= outpath, **param)
    return 'Done! Check /mnt/data for Output\n'
