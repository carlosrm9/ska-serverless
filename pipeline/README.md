# Instructions

## Building the images

In order to build the images, one should have Docker installed on your machine. To build the image, run:
```
docker build -t <container_name> .
```
This command has to be run in the directory where your Dockerfile and .py are.

## Running the containers

To run the containers, run:
```
docker run -it -v local/path/to/data:/data/ <container_name> "$(cat parameters.json)"
```
This will run the desired containerized function with the parameters included in `parameters.json` file and give the output in `local/path/to/data/`.

## Warning

Calibration and cleaning Casa 6.5.0 parameters.json are particularized to a file named ngc5921.demo.ms. Name of input and output files, and other parameters can be modified or included as needed.
