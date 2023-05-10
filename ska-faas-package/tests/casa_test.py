import timeit
import subprocess
import os

def main():
    import casatasks as ct
    ct.importuvfits(fitsfile = "data/NGC5921.fits", vis = "data/ngc5921.demo.ms")
    ct.listobs(vis = "data/ngc5921.demo.ms", listfile = "data/listobs.txt", verbose = False, overwrite = True)
    ct.flagdata(vis='data/ngc5921.demo.ms',autocorr=True)
    ct.setjy(vis='data/ngc5921.demo.ms',field='1331+305*', model='3C286_L.im')
    ct.bandpass(vis='data/ngc5921.demo.ms', caltable='data/ngc5921.demo.bcal', field='0', selectdata=False,bandtype='B', solint='inf', combine='scan', refant='15')
    ct.gaincal(vis='data/ngc5921.demo.ms', caltable='data/ngc5921.demo.gcal', gaintable=['data/ngc5921.demo.bcal'], interp=['nearest'], field='0,1',
        spw='0:6~56', gaintype='G', solint='inf', calmode='ap', refant='15')
    ct.fluxscale(vis='data/ngc5921.demo.ms', fluxtable='data/ngc5921.demo.fluxscale', caltable='data/ngc5921.demo.gcal', reference='1331*', transfer='1445*')
    ct.applycal(vis='data/ngc5921.demo.ms', field='1,2', gaintable=['data/ngc5921.demo.fluxscale','data/ngc5921.demo.bcal'], 
         gainfield=['1','*'], interp=['linear','nearest'], spwmap=[], selectdata=False)
    ct.split(vis='data/ngc5921.demo.ms', outputvis='data/ngc5921.demo.src.split.ms', field='N5921*', spw='', datacolumn='corrected')
    ct.uvcontsub(vis='data/ngc5921.demo.src.split.ms', field='N5921*', fitspw='0:4~6;50~59', spw='0', solint=0.0, fitorder=0, 
        want_cont=True)
    ct.tclean(vis='data/ngc5921.demo.src.split.ms.contsub', imagename='data/ngc5921.demo.tclean', 
       field='0', datacolumn='data', specmode='cube', nchan=46, start=5, width=1, 
       spw='', deconvolver='hogbom', gridder='standard', niter=6000, gain=0.1, 
       threshold='8.0mJy', imsize=[256,256], cell=['15.0arcsec','15.0arcsec'], 
       weighting='briggs', robust=0.5,  mask = 'box[[108pix,108pix],[148pix,148pix]]', 
       interactive=False, pblimit=-0.2)
    directory = os.listdir('data/')
    print(directory)
    for filename in directory:
        if filename != 'NGC5921.fits':
            subprocess.run(['sudo','rm','-r','data/' + filename])


if __name__ == '__main__':
    print(timeit.timeit("main()", setup="from __main__ import main", number=10))
