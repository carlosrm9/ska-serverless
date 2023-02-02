import stimela
import os

INPUT = 'input/' # Input directory  (It must exit)
OUTPUT = 'output/' # Output directory
MSDIR = 'msdir/' # Measurement Set directory
PREFIX = 'Obs' # Prefix for output images

MSNAME = 'Obs.ms' # Measurent Set Name

pipeline = stimela.Recipe('Flagging with Aoflagger',
			  ms_dir=MSDIR,
			  indir=INPUT,
			  outdir=OUTPUT,
			  log_dir=os.path.join(OUTPUT,'logs'),
			  )
with open("parameters.txt", "r") as f:
    parameters = f.read()

params = eval(parameters)

pipeline.add("cab/autoflagger",	# this is the full name of the executor image
    "flagging_aoflagger",		# container label
    params, 	# These are the options set above
    label="Flag data")	# Task label. For logging purposes

 
pipeline.run()
