import casatasks as ct
import casaplotms as csplot

ct.bandpass(vis='/data/ngc5921.demo.ms', caltable='/data/ngc5921.demo.bcal', field='0', selectdata=False,bandtype='B', solint='inf', combine='scan', refant='15')

# csplot.plotms(vis='ngc5921.demo.bcal', field='0', gridrows=2, gridcols=1, plotindex=0, rowindex=0, 
#       xaxis='channel', yaxis='amp', showgui=False, clearplots=False, coloraxis='antenna1',
#       overwrite=True,plotfile='amp_ch.jpg')
# csplot.plotms(vis='ngc5921.demo.bcal', field='0', gridrows=2, gridcols=1, plotindex=1, rowindex=1, 
#       xaxis='channel', yaxis='phase', showgui=False, clearplots=False, coloraxis='antenna1',
#       overwrite=True,plotfile='phase_ch.jpg')
