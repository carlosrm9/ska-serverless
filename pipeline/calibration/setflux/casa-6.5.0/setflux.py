import sys
import json
import casatasks as ct

parameters=sys.argv[1]

with open(parameters, "r") as file:
    param_json = file.read()

params = json.loads(param_json)

ct.setjy(**params)

