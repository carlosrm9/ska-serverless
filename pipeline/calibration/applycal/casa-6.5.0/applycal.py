import casatasks as ct

with open("parameters.txt", "r") as file:
    parameters = file.read()

params = eval(parameters)

ct.applycal(**params)
