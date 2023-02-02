import casatasks as ct

with open("parameters_split.txt", "r") as file:
    parameters_split = file.read()

params_split = eval(parameters_split)

with open("parameters_sub.txt", "r") as file:
    parameters_sub = file.read()

params_sub = eval(parameters_sub)

ct.split(**params_split)

ct.uvcontsub(**params_sub)
