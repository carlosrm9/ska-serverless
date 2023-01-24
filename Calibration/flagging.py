import casatasks as ct
import casaplotms as cplot

ct.flagdata(vis='ngc5921.demo.ms',autocorr=True)

# cplot.plotms(vis='/data/ngc5921.demo.ms',showgui=False,overwrite=True,plotfile='/data/flagging.jpg',coloraxis='field')
