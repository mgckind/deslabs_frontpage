# Matias Carrasco Kind
#
# Flask and nginx
#

FROM ubuntu:14.04
MAINTAINER Matias Carrasco Kind <mgckind@gmail.com>

ENV HOME /root
ENV SHELL /bin/bash

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y git nano git curl nano wget dialog net-tools build-essential vim unzip libaio1
RUN apt-get install -y python
RUN apt-get install -y  python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN apt-get install -y python-software-properties
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:nginx/stable
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y nginx

RUN  rm -f /etc/nginx/sites-enabled/default
RUN mkdir -p /var/www
RUN mkdir -p /var/www/matias/


COPY config/matias /etc/nginx/sites-enabled/matias 

RUN chmod 755 /var/www
EXPOSE 80 

RUN chown -R www-data:www-data /var/www/matias/public_html

#copy files
COPY public_html  /var/www/matias/public_html
RUN /etc/init.d/nginx start

CMD ["nginx", "-g", "daemon off;"]
