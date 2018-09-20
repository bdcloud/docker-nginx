#######################################
# Dockerfile to launch Nginx
#######################################

# Set the base image
FROM bdcloud/python2-base

MAINTAINER james tang <jamess@126.com>


# Package manager
RUN apt-get install -y nginx 

ADD ./run.sh /
ADD ./config_nginx.py /
#ADD ./nginx.conf /etc/nginx/
ADD ./nginx.conf /

# Expose ports
EXPOSE 8000

# Set the default command to execute
CMD ["./run.sh"]

