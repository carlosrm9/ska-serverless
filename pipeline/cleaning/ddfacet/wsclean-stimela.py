import stimela
import os

INPUT = 'input/' # Input directory  (It must exit)
OUTPUT = 'output/' # Output directory
MSDIR = 'msdir/' # Measurement Set directory
PREFIX = 'Obs' # Prefix for output images

MSNAME = 'Obs.ms' # Measurent Set Name

pipeline = stimela.Recipe('Cleaning with ddfacet',
			  ms_dir=MSDIR,
			  indir=INPUT,
			  outdir=OUTPUT,
			  log_dir=os.path.join(OUTPUT,'logs'),
			  )
with open("parameters.txt", "r") as f:
    parameters = f.read()

params = eval(parameters)

pipeline.add("cab/ddfacet",	# this is the full name of the executor image
    "cleaning_ddfacet",		# container label
    params, 	# These are the options set above
    label="Cleaning")	# Task label. For logging purposes

 
pipeline.run()
