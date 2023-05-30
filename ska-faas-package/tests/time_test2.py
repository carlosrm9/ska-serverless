import timeit
import subprocess
import os


def main():
    from ska_serverless.config import read_config

    read_config('config.ini')

    import ska_serverless.casafn as casa
    import ska_serverless.binary_app as ba
    casa.fits2ms('NGC5921.fits','ngc5921.demo.ms')
    casa.listobs('ngc5921.demo.ms', 'listobs.txt')
    casa.flagdata('ngc5921.demo.ms', True)
    casa.setjy('ngc5921.demo.ms',"1331+305*","3C286_L.im")
    casa.bandpasscal("ngc5921.demo.ms","ngc5921.demo.bcal", "0", False, "B", "inf", "scan", "15")
    casa.gaincal('ngc5921.demo.ms', 'ngc5921.demo.gcal', ['ngc5921.demo.bcal'], ['nearest'],
            '0,1', '0:6~56', 'G', 'inf', 'ap', '15')
    casa.fluxscale("ngc5921.demo.ms","ngc5921.demo.fluxscale","ngc5921.demo.gcal", "1331*", "1445*")
    casa.applycal('ngc5921.demo.ms', '1,2', ['ngc5921.demo.fluxscale','ngc5921.demo.bcal'],
                  ['1','*'], ['linear','nearest'], [], False)
    casa.split('ngc5921.demo.ms', 'ngc5921.demo.src.split.ms', 'N5921*', '',
               'corrected')
    casa.uvcontsub('ngc5921.demo.src.split.ms', 'N5921*', '0:4~6;50~59', '0',
                    0.0, 0, True)
    ba.wsclean('ngc5921.demo.src.split.ms.contsub',[1280, 1280], "8arcsec", 0.8, 6000, 0.01, True)
    directory = os.listdir('/mnt/data/')
    print(directory)
    for filename in directory:
        if filename != 'NGC5921.fits':
            subprocess.run(['sudo','rm','-r','/mnt/data/' + filename])


if __name__ == '__main__':
    print(timeit.timeit("main()", setup="from __main__ import main", number=10))