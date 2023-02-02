import casatasks as ct
import casaplotms as cplot

with open("parameters.txt", "r") as file:
    parameters = file.read()

params = eval(parameters)

ct.flagdata(**params)

# cplot.plotms(vis='/data/ngc5921.demo.ms',showgui=False,overwrite=True,plotfile='/data/flagging.jpg',coloraxis='field')
