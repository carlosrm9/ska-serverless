import casatasks as ct

ct.gaincal(vis='/data/ngc5921.demo.ms', caltable='/data/ngc5921.demo.gcal', gaintable=['/data/ngc5921.demo.bcal'], interp=['nearest'], field='0,1',
        spw='0:6~56', gaintype='G', solint='inf', calmode='ap', refant='15')
