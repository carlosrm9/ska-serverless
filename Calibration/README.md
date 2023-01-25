#### Calibration scripts
This folder contains the scripts needed to perform a basic calibration and cleaning of an observation using CASA. It is particularized to NGC5921.fits, but it can be changed.

To execute these scripts using Docker, use:

```
docker run -it -v host/path/to/files:/script amigahub/casa:6.5.0 /casa/casa-6.5.0.15-py3.6/bin/python3 /script/script.py
```

The order in which the different scripts must be run is:
+ importfits.py
+ listobs.py (This will generate a .txt with information about the observation and the calibrators)
+ flagging.py
+ setflux.py
+ bandpass_cal.py
+ gaincal.py
+ fluxscale.py
+ applycal.py
+ uvcontsub.py
+ tclean.py

Information about the functions used in these scripts can be found in tools.md. Parameters used in those functions can be altered depending of the particular needs of the observations.
