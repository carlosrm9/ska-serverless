from flask import request
import requests
import os
import json
import casatasks as ct
import subprocess

def main():
    param = request.get_json()
    input = param["Input-MS"]
    output = param["Output-Fluxscale"]
    caltab = param["caltable"]
    del param["Input-MS"]
    del param["Output-Fluxscale"]
    del param["caltable"]
    inpath = '/app/data/'+ input
    outpath = '/app/data/' + output
    calpath = '/app/data/' + caltab
    ct.fluxscale(vis = inpath, fluxtable = outpath, caltable = calpath, **param)
    return 'Done!\n'
