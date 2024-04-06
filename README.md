### _Welcome to my repository!_
## 🎸 Stack:
- Language: Python🐍 version 3.10✅.
- Development approach: Django🔨 version 5.0.4🔥.
## ⚙ Installation and usage:
### Dev server
#### 1. Go to IDE and run in terminal:
    git clone https://github.com/Nerogen/Tree_Menu_Django.git
#### 2. Then run in terminal next line:
    pip install -r requirements.txt
#### 3. Nice, run in terminal next command:
    python manage.py migrate 
#### 4. Then start localhost:
    python manage.py runserver
### Docker
#### 1. Go to IDE and run in terminal:
    git clone https://github.com/Nerogen/Tree_Menu_Django.git
#### 2. You also need installed docker with compose plugin:
    guide https://docs.docker.com/engine/install/
#### 3. Then run in terminal:
    docker-compose up -d --build
### K8s
#### 1. Go to your host with kubectl and clone repo:
    git clone https://github.com/Nerogen/Tree_Menu_Django.git
#### 2. then apply files for deployment and service for access your app on 30001 port
    kubectl apply -f deploy/deploy.yaml
    kubectl apply -f deploy/service.yaml

## 😎 About site
Tree Menu is a simple representation of menus hierarchy.
![image](https://github.com/Nerogen/jenkins_pipline_for_kube/assets/72101790/1115b8b0-165a-4478-9cc1-f8ae28bbff4e)

You can modify hierarchy with Django admin, pass and login for super (admin80lvl, admin80lvl) or create new.
![image](https://github.com/Nerogen/jenkins_pipline_for_kube/assets/72101790/f0da978a-33c2-424f-b3ce-45260bffe791)
