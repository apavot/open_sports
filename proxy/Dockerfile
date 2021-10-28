# set alpine as the base image of the Dockerfile
FROM alpine:latest

# update the package repository and install Tor
RUN apk update && \
    apk add tor curl && \
    rm /var/cache/apk/* 

# Copy over the torrc created above and set the owner to `tor`
COPY torrc /etc/tor/torrc
# RUN for i in `tor --hash-password abc123|grep -Eo '16:[A-Z0-9]{58}'`; do sed 's/PASSWORD_TOKEN/'$i'/g' /etc/tor/torrc2 > /etc/tor/torrc; done;
RUN chown -R tor /etc/tor

EXPOSE 9050
EXPOSE 9051

# Set `tor` as the default user during the container runtime
USER tor

# Set `tor` as the entrypoint for the image
ENTRYPOINT ["tor"]

# Set the default container command
# This can be overridden later when running a container
CMD ["-f", "/etc/tor/torrc"]