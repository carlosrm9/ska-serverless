import casatasks as ct

ct.gaincal(vis='ngc5921.demo.ms', caltable='ngc5921.demo.gcal', gaintable=['ngc5921.demo.bcal'], interp=['nearest'], fi>        spw='0:6~56', gaintype='G', solint='inf', calmode='ap', refant='15')
