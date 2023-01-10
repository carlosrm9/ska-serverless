# Radio Tools

## Pre-processing

### WSCLEAN

Description/Objectives: "w-stacking" cleaning algorithm. It deconvolutes the image to obtain the true flux density of the observed object.

Parameterization (and complexity): I have not found in the documentation a complete list of all the parameters of this funtion. Some of them are:
+ -size w h (width and heigth of image, they need to be even)
+ -scale a (angular size of a single pixel of the image)
+ -niter n (maximum number of minor iterations allowed to be used)
+ -(auto-)threshold s (It defines where to stop cleaning. When using auto-,    the criterium is that the cleaning will continue until the peak residaul flux is below s times the standard deviation of the noise of the image.)
+ -mgain m (It sets the major iteration gain, the factor by which the peak is reduced).

These are the "Basic Cleaning" parameters. There are a great number of them, so I think the complexity of implementing all of them is very high.


Parallelizable: Due to the nature of the "w-stacking" algorithm, I think that parallelization is not possible. However, I have not found anything in the documentation that says otherwise.

Supports file splits: I have not found anything about it in the documentation. I did however found a section called Multiple measurement sets, that allows you to clean the combined data from all measurement sets together. 

How is the data entry and types of data entry: I have not found the specific format of data entry. It names the input data obs.ms

Available versions (for GPU, special for architectures, etc.):
Stable versions: 3.0, 3.1 and 3.2. There are older stable versions, 2.0-2.10 and 1.0-1.12.

Example of usage: To clean an observation to a 3 sigma noise level,
```
wsclean -auto-threshold 3 -size 2048 2048 -scale 1amin \
  -mgain 0.8 -niter 50000 observation.ms
```

### TSCLEAN 

Description/Objectives. I have not found any function called TSClean related to Radioastronomy

Parameterization (and complexity).

Parallelizable.

Supports file splits.

How is the data entry and types of data entry.

Available versions (for GPU, special for architectures, etc.)


Example of usage.


### CASA

Description/Objectives.

Parameterization (and complexity).

Parallelizable.

Supports file splits.

How is the data entry and types of data entry.

Available versions (for GPU, special for architectures, etc.)

Example of usage.

### ASTROPY

Description/Objectives.

Parameterization (and complexity).

Parallelizable.

Supports file splits.

How is the data entry and types of data entry.

Available versions (for GPU, special for architectures, etc.)

Example of usage.



