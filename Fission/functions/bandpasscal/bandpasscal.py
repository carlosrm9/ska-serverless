from flask import request
import requests
import os
import json
import casatasks as ct
import subprocess

def main():
    param = request.get_json()
    input = param["Input-MS"]
    output = param["Output-Cal"]
    del param["Input-MS"]
    del param["Output-Cal"]
    inpath = '/app/data/'+ input
    outpath = '/app/data/' + output
    ct.bandpass(vis = inpath, caltable = outpath,**param)
    return 'Done!\n'
