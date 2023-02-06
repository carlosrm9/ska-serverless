import sys
import casatasks as ct
import os,sys

parameters=sys.argv[1]

with open(parameters, "r") as file:
    param_json = file.read()

params = json.loads(param_json)

ct.tclean(**params)

path = '.'
cleans = [clean for clean in os.listdir(path) if clean.startswith('ngc5921.demo.tclean') ]

for clean in cleans:
    ct.exportfits(imagename=clean,fitsimage=clean+'.fits',overwrite=True)
