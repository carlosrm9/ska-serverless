import sys
import json
import subprocess

parameters = sys.argv[1]
translator = sys.argv[2]

params = json.loads(parameters)
trans = json.loads(translator)

trans_params = updated_dict = {trans.get(k, k): v for k, v in params.items()}

result = []
for key, value in trans_params.items():
    if key == "MS-Name":
        continue
    elif key == "update-model":
        if value:
            result.append(f"-{key}"+"-required")
        else:
            result.append("-no"+f"-{key}"+"-required")
    elif key == "reorder":
        if value:
            result.append(f"-{key}")
        else:
            result.append("-no"+f"-{key}")

    elif type(value) == list:
        result.append(f"-{key}")
        for item in value:
            result.append(str(item))
    else:
        result.append(f"-{key} {value}")
parameters_str=" ".join(result)
subprocess.run(["wsclean"] + parameters_str.split() + [trans_params["MS-Name"]])
