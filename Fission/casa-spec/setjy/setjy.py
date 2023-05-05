from flask import request
import requests
import os
import json
import casatasks as ct
import subprocess

def main():
    param = request.get_json()
    input = param["Input-MS"]
    del param["Input-MS"]
    inpath = '/app/data/'+ input
    ct.setjy(vis = inpath, **param)
    return 'Done!\n'
