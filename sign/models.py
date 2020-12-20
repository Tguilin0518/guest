from django.db import models


# Create your models here.
# 发布会
class Event(models.Model):
    name = models.CharField(max_length=100)            # 发布会标题
    limit = models.IntegerField()                      # 限制人数
    status = models.BooleanField()                     # 状态
    address = models.CharField(max_length=200)         # 地址
    start_time = models.DateTimeField('events time')   # 发布会时间
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    def __str__(self):

        return self.name


# 嘉宾
class Guest(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)   # 关联发布会id
    realname = models.CharField(max_length=64)                  # 姓名
    phone = models.CharField(max_length=16)                     # 手机号
    email = models.EmailField()                                 # 邮箱
    sign = models.BooleanField()                                # 签到状态
    create_time = models.DateTimeField(auto_now=True)           # 创建时间（自动获取当前时间）

    class Meta:
        unique_together = ('phone', 'event')

    def __str__(self):
        return self.realname


# 修改创建时间类型
# ALTER TABLE  `sign_event` CHANGE  `create_time`  `create_time`
#                                           TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
# ALTER TABLE  `sign_guest` CHANGE  `create_time`  `create_time`
#                                           TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;

"""
1)新建数据库——在models.py中把模型创建好后，执行数据库迁移
C:\\Users\\Administrator\\Desktop\\guest>
C:\\Users\\Administrator\\Desktop\\guest>python manage.py makemigrations
                在应用的migrations文件夹生成迁移文件(也就是记录文件)
C:\\Users\\Administrator\\Desktop\\guest>python manage.py migrate
                执行对应的记录文件，翻译成sql语句并到数据库中执行对应sql来创建表
            D:\>cd Django项目\guest

            D:\Django项目\guest>python manage.py makemigrations
            No changes detected
            
            D:\Django项目\guest>python manage.py migrate
            System check identified some issues:
            
            WARNINGS:
            ?: (mysql.W002) MariaDB Strict Mode is not set for database connection 'default'
                    HINT: MariaDB's Strict Mode fixes many data integrity problems in MariaDB, 
                    such as data truncation upon insertion, by escalating warnings into errors. 
                    It is strongly recommended you activate it. See: 
                    https://docs.djangoproject.com/en/3.1/ref/databases/#mysql-sql-mode
            Operations to perform:
              Apply all migrations: admin, auth, contenttypes, sessions, sign
            Running migrations:
              Applying contenttypes.0001_initial... OK
              Applying auth.0001_initial... OK
              Applying admin.0001_initial... OK
              Applying admin.0002_logentry_remove_auto_add... OK
              Applying admin.0003_logentry_add_action_flag_choices... OK
              Applying contenttypes.0002_remove_content_type_name... OK
              Applying auth.0002_alter_permission_name_max_length... OK
              Applying auth.0003_alter_user_email_max_length... OK
              Applying auth.0004_alter_user_username_opts... OK
              Applying auth.0005_alter_user_last_login_null... OK
              Applying auth.0006_require_contenttypes_0002... OK
              Applying auth.0007_alter_validators_add_error_messages... OK
              Applying auth.0008_alter_user_username_max_length... OK
              Applying auth.0009_alter_user_last_name_max_length... OK
              Applying auth.0010_alter_group_name_max_length... OK
              Applying auth.0011_update_proxy_permissions... OK
              Applying auth.0012_alter_user_first_name_max_length... OK
              Applying sessions.0001_initial... OK
              Applying sign.0001_initial... OK
              Applying sign.0002_auto_20201213_0204... OK
""" # 新建数据库——在models.py中把模型创建好后，执行数据库迁移

"""
2)执行数据库同步指令——新增非空字段  比如 : state = models.BooleanField
    a)直接在提示信息的这个位置 Select an option ：输入默认值 然后回车
    b)state = models.BooleanField(default=True) # (default='默认值') |
      state = models.BooleanField(none=True)    # 非空字段
""" # 添加 修改数据库同步指令

"""     
3)配置连接数据库
    a)先在终端创建mysql数据库
            C:\\Users\\Administrator>mysql -u root -p
            Enter password: ******
            Welcome to the MySQL monitor.  Commands end with ; or \g.
            Your MySQL connection id is 19
            Server version: 5.5.5-10.1.21-MariaDB mariadb.org binary distribution
            
            Copyright (c) 2000, 2011, Oracle and/or its affiliates. All rights reserved.
            
            Oracle is a registered trademark of Oracle Corporation and/or its
            affiliates. Other names may be trademarks of their respective
            owners.
            
            Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
            
            mysql> show databases;
            +--------------------+
            | Database           |
            +--------------------+
            | db.sqlite3         |
            | information_schema |
            | mysql              |
            | performance_schema |
            | zentao             |
            | zentaoep           |
            | zentaopro          |
            +--------------------+
            7 rows in set (0.04 sec)
            
            mysql> create database guestmysql default charset=utf8mb4;
            Query OK, 1 row affected (0.08 sec)
            
            mysql> show create database guestmysql;
            +------------+------------------------------------------------------------------------+
            | Database   | Create Database                                                        |
            +------------+------------------------------------------------------------------------+
            | guestmysql | CREATE DATABASE `guestmysql` /*!40100 DEFAULT CHARACTER SET utf8mb4 */ |
            +------------+------------------------------------------------------------------------+
            1 row in set (0.00 sec)
      
    b)在项目settins.py文件修改DATABASES = { }
            b1)pycharm操作
            DATABASES = {
                'default': {
                    # 'ENGINE': 'django.db.backends.sqlite3',
                    # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME':'guestmysql',
                            'HOST':'127.0.0.1',
                            'POST':3306,
                            'USER':'root',
                            'PASSWORD':'123456',
                            }
                        } # 注意: 字典中的每一项名称都是固定写法，并且必须都是大写
                        
            b2)cmd登录数据库操作  !!! 完整连接数据库指令 >mysql -h 127.0.0.1 -P 3306 -u root -p123456
                    C:\\Users\\Administrator>mysql -h 127.0.0.1 -P 3306 -u root -p123456
                    Welcome to the MySQL monitor.  Commands end with ; or \g.
                    Your MySQL connection id is 21
                    Server version: 5.5.5-10.1.21-MariaDB mariadb.org binary distribution
                    
                    Copyright (c) 2000, 2011, Oracle and/or its affiliates. All rights reserved.
                    
                    Oracle is a registered trademark of Oracle Corporation and/or its
                    affiliates. Other names may be trademarks of their respective
                    owners.
                    
                    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
                    
                    mysql>
                    
            b3)指定django连接mysql的模块
                    b3.1)下载pymysql  pip install pymysql
                    C:\\Users\\Administrator>pip install pymysql
                        Requirement already satisfied: pymysql in 
                        c:\\users\\administrator\\appdata\\local\\programs
                                                \\python\\python37\\lib\\site-packages (0.10.1)'
                    b3.2)在项目主目录下的__init__.py文件中指定：
                        import pymysql
                        pymysql.version_info = (1, 4, 13, "final", 0)
                        pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库
""" # 配置连接数据库

"""
4)cmd下重新创建管理员
        D:\Django项目\guest>python manage.py createsuperuser
        Username (leave blank to use 'administrator'): admin
        Email address: 2306427193@qq.com
        Password:
        Password (again):
        Superuser created successfully.

""" # 重新创建管理员
