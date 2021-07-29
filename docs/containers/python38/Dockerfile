FROM ubuntu:20.04
MAINTAINER xx-zhang <actanble@gmail.com>

ENV LANG en_US.UTF-8
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD ./sources.list /etc/apt/sources.list
RUN apt-get -yqq update
RUN apt-get -y install python3 python3-dev python3-pip
# TODO 安装辅助工具
RUN apt-get -y install nmap masscan tcpreplay tcpdump lftp

# Install Mysql Client
WORKDIR /usr/src/app
VOLUME /usr/src/app

ADD requirements.base.txt /requirements.txt

RUN pip3 install --upgrade pip \
    --trusted-host mirrors.aliyun.com \
    --index-url http://mirrors.aliyun.com/pypi/simple/
RUN pip3 install -r /requirements.txt

USER root