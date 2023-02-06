import sys
import json
import casatasks as ct
import casaplotms as csplot

parameters=sys.argv[1]

with open(parameters, "r") as file:
    param_json = file.read()

params = json.loads(param_json)

ct.bandpass(**params)

# csplot.plotms(vis='ngc5921.demo.bcal', field='0', gridrows=2, gridcols=1, plotindex=0, rowindex=0, 
#       xaxis='channel', yaxis='amp', showgui=False, clearplots=False, coloraxis='antenna1',
#       overwrite=True,plotfile='amp_ch.jpg')
# csplot.plotms(vis='ngc5921.demo.bcal', field='0', gridrows=2, gridcols=1, plotindex=1, rowindex=1, 
#       xaxis='channel', yaxis='phase', showgui=False, clearplots=False, coloraxis='antenna1',
#       overwrite=True,plotfile='phase_ch.jpg')
