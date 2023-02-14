import sys
import json
import subprocess

parameters = sys.argv[1]

params = json.loads(parameters)

result = []
for key, value in params.items():
        result.append(f"--{key} {value}")
parameters_str=" ".join(result)

subprocess.run(["python3","/src/DDFacet/DDFacet/DDF.py"] + parameters_str.split())