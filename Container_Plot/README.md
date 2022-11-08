# Python3 Plotter
This is a Docker container used to plot a graph from a data.txt using Python3. 
To run this container, first build the image using 
docker build -t pyplotter
Then use docker run -v path/to/dir:/home/app/data --rm name to run the container. 
This will generate png with the desired graph in your data.txt directory.
