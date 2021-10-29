
docker image ls;for i in `docker image ls|grep -E "open_sports"|grep -Eo "[a-z0-9]{12}"`; do docker image rm -f $i; done; docker image ls
