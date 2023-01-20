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
##### WSCLEAN Docker Container:

 To install the image:
 ```
 docker pull stimela/wsclean:1.6.3
 ```
This will install a Docker container with wsclean version 2.9.0

Here we have an example of how to run this container to clean an already calibrated measurement (obs.calib.ms).
```
docker run -it -v path/to/obs.calib.ms:/data/ stimela/wsclean:1.6.3 wsclean -auto-threshold 3 \
-size 1280 1280 -scale 8asec -mgain 0.8 -niter 1000 /data/obs.ms
```
This will perform a simple cleaning to a 3 sigma noise level with 1000 iterations. 


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

#### setjy 

Description/Objectives. Fills the model column with the visibilities of a calibrator

Parameterization (and complexity). 
+ vis (Name of input visibility file)
+ field (Field name)
+ model (File location for field model)
There are others parameters.

Parallelizable.-

Supports file splits.-

How is the data entry and types of data entry. Data entry is visibility (and field of calibration source)

Available versions (for GPU, special for architectures, etc.)-


Example of usage.

```
# 1331+305 = 3C286 is our primary calibrator.
setjy(vis='ngc5921.demo.ms', field='1331+305*', model='3C286_L.im')
```

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

#### gaincal

Description/Objectives. Determine temporal gains from calibrator observations

Parameterization (and complexity). 
+ vis (Name of input visibility file)
+ caltable (Name of output gain calibration table)
+ gaintable (Gain calibration table(s) to apply on the fly)
+ interp (Temporal interpolation for each gaintable)
+ field (Select field using field id(s) or field name(s), this field contains the data of the strong source)
+ spw (Select spectral window/channels)
+ gaintype (Type of gain solution: G,T,GSPLINE,K,KCROSS)
+ solint (Solution interval in time)
+ calmode (Type of solution: ’ap’, ’p’, ’a’)
+ refant (Reference antenna name(s))

Parallelizable.-

Supports file splits.-

How is the data entry and types of data entry. Data entry is visibility.

Available versions (for GPU, special for architectures, etc.)-


Example of usage.
```
gaincal(vis='ngc5921.demo.ms', caltable='ngc5921.demo.gcal', gaintable=['ngc5921.demo.bcal'], interp=['nearest'], field='0,1', 
        spw='0:6~56', gaintype='G', solint='inf', calmode='ap', refant='15')
```

#### fluxscale

Description/Objectives. Bootstrap the flux density scale from standard calibrators

Parameterization (and complexity).
+ vis (Name of input visibility file)
+ fluxtable (Name of output, flux-scaled calibration table)
+ caltable (Name of input calibration table)
+ reference (Reference field name)
+ transfer (Transfer field name)

Parallelizable.-

Supports file splits.-

How is the data entry and types of data entry. Data entries are visibilities and calibration table.

Available versions (for GPU, special for architectures, etc.)-


Example of usage.

```
fluxscale(vis='ngc5921.demo.ms', fluxtable='ngc5921.demo.fluxscale', caltable='ngc5921.demo.gcal', reference='1331*', transfer='1445*')
```

#### applycal

Description/Objectives. Apply calibrations solutions(s) to data

Parameterization (and complexity).
+ vis (Name of input visibility file)
+ field (Select field using field id(s) or field name(s) for the calibration to be applied on)
+ gaintable (Gain calibration table(s) to apply on the fly)
+ gainfield (Select a subset of calibrators from gaintable)
+ interp (Interp type in time[freq], per gaintable)
+ spwmap (Spectral windows combinations to form for gaintables)
+ selectdata (Not really sure about this parameter)

Parallelizable.-

Supports file splits.-

How is the data entry and types of data entry. Visibilities and gaintable/gainfield.

Available versions (for GPU, special for architectures, etc.)-


Example of usage. 

```
applycal(vis='ngc5921.demo.ms', field='1,2', gaintable=['ngc5921.demo.fluxscale','ngc5921.demo.bcal'], 
         gainfield=['1','*'], interp=['linear','nearest'], spwmap=[], selectdata=False)
```

#### split 
Description/Objectives. Create a visibility subset from an existing visibility set

Parameterization (and complexity).
+ vis (Name of input Measurement set)
+ outputvis (Name of output Measurement set)
+ field (Select field using ID(s) or name(s))
+ spw (Select spectral window/channels)
+ datacolumn (Which data column(s) to process)

Parallelizable.-

Supports file splits.-

How is the data entry and types of data entry. Visibility

Available versions (for GPU, special for architectures, etc.)-


Example of usage.
```
split(vis='ngc5921.demo.ms', outputvis='ngc5921.demo.src.split.ms', field='N5921*', spw='', datacolumn='corrected')
```
#### uvcontsub

Description/Objectives. Continuum fitting and subtraction in the uv plane.

Parameterization (and complexity).
+ vis (Continuum fitting and subtraction in the uv plane)
+ field (Select field(s) using id(s) or name(s))
+ fitspw (Spectral window:channel selection for fitting the continuum)
+ spw (Spectral window selection for output)
+ solint (Continuum fit timescale)
+ fitorder (Polynomial order for the fits)
+ want_cont (Create vis + ”.cont” to hold the continuum estimate)

Parallelizable.-

Supports file splits.-

How is the data entry and types of data entry. Visibility

Available versions (for GPU, special for architectures, etc.)-


Example of usage. The output will be ngc5921.demo.ms.contsub for the continuum-subtracted spectral line data and ngc5921.demo.ms.cont for the average of the continuum
```
uvcontsub(vis='ngc5921.demo.src.split.ms', field='N5921*', fitspw='0:4~6;50~59', spw='0', solint=0.0, fitorder=0, 
        want_cont=True)
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
 
 ##### Casa Docker Container:

To install the image:
 ```
 docker pull amigahub/casa:6.X.X
 ```
 where 6.X.X is the desired version.

Here we have an example of how to run this container (Casa 6.5.0) to clean an already calibrated measurement (obs.calib.ms).

``` 
docker run -it -v host/path/to/files:/script amigahub/casa:6.5.0 /casa/casa-6.5.0.15-py3.6/bin/python3 /script/script.py
```

`host/path/to/files` must be the path to both `obs.calib.ms` and `script.py`. script.py must contain the python script wanted to be run. In this case, we will generate two images, the one before cleaning (obs.dirty.image) and the one after doing 1000 iterations of tclean (obs.Reg.Clean.niter1k.image) along the rest of output data that tclean gives us after running. script.py should be 


```
import casatasks as ct

ct.rmtables('<imagename>.*')

tclean(vis='/script/obs.calib.ms', imagename='/script/obs.dirty', 
      imsize=1280, cell='8arcsec', pblimit=-0.01, niter=0,  
      stokes='I', savemodel='modelcolumn')

tclean(vis='/script/obs.calib.ms', imagename='obs.Reg.Clean.niter1K', 
      imsize=1280, cell='8arcsec', pblimit=-0.01, niter=1000, savemodel='modelcolumn')
```

For Casa 6.4.4, use:

``` 
docker run -it -v host/path/to/files:/script amigahub/casa:6.4.4 /casa/casa-6.4.4.31-py3.6/bin/python3 /script/script.py
```

For Casa 6.4.0, use:

``` 
docker run -it -v host/path/to/files:/script amigahub/casa:6.4.4 /casa/casa-6.4.0-16/bin/python3 /script/script.py
```

For Casa 6.5.2, use:

``` 
docker run -it -v host/path/to/files:/script amigahub/casa:6.4.4 /casa/casa-6.5.2-26-py3.6/bin/python3 /script/script.py
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





