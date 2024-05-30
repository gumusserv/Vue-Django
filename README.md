# Vue-Django
## 所需依赖
- pip install django
- pip install mysqlclient
- 安装MySQL--8.3.0
## 如何启动
- 首先，clone到本地：git clone https://github.com/gumusserv/Vue-Django.git
- cd Vue-Django
- 在终端1, cd mysite, 先后执行python manage.py makemigrations, python manage.py migrate      然后运行python manage.py runserver 127.0.0.1:8000        
- 在终端2, cd frontend, 先执行npm install -g @vue/cli，再执行npm run serve
- 在浏览器输入127.0.0.1:8080即可
