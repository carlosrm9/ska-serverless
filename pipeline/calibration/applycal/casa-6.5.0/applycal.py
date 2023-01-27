import casatasks as ct

ct.applycal(vis='/data/ngc5921.demo.ms', field='1,2', gaintable=['/data/ngc5921.demo.fluxscale','/data/ngc5921.demo.bcal'], 
         gainfield=['1','*'], interp=['linear','nearest'], spwmap=[], selectdata=False)
ct.applycal(vis='/data/ngc5921.demo.ms', field='0', gaintable=['/data/ngc5921.demo.fluxscale','/data/ngc5921.demo.bcal'], gainfield=['0','*'], 
         interp=['linear','nearest'], spwmap=[], selectdata=False)

