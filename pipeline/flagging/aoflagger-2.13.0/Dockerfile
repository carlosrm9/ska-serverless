FROM stimela/aoflagger:1.2.4

RUN mkdir /script/
RUN mkdir /data/
COPY script.py /script

WORKDIR /data/

ENTRYPOINT ["python3","/script/script.py"]
