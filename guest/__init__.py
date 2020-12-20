# import pymysql
# pymysql.install_as_MySQLdb()
import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库
"""
如果你使用pymysql驱动的话，上面两行必须添加。
"""

"""总结：通过django来创建一个完整、简单的web项目"""
"""
第一步：创建视图函数 
    在应用文件夹sign下面的views.py文件写视图函数
    eg：
        def index(request):#定义index函数向客户端返回字符串
            # request--envrion 请求相关数据 request叫做HTTPRequest对象，请求相关数据都是request属性
            # return HttpResponse("Hello!")
            return render(request,"index.html")   # "xx/index.html"
            # render方法用来打开html文件 对文件进行模板渲染
            # 第一个参数是request  第二个参数是html文件路径
            # django会自动过去tempaltes文件夹找html文件
            # 渲染完成之后 返回响应页面数据  最终交给wsgi中的socket  再讲页面数据返回给客户端 
""" # 第一步：创建视图函数
"""
第二步：创建html文件
    在应用文件夹sign下创建templates文件夹中创建视图html文件
    1)使用render方法时，在django的默认的templates模板相关功能的配置项中 里面指定了html文件的存放目录
        settings-templates-DIRS
            如果templates放在项目文件夹guest下 则需要找到这个根路径
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
            'DIRS':[os.path.join(BASE_DIR,'templates')]
""" # 第二步：创建html文件
"""
第N步：ORM与迁移数据库 https://www.cnblogs.com/clschao/articles/10427807.html
1)cmd: 新建库
    进入数据库管理  >mysql -u root -p
    新建数据库      >create database guestmysql default charset=utf8mb4;
    查看           > show create database guestmysql;
    
2)settings.py: 设置
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':'guestmysql',
            'HOST':'127.0.0.1',
            'POST':3306,
            'USER':'root',
            'PASSWORD':'123456',
                    }
                } # 注意: 字典中的每一项名称都是固定写法，并且必须都是大写
3)models.py
    #python的类
    class Employee(models.Model):
         id=models.AutoField(primary_key=True)
         name=models.CharField(max_length=32)
         gender=models.BooleanField()
         birthday=models.DateField()
         department=models.CharField(max_length=32)
         salary=models.DecimalField(max_digits=8,decimal_places=2)
    #python的类对象
          #添加一条表纪录:
              emp=Employee(name="alex",gender=True,birthday="1985-12-12",epartment="保洁部")
              emp.save()
          #查询一条表纪录:
              Employee.objects.filter(age=24)
          #更新一条表纪录:
              Employee.objects.filter(id=1).update(birthday="1989-10-24")
          #删除一条表纪录:
              Employee.objects.filter(name="alex").delete()
              
4)cmd:数据库迁移
    guest>python manage.py makemigrations
        No changes detected
            
    guest>python manage.py migrate
        System check identified some issues:
    
    说明:makemigrations 生成记录文件
        migrate执行记录文件 并翻译成sql 到配置数据库中生成表，执行完后
        Django会将执行过的migration文件记录到django_migration表中做一个执行记录
            记录哪些migrations文件执行过，
            再执行数据库同步指令时，则django检测并不执行已经执行的指令
        
5)cmd:新建管理员
    guest>python manage.py createsuperuser
        Username (leave blank to use 'administrator'): admin
        Email address: 2306427193@qq.com
        Password:
        Password (again):
        Superuser created successfully.
    
""" # 第三步创建数据库