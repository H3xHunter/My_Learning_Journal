Run a command in a new container
Usage
```docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]```
```bash
docker run <name>
docker run -d <name>   -> docker attach <id container>
docker container run --name <name> -p <port_out:port_app> <server name>
docker run -v <volume> < app name>
docker -it <name>   #This is STDIN STDOUT
```
#### Stop an app
```bash
docker container stop <name>
docker container kill <name>
```
#### List all
```bash
docker image  ls
docker network ls 
docker container ls
```
Remove image
```bash
docker image rm <name>
```
Retag local image
```bash
docker tag <name> <tag>
```
Push image to a registry
```bash
docker push <dir/name>
```
Build an image
```bash
docker build -t <name>
```
Pull image from registry
```bash
docker pull <name>
```
