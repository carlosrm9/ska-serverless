import casatasks as ct
import os

with open("parameters.txt", "r") as file:
    parameters = file.read()

params = eval(parameters)
ct.tclean(**params)

path = '.'
cleans = [clean for clean in os.listdir(path) if clean.startswith('ngc5921.demo.tclean') ]

for clean in cleans:
        ct.exportfits(imagename=clean,fitsimage=clean+'.fits',overwrite=True)
