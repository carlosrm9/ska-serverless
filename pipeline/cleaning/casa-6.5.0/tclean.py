import casatasks as ct
import os,sys



if __main__():      
    #PARAMS = sys.argv[1] PARAMS

    #with open("parameters.txt", "r") as file:
    #    parameters = file.read()

    params = eval(PARAMS)
    ct.tclean(**params)

    path = '.'
    cleans = [clean for clean in os.listdir(path) if clean.startswith('ngc5921.demo.tclean') ]

    for clean in cleans:
            ct.exportfits(imagename=clean,fitsimage=clean+'.fits',overwrite=True)
