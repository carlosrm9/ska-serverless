import sys
import json
import casatasks as ct
import os,sys

param_json=sys.argv[1]

params = json.loads(param_json)

ct.tclean(**params)

path = '.'
cleans = [clean for clean in os.listdir(path) if clean.startswith('ngc5921.demo.tclean') ]

for clean in cleans:
    ct.exportfits(imagename=clean,fitsimage=clean+'.fits',overwrite=True)
