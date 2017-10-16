# vault-consul-demo

```
sudo apt-get remove -y docker docker-engine docker.io
sudo apt-get install -y\
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    git;
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository -y \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update -y
sudo apt-get install -y docker-ce
sudo curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
cd /opt;
git clone https://github.com/Skuratau/vault-consul-demo.git vault
bash vault/unlocker/build.sh
cd ./vault
docker-compose up -d```
