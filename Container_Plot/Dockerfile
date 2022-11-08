FROM ubuntu:22.04
RUN apt-get update 
RUN apt-get install python3 -y
RUN apt-get install pip -y
RUN python3 -m pip install -U matplotlib
RUN mkdir /home/app
COPY app/app.py /home/app
RUN mkdir /home/app/data
WORKDIR /home/app
CMD python3 app.py

