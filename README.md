# Docker-class

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

## Docker help
```shell
$ docker --help
$ docker-compose --help
```

* [Docker docs](https://docs.docker.com/engine/reference/commandline/docker/)
* [Docker-compose docs](https://docs.docker.com/compose/compose-file/)
