# Instructions

## Building the images

In order to build the images, one should have Docker installed on your machine. To build the image, run:
```
docker build -t nameofcontainer .
```
This command has to be run in the directory where your Dockerfile and .py are.

## Running the containers

To run the containers, run:
```
docker run -it -v local/path/to/data:/data/ nameofcontainer
```
This will run the desired containerized function and give the output in `local/path/to/data/`.

## Warning

Calibration and cleaning Casa 6.5.0 functions are particularized to a file named ngc5921.demo.ms. Name if input and output files can be modified as needed.