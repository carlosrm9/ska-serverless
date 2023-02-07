import sys
import json
import casatasks as ct

param_json=sys.argv[1]

params = json.loads(param_json)

ct.setjy(**params)

