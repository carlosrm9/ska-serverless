## Installation instructions

To run the container, use
```
docker run -it -v /path/to/obs.ms:/data/ wsclean:v3.2.0 wsclean [-options] /data/obs.ms
```
Alternatively, you can run wsclean parameters from a parameters.txt with 

```
docker run -it -v /path/to/obs.ms:/data/ wsclean:v3.2.0 wsclean $(cat parameters.txt)
```
