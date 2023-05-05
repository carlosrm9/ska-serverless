from flask import request
import requests
import os
import json
import casatasks as ct
import subprocess

def main():
    param = request.get_json()
    input = param["Input-MS"]
    gaintab = param["gaintable"]
    del param["Input-MS"]
    del param["gaintable"]
    for i in range(len(gaintab)):
        gaintab[i] = '/app/data/' + gaintab[i]
    inpath = '/app/data/'+ input
    ct.applycal(vis = inpath, gaintable = gaintab, **param)
    return 'Done!\n'
