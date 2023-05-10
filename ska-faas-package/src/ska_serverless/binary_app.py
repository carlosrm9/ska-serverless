import os
import requests
import json

url = os.environ['FISSION_URL']

def aoflagger(input_name):
    parameters = {"Input-MS": input_name}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/aoflagger', headers = {'Content-Type': 'application/json'}, data=json_data)
    return print('aoflagger done!')

def wsclean(input_name, size, scale, mgain, niter, pbl, update_model):
    parameters = {
    "Input-MS" : input_name,"size" : size, "scale": scale,"mgain": mgain, "niter": niter,"primary-beam-limit" : pbl,
    "update-model" : update_model}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/wsclean', headers = {'Content-Type': 'application/json'}, data=json_data)
    return print('wsclean done!')
