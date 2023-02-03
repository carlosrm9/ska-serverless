## Installation instructions
To install this container, clone `https://gitlab.com/aroffringa/wsclean` using

```
git clone https://gitlab.com/aroffringa/wsclean
```

Then, copy `Dockerfile` and `installation.sh` to `/path/to/repository/scripts/docker`. Then run 

```
. installation.sh
```

This will create a Docker container with wsclean v3.2.0. Before using it, one must tag it using its ID (to check the container ID use `docker images`):

``` 
docker tag Cont_ID wsclean:v3.2.0
```

Finally, to run the container, use

```
docker run -it -v /path/to/obs.ms:/data/ wsclean:v3.2.0 wsclean [-options] /data/obs.ms
```
Alternatively, you can run wsclean parameters from a parameters.txt with 

```
docker run -it -v /path/to/obs.ms:/data/ wsclean:v3.2.0 wsclean $(cat parameters.txt)
```
