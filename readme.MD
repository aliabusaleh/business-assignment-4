# Assignment #4 - Workflows with Apache Airflow
## Data Science and Business Workflows
### EMJMD Big Data Management and Analytics, ULB

[Abusaleh, Ali](github.com/aliabusaleh)

[Lorencio Abril, Jose Antonio](github.com/lorenc1o)

# Prerequisites
[source of documentation](https://docs.docker.com/engine/install/ubuntu/)
* Remove any old versions of docker or libraries
```
$ sudo apt-get remove docker docker-engine docker.io containerd runc
```
* Update packages on the system 
```
$ sudo apt-get update
```
* Install prerequisites  
```
$ sudo apt-get install ca-certificates curl gnupg lsb-release
```
 * Add Docker’s official GPG key
 ```
$ sudo mkdir -p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
# Install Docker (Ubuntu 18.04LTS version)
* Install latest version 
```
$ sudo apt install apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - 
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu `lsb_release -cs` test"
$ sudo apt update
$ sudo apt install docker-ce
```
* Verify installation 
```
$ docker -v
```
* Run docker hello-world 

```
$ sudo docker run hello-world
```

# Install Airflow 
[Source of instructions](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#before-you-begin)
* Create directoy for the docker compose file 
```
$ sudo mkdir AirflowSetup
$ cd AirflowSetup
```
* Download docker compose file 
```
$ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.4.1/docker-compose.yaml'
```
* Create folders for to sync Docker with local files 
```
$ sudo mkdir ./dags ./logs ./plugins
```
* Create file for local variable for docker (this file is necessary which corresponds to UID of the user who runs the docker container)
```
$ touch .env
```
* Add AIRFLOW_UID to env. file 
```
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
* Before running the docker image, make sure you have debian bullseyes by running this 
```
$ docker run --rm "debian:bullseye-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'
``` 
* Now, initialize the image 
```
docker compose up airflow-init
```
