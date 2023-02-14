FROM amigahub/killms:v1

RUN mkdir /script
COPY script.py /script/

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["python3","/script/script.py"]