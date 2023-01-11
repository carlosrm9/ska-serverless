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
#### casatasks.importuvfits

Description/Objectives: It imports the multisource UVFITS data to a CASA measurement set

Parameterization (and complexity):
+ fitsfile Name of input file
+ vis Name of output visibility file
+ async (True or False. If true run in the background, prompt is freed).

Parallelizable: -

Supports file splits: -

How is the data entry and types of data entry: Data entry image.fits

Available versions (for GPU, special for architectures, etc.): -

Example of usage.
```
importuvfits(fitsfile=’NGC5921.fits’,vis=’ngc5921.ms’)
```
#### flagdata
Description/Objectives. It flags the visibilities to reduce noise.

Parameterization (and complexity):
+ vis (Input visibilities to be flagged)
+ autocorr (True or False. If True flags only autocorrelations).
+ There are other parameters (74 in total). They can be found at https://casa.nrao.edu/docs/taskref/flagdata-task.html

Parallelizable: -

Supports file splits: -

How is the data entry and types of data entry: Data entry are visibilities, obtained from fits with the previous function. 

Available versions (for GPU, special for architectures, etc.): -


Example of usage. How to flag only the autocorrelations:
```
flagdata(vis="ngc5921.demo.ms", autocorr=True)
```
### In a usual workflow, there are other functions used between the previous ones and the next ones. I think they are not of interest because they only sets what I suppose are "small things", which can be performed locally. 

#### bandpass

Description/Objectives. Calculates a bandpass calibration solution. It needs observations of strong known sources.

Parameterization (and complexity):
+ vis (Name of input visibility file)
+ caltable (Name of output gain calibration table)
+ field (Select field using field id(s) or field name(s), this field contains the data of the strong source)
+ selectada (True or False. Other data selection parameters)
+ bandtype (Type of bandpass solution)
+ solint (Solution interval in time)
+ combine (Data axes which to combine for solve)
+ refant (Reference antenna name(s))
There are a lot of other parameters.
Parallelizable. -

Supports file splits. -

How is the data entry and types of data entry. Data entry is visibility

Available versions (for GPU, special for architectures, etc.) -


Example of usage.
```
bandpass(vis='ngc5921.demo.ms', caltable='ngc5921.demo.bcal', field='0', selectdata=False, 
         bandtype='B', solint='inf', combine='scan', refant='15')
```

#### tclean
Description/Objectives. Form images from visibilities and reconstruct a sky model.

Parameterization (and complexity). Great number or parameters. They are found at https://casa.nrao.edu/docs/taskref/tclean-task.html. Some of them are:
+ vis (Visibilities ready to be imaged)
+ imagename (name of the resulting image)
+ field (Select fields to image or mosaic)
+ datacolumn (Data column to image: data or corrected)
+ specmode (Spectral definition mode:mfs,cube,cubedata. More info about this at https://casa.nrao.edu/docs/taskref/tclean-task.html)
+ nchan (Number of channels in the output image)
+ start (First channel of output cube images specified by data channel number)
+ width (Channel width of output cube images specified by data channel number
+ spw (Select spectral window/channels)
+ deconvolver (Name of minor cycle algorithm: hogbom,clark,multiscale,mtmfs,mem,clarkstokes)
+ gridder (Gridding options: standard, wproject, widefield, mosaic, awproject)
+ niter (Maximum number of iterations)
+ gain (Fraction of the source flux to subtract out of the residual image for the CLEAN algorithm and its variants)
+ threshold (Stopping threshold (number in units of Jy, or string)
+ imsize (Number of pixels of the final image)
+ cell (Cell size of the final image)
+ weighting (Weighting scheme: natural,uniform,briggs,superuniform,radial)
+ robust (Robustness parameter for Briggs weighting)
+ mask (The name of a CASA image or region file or region string that specifies a 1/0 mask to be used for deconvolution)
+ interactive (Modify masks and parameters at runtime)
+ pblimit (PB gain level at which to cut off normalizations. I don't really get what is this)

Parallelizable.-

Supports file splits.-

How is the data entry and types of data entry. Visibilities calibrated and ready to be imaged.

Available versions (for GPU, special for architectures, etc.)-


Example of usage.

```
tclean(vis='ngc5921.demo.src.split.ms.contsub', imagename='ngc5921.demo.tclean', 
       field='2', datacolumn='data', specmode='cube', nchan=46, start=5, width=1, 
       spw='', deconvolver='hogbom', gridder='standard', niter=6000, gain=0.1, 
       threshold='8.0mJy', imsize=[256,256], cell=['15.0arcsec','15.0arcsec'], 
       weighting='briggs', robust=0.5,  mask = 'box[[108pix,108pix],[148pix,148pix]]', 
       interactive=False, pblimit=-0.2)
 ```



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





