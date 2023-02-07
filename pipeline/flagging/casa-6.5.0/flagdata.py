import sys
import json
import casatasks as ct
import casaplotms as cplot

param_json=sys.argv[1]

params = json.loads(param_json)

ct.flagdata(**params)

# cplot.plotms(vis='/data/ngc5921.demo.ms',showgui=False,overwrite=True,plotfile='/data/flagging.jpg',coloraxis='field')
