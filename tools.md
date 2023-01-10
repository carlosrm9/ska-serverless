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
I have searched through the documentation of this package and the only thing that I have found that may be useful in our field is astropy.convolution.convolve. 
#### astropy.convolution.convolve
Description/Objectives: I convolves an array (image) with a kernel (I am not sure about the meaning of kernel in this context).

Parameterization (and complexity). The parameters are:
+ boundary (It determines how to handle boundaries, i.e, fill to a fixed value (fill_value) , periodic, etc.)
+ fill_value 
+ normalize_kernel (Whether normalized or not the kernel)
+ nan_treatment (How to treat corrupted data from the image: interpolation, fill_value,etc.)
+ preserve_nan (Preserve or not corrupted pixels after convolution)
+ mask (A mask array)

Parallelizable.I have not found anything on this matter.

Supports file splits.I have not found anything on this matter.

How is the data entry and types of data entry. Data entry is an array, that can be an image.fits that previosly is opened with astropy.io.open, and a kernel, that may be one of the existing in the package, or a custom creation (with another function of the package, customkernel).

Available versions (for GPU, special for architectures, etc.) The lastest version of the Astropy package are 5.2.1, 5.2, 5.1.2, and 5.1. I have not found anything about different versions for GPU or special architectures.

Example of usage.

https://docs.astropy.org/en/stable/convolution/index.html contains multiples examples of usage





