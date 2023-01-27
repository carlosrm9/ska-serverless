import casatasks as ct
import os

ct.tclean(vis='/data/ngc5921.demo.src.split.ms.contsub', imagename='/data/ngc5921.demo.tclean', 
       field='0', datacolumn='data', specmode='cube', nchan=46, start=5, width=1, 
       spw='', deconvolver='hogbom', gridder='standard', niter=6000, gain=0.1, 
       threshold='8.0mJy', imsize=[256,256], cell=['15.0arcsec','15.0arcsec'], 
       weighting='briggs', robust=0.5,  mask = 'box[[108pix,108pix],[148pix,148pix]]', 
       interactive=False, pblimit=-0.2)

path = '.'
cleans = [clean for clean in os.listdir(path) if clean.startswith('ngc5921.demo.tclean') ]

for clean in cleans:
        ct.exportfits(imagename=clean,fitsimage=clean+'.fits',overwrite=True)