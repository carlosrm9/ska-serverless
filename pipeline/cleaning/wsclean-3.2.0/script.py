import sys
import json
import subprocess

parameters = sys.argv[1]

params = json.loads(parameters)

result = []
for key, value in params.items():
    if key == "ms":
        continue
    if type(value) == list:
        result.append(f"-{key}")
        for item in value:
            result.append(str(item))
    else:
        result.append(f"-{key} {value}")
parameters_str=" ".join(result)
subprocess.run(["wsclean"] + parameters_str.split() + [params["ms"]])
