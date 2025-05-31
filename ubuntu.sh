# обновим пакеты и репозитории
sudo apt-get update
sudo apt-get upgrade -y
# установим curl
sudo apt-get install curl -y
# установим nginx
sudo apt-get install nginx -y
# установим докер
sudo apt-get install apt-transport-https lsb-release -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
# добавим текущего пользователя в группу докер
sudo usermod -aG docker $USER
