import sys
import json
import casatasks as ct
import os,sys

parameters = sys.argv[1]
translator = sys.argv[2]

params = json.loads(parameters)
trans = json.loads(translator)

trans_params = {}

trans_params = {}
for k, v in params.items():
    if v is not None:
        trans_k = trans.get(k, k)
        if trans_k is None:
            continue
        elif trans_k == "savemodel":
            if v:
                trans_params[trans_k] = "modelcolumn"
            else: 
                trans_params[trans_k] = "none"
        else:
            trans_params[trans_k] = v

ct.tclean(**trans_params)

path = '.'
cleans = [clean for clean in os.listdir(path) if clean.startswith('ngc5921.demo.tclean') ]

for clean in cleans:
    ct.exportfits(imagename=clean,fitsimage=clean+'.fits',overwrite=True)
