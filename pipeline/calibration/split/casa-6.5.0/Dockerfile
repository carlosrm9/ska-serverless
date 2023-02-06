FROM centos:8

RUN sed -i -e "s|mirrorlist=|#mirrorlist=|g" /etc/yum.repos.d/CentOS-*
RUN sed -i -e "s|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g" /etc/yum.repos.d/CentOS-*
RUN dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y
RUN yum -y update && yum -y upgrade

RUN yum -y install ImageMagick ImageMagick-devel ImageMagick-perl
RUN yum -y  install xorg-x11-server-Xvfb 
RUN	yum -y install compat-libgfortran-48 
RUN	yum -y install libnsl 
RUN	yum -y install libcanberra-gtk2
RUN	yum -y install python36-devel
RUN	yum -y install openmpi-devel
RUN	yum -y install mpich-devel 
RUN dnf -y install python3
RUN	yum -y install git wget

RUN mkdir /casa/
WORKDIR /casa/
RUN wget https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/rhel/casa-6.5.0-15-py3.8.tar.xz 
RUN tar -xf casa-6.5.0-15-py3.8.tar.xz
RUN mkdir /script/
COPY split.py /script/
RUN mkdir /data/
WORKDIR /data/
ENV PATH="/casa/casa-6.5.0-15-py3.8/bin/:$PATH"
ENTRYPOINT ["python3","/script/split.py"] 

 
