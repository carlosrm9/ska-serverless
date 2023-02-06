import json
import casatasks as ct
import casaplotms as cplot

with open("parameters.json", "r") as file:
    param_json = file.read()

params = json.loads(param_json)

ct.flagdata(**params)

# cplot.plotms(vis='/data/ngc5921.demo.ms',showgui=False,overwrite=True,plotfile='/data/flagging.jpg',coloraxis='field')
