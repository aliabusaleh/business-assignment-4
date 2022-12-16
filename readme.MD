# Business Assignment #4
[source of documentation](https://docs.docker.com/engine/install/ubuntu/)
# Prerequisites
* remove any old versions of docker or libraries
```
$ sudo apt-get remove docker docker-engine docker.io containerd runc
```
* update packges on the system 
```
$ sudo apt-get update
```
* install prerequisites  
```
$ sudo apt-get install ca-certificates curl gnupg lsb-release
```
 * Add Docker’s official GPG key
 ```
$ sudo mkdir -p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
# Install Docker (Ubuntu 18.04LTS version)
* install latest version 
```
$ sudo apt install apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - 
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu `lsb_release -cs` test"
$ sudo apt update
$ sudo apt install docker-ce
```
* verify installation 
```
$ docker -v
```
* run docker hello-world 

```
$ sudo docker run hello-world
```

# Install Airflow 
[Source of instractions](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#before-you-begin)
* create directoy for the docker compose file 
```
$ sudo mkdir AirflowSetup
$ cd AirflowSetup
```
* download docker compose file 
```
$ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.4.1/docker-compose.yaml'
```
* create folders for to sync Docker with local files 
```
$ sudo mkdir ./dags ./logs ./plugins
```

* create file for local variable for docker ( this file is necessary which crosspond to UID of the user who runs the docker container)
```
$ touch .env
```

* add AIRFLOW_UID to env. file 
```
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

* before running it make sure you have debian bullseys by running this 
```
$ docker run --rm "debian:bullseye-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'
``` 

* initilize the database 
```
docker compose up airflow-init
```

