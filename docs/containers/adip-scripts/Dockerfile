FROM ubuntu:20.04
MAINTAINER xx-zhang <actanble@gmail.com>

ENV LANG en_US.UTF-8
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD ./sources.list /etc/apt/sources.list
RUN apt-get -yqq update
RUN apt-get -y install python3 python3-dev python3-pip

# install some tools
RUN apt-get -y install lftp

# Install Mysql Client
WORKDIR /usr/src/app
VOLUME /usr/src/app

## ./local--bootstrap.sh

ADD ./local-bootstrap.sh /bootstrap.sh
RUN chmod +x /bootstrap.sh && /bootstrap.sh