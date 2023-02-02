import casatasks as ct

with open("parameters.txt", "r") as file:
    parameters = file.read()

params = eval(parameters)

ct.setjy(vis='/data/ngc5921.demo.ms',field='1331+305*', model='3C286_L.im')

