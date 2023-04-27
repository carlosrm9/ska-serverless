import os
import requests
import json

url = os.environ['FISSION_URL']

def fits2ms(input_name, output_name, antscheme = 'old'):
    parameters = {'Input-MS': input_name, 'Output-MS': output_name, 'antnamescheme' : antscheme}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/fits2ms', headers = {'Content-Type': 'application/json'}, data=json_data)
    return print('fits2ms done!')

def listobs(input_name, output_name, verbose = False, overwrite = True):
    parameters = {"Input-MS" : "ngc5921.demo.ms",
                  "Output-MS" :"listobs.txt",
                  "verbose" : verbose,
     		  "overwrite": overwrite}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/listobs', headers = {'Content-Type': 'application/json'},
                             data=json_data)
    return print('listobs done!')

def flagdata(input_name, autocorr):
    parameters = {"Input-MS": input_name, "autocorr": autocorr}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/flagdata', headers = {'Content-Type': 'application/json'},
                         data=json_data)
    return print('flagdata done!')

def setjy(input_name, field, model):
    parameters = {"Input-MS" : input_name, "field" : field, "model" : model}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/setjy', headers = {'Content-Type': 'application/json'},
                         data=json_data)
    return print('setjy done!')

def bandpasscal(input_name, output_cal, field, selectdata, bandtype, solint, combine, refant):
    parameters = {"Input-MS" : input_name, "Output-Cal" : output_cal, "field" : field, "selectdata" : selectdata,
                  "bandtype" : bandtype, "solint" : solint, "combine" : combine, "refant" : refant}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/bandpasscal', headers = {'Content-Type': 'application/json'},
                         data=json_data)
    return print('bandpasscal done!')

def gaincal(input_name, output_cal, gaintable, interp, field, spw, gaintype, solint, calmode, refant):
    parameters = {"Input-MS" : input_name, "Output-Cal" : output_cal, "gaintable" : gaintable, "interp" : interp,
                  "field" : field, "spw" : spw, "gaintype" : gaintype, "solint" : solint, "calmode" : calmode,
                  "refant" : refant}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/gaincal', headers = {'Content-Type': 'application/json'},
                         data=json_data)
    return print('gaincal done!')

def fluxscale(input_name, outflux_name, caltable, reference, transfer):
    parameters = {"Input-MS" : input_name, "Output-Fluxscale" : outflux_name, "caltable" : caltable,
                  "reference" : reference, "transfer" : transfer}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/fluxscale', headers = {'Content-Type': 'application/json'},
                         data=json_data)
    return print('fluxscale done!')

def applycal(input_name, field, gaintable, gainfield, interp, spwmap, selectdata):
    parameters = {"Input-MS" : input_name, "field" : field, "gaintable" : gaintable, "gainfield" : gainfield,
    "interp" : interp, "spwmap" : spwmap, "selectdata" : selectdata}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/applycal', headers = {'Content-Type': 'application/json'},
                         data=json_data)
    return print('applycal done!')

def split(input_name, output_name, field, spw, datacolumn):
    parameters = {"Input-MS" : input_name, "Output-MS" : output_name, "field" : field, "spw" : spw,
                  "datacolumn" : "corrected"}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/split', headers = {'Content-Type': 'application/json'},
                         data=json_data)
    return print('split done!')

def uvcontsub(input_name, field, fitspw, spw, solint, fitorder, want_cont):
    parameters = {"Input-MS" : input_name, "field" : field, "fitspw" : fitspw, "spw" : spw,
                  "solint" : solint, "fitorder" : fitorder, "want_cont" : want_cont}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/uvcontsub', headers = {'Content-Type': 'application/json'},
                         data=json_data)
    return print('uvsubcont done!')

def tclean(input_name, output_name, field, datacolumn, specmode, nchan, start, width, spw, deconvolver, gridder, niter,
           gain, threshold, imsize, cell, weighting, robust, mask, interactive, pblimit):
    parameters = {"Input-MS" : input_name, "Output-MS" : output_name, "field" : field, "datacolumn" : datacolumn,
                  "specmode" : specmode, "nchan" : nchan, "start" : start, "width" : width, "spw" : spw,
                  "deconvolver" : deconvolver, "gridder" : gridder, "niter" : niter, "gain" : gain,
                  "threshold" : threshold, "imsize" : imsize, "cell" : cell, "weighting" : weighting,
                  "robust" : robust, "mask" : mask, "interactive" : interactive, "pblimit" : pblimit}
    json_data = json.dumps(parameters)
    response = requests.post(url + '/tclean', headers = {'Content-Type': 'application/json'},
                         data=json_data)
    return print('tclean done!')
