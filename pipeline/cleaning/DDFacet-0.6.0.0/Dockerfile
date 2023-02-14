FROM stimela/ddfacet:1.7.0

RUN mkdir /script
COPY script.py /script/

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["python3","/script/script.py"]
