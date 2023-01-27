import casatasks as ct

ct.split(vis='/data/ngc5921.demo.ms', outputvis='/data/ngc5921.demo.src.split.ms', field='N5921*', spw='', datacolumn='corrected')

ct.uvcontsub(vis='/data/ngc5921.demo.src.split.ms', field='N5921*', fitspw='0:4~6;50~59', spw='0', solint=0.0, fitorder=0, 
        want_cont=True)