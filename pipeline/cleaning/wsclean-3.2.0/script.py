import sys
import json
import subprocess

parameters=sys.argv[1]


params = json.loads(parameters)

args = ["wsclean"]
for k, v in params.items():
    args.append("-" + k)
    if v is not None:
        args.append(str(v))

subprocess.run(args)

