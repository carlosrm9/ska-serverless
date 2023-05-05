from flask import request
import requests
import os
import json
import casatasks as ct
import subprocess

def main():
    param = request.get_json()
    input = param["Input-MS"]
    output = param["Output-MS"]
    del param["Input-MS"]
    del param["Output-MS"]    
    inpath = '/app/data/' + input
    outpath = '/app/data/' + output
    ct.listobs(vis = inpath, listfile = outpath , **param) 
    return 'Done!\n'
