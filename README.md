# Docker-class

The `leandro2r/docker-class` is already hosted in [Docker hub](https://hub.docker.com/r/leandro2r/docker-class).

```shell
$ docker pull leandro2r/docker-class
```

## Image build
```shell
$ docker build -t <image-name> .
```

Example:
```shell
$ docker build -t docker-class:0.0.1 .
```

## Container run (when the container is not started)
```shell
$ docker run -e ENV=VAL -it <existing-image-name> sh
$ docker run --name <container-name> -d <existing-image-name>
```

Example:
```shell
$ docker run -e DB_HOST=elastic -it docker-class:0.0.1 sh
$ docker run --name docker-class_container -d docker-class:0.0.1
```

## Container access/command run (when it's already started)
```shell
$ docker exec -it <contaner-name> sh
$ docker exec -it <contaner-name> date
```

Example:
```shell
$ docker exec -it docker-class_container sh
$ docker exec -it docker-class_container date
```

## Docker-compose
```shell    
$ docker-compose up -d
$ docker-compose pull
```

## Swarm cluster creation
```shell
$ docker swarm init --advertise-addr <ip-address>
# Docker swarm token to join the cluster
$ docker swarm join-token -q manager
$ docker swarm join --token <token> <init-ip-address>:2377
$ docker node promote <node-hostname>
```

Example:
```shell
$ docker swarm init --advertise-addr 192.168.200.178
$ docker swarm join --token <join-token> 192.168.200.178:2377
$ docker node promote docker-class
```

## Swarm node label set
```shell
$ docker node update --label-add <label>=<value> <node-hostname>
$ docker node inspect --pretty <node-hostname>
```

Example:
```shell
$ docker node update --label-add master=true $(hostname)
$ docker node inspect --pretty self
```

## Swarm stack deploy
```shell
$ docker stack deploy --compose-file=<docker-compose-file> <stack-name>
```

Example:
```shell
$ docker stack deploy --compose-file=docker-compose.yml class_stack
```

## Swarm stack list and logs
```shell
$ docker service ls
$ docker service logs <service-name> --no-trunc -f
```

Example:
```shell
$ docker service ls
$ docker service logs class_stack_api --no-trunc -f
```

## Docker help
```shell
$ docker --help
$ docker-compose --help
```

* [Docker docs](https://docs.docker.com/engine/reference/commandline/docker/)
* [Docker-compose docs](https://docs.docker.com/compose/compose-file/)
