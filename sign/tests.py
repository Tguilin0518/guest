# 6.2 Django的单元测试类django.test.TestCase 从inuttest.TestCase继承

from django.test import TestCase
from sign.models import Event, Guest  # 以发布会Event，嘉宾Guest为例



# from datetime import datetime

# from django.contrib.auth.models import User
# from sign.models import Event, Guest

# Create your tests here.
class ModelTest(TestCase):  # 创建ModelTest类 继承django.TestCase测试类
    '''模型测试'''

    def setUp(self):  # setUp的初始化方法中，分别创建一条Event，Guest数据
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000, address='shenzhen',
                             start_time='2016-08-31 02:18:22')
        Guest.objects.create(id=1, event_id=1, realname='alen', phone='13711001101', email='alen@mail.com', sign=False)

    def test_event_models(self):
        '''测试发布会表'''
        result = Event.objects.get(name="oneplus 3 event")
        self.assertEqual(result.address, "shenzhen")
        self.assertTrue(result.status)

    def test_guest_models(self):
        '''测试嘉宾表'''
        result = Guest.objects.get(phone='13711001101')
        self.assertEqual(result.realname, "alen")
        self.assertFalse(result.sign)
    # 通过test_event_models、test_guest_models查询创建的数据，断言数据是否正确


# """
class IndexPageTest(TestCase):
    '''测试index登录首页'''

    def test_index_page_renders_index_template(self):
        ''' 断言是否用给定的index.html模版响应'''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    ''' 测试登录动作'''

    def setUp(self):
        from django.contrib.auth.models import User
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

    def test_add_author_email(self):
        ''' 测试添加用户 '''
        from django.contrib.auth.models import User
        user = User.objects.get(username="admin")
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@mail.com")

    def test_login_action_username_password_null(self):
        ''' 用户名密码为空 '''
        response = self.client.post('/login_action/', {'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password null!", response.content)

    def test_login_action_username_password_error(self):
        ''' 用户名密码错误 '''
        response = self.client.post('/login_action/', {'username': 'abc', 'password': '123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error!", response.content)

    def test_login_action_success(self):
        ''' 登录成功 '''
        response = self.client.post('/login_action/', data={'username': 'admin', 'password': 'admin123456'})
        self.assertEqual(response.status_code, 302)


class EventMangeTest(TestCase):
    ''' 发布会管理 '''

    def setUp(self):
        from django.contrib.auth.models import User
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(name="xiaomi5", limit=2000, address='beijing', status=1, start_time='2017-8-10 12:30:00')
        login_user = {'username': 'admin', 'password': 'admin123456'}
        self.client.post('/login_action/', data=login_user)  # 预先登录

    def test_add_event_data(self):
        ''' 测试添加发布会 '''
        event = Event.objects.get(name="xiaomi5")
        self.assertEqual(event.address, "beijing")

    def test_event_mange_success(self):
        ''' 测试发布会:xiaomi5 '''
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)

    def test_event_manage_search_success(self):
        ''' 测试发布会搜索 '''
        response = self.client.post('/search_name/', {"name": "xiaomi5"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)


class GuestManageTest(TestCase):
    ''' 嘉宾管理 '''

    def setUp(self):
        from django.contrib.auth.models import User
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1,name="xiaomi5", limit=2000, address='beijing', status=1, start_time='2017-8-10 12:30:00')
        Guest.objects.create(realname="alen", phone=18611001100,email='alen@mail.com', sign=0, event_id=1)
        login_user = {'username': 'admin', 'password': 'admin123456'}
        self.client.post('/login_action/', data=login_user)  # 预先登录

    def test_add_guest_data(self):
        ''' 测试添加嘉宾 '''
        guest = Guest.objects.get(realname="alen")
        self.assertEqual(guest.phone, "18611001100")
        self.assertEqual(guest.email, "alen@mail.com")
        self.assertFalse(guest.sign)

    def test_event_mange_success(self):
        ''' 测试嘉宾信息: alen '''
        response = self.client.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alen", response.content)
        self.assertIn(b"18611001100", response.content)

    def test_guest_mange_search_success(self):
        ''' 测试嘉宾搜索 '''
        response = self.client.post('/search_phone/',{"phone":"18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alen", response.content)
        self.assertIn(b"18611001100", response.content)


class SignIndexActionTest(TestCase):
    ''' 发布会签到 '''

    def setUp(self):
        from django.contrib.auth.models import User
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1, name="xiaomi5", limit=2000, address='beijing', status=1, start_time='2017-8-10 12:30:00')
        Event.objects.create(id=2, name="oneplus4", limit=2000, address='shenzhen', status=1, start_time='2017-6-10 12:30:00')
        Guest.objects.create(realname="alen", phone=18611001100, email='alen@mail.com', sign=0, event_id=1)
        Guest.objects.create(realname="una", phone=18611001101, email='una@mail.com', sign=1, event_id=2)
        login_user = {'username': 'admin', 'password': 'admin123456'}
        self.client.post('/login_action/', data=login_user)

    def test_sign_index_action_phone_null(self):
        ''' 手机号为空 '''
        response = self.client.post('/sign_index_action/1/', {"phone": ""})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"phone error.", response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        ''' 手机号或发布会id错误 '''
        response = self.client.post('/sign_index_action/2/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"event id or phone error.", response.content)

    def test_sign_index_action_user_sign_has(self):
        ''' 用户已签到 '''
        response = self.client.post('/sign_index_action/2/', {"phone": "18611001101"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"user has sign in.", response.content)

    def test_sign_index_action_sign_success(self):
        ''' 签到成功 '''
        response = self.client.post('/sign_index_action/1/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"sign in success!", response.content)


# """

'''
运行所有用例：
python3 manage.py test

运行sign应用下的所有用例：
python3 manage.py test sign

运行sign应用下的tests.py文件用例：
python3 manage.py test sign.tests

运行sign应用下的tests.py文件中的 GuestManageTest 测试类：
python3 manage.py test sign.tests.GuestManageTest

'''

'''第七章：接口测试 !!!对协议接口的开发与测试'''

''' 
1、接口测试概念分类
程序接口——程序接口模块:输入输出的类 方法或函数 。一般需要使用与开发程序接口相同的编程语言，通过对类、方法、函数的调用，断言返回的结果
协议接口——不同的协议提供的接口:封装了底层代码，一般不受编程语言的限制，通过接口测试工具或其他编程语言进行测试
point!!!—对协议接口的开发与测试 
''' #接口测试概念分类

''' 
2、接口分类
1）系统与系统的接口 —— 
2）下层服务对上层服务的接口 ——  
 
    DB:数据库<-开发编写的单元测试保证代码质量-->
        service:服务器所提供的数据的处理<-接口测试在功能界面未开发出来之前对系统的接口进行测试-->
            应用层:UI层,对应浏览器页面所提供的功能、登录、注册、查询、删除<功能测试人员手工+UI自动化测试保证功能可用>
                    
3）系统内部，服务与服务之间的调用 程序之间的调用 完成查询功能的接口
''' #接口分类

'''
3、抽象的定义——接口
1)面对对象de编程语言——、java的Interface     
 接口并不是类，虽然编写接口的方式和类很相似，但        m,m  是他们属于不同的概念。类描述对象的属性和方法，接口则包含 类要实现的方法。接口无法被实例化，但是可以被实现。一个实现接口的类，必须实现接口内所描述的所有方法，否则就必须声明为抽象类。

!!!接口测试的对象是已经实现了接口的类：前端与后端交互的request请求、response响应。

2）面向对象与面向过程
面向过程python，人和程序主观体都专注于如何串联起一个程序需要的无数函数,那么多函数如何在流程上是通的, 无误的.

面向对象Java里,人的使用与程序主观体使用分离开来, 人还是在编写函数, 但从程序角度看, 主观体专注于分辨和判断函数的组织和分配问题. 之后, 人再来根据需求调用相应的函数即可.

面向过程专注于微观视角, 面向对象专注于宏观视角.

举例装修搬材料, 从材料商搬到家里, 你到底是亲力亲为每个细节都监管,甚至搬运的过程中亲手扶着一直到家来完成, 还是, 你指派一个人,比如一个小朋友来做这件事,而你只管知晓和看管-材料商 搬运 到家放下-三个节奏, 来完成.

''' #接口的定义+面对过程与面向对象

''' 
1）后端不必精通前端技术（HTML5/JavaScript/CSS），只需要专注于数据的处理并提供Web接口
django+数据库配置

2）前端的专业性越来越高，通过调用web接口获取数据，从而专注于数据展示和页面交互的设计
Bootstrap（django的一个应用）前框框架结合django开发web页面

3）开发前后端区别
（1）专业知识：前端 Web 开发人员需要精通 HTML，CSS 和 JavaScript；后端开发人员需要精通数据库，服务器，API 等技能。
（2）职位描述：前端开发人员团队设计网站的外观，并通过测试不断修改；后端开发人员团队开发软件，并构建支持前端的数据库架构。
（3）独立开发服务：除非网站是一个简单工作的静态网站，否则不能单独提供前端服务；后端服务可以作为 BaaS（后端即服务）独立提供。
（4）项目目标：前端开发人员的目标是确保所有用户都可以访问该网站或应用，并在所有视图中做出响应 —— 移动和桌面；
            后端开发人员的目标是围绕前端构建程序，并提供所需的所有支持，并确保站点或应用始终正常运行。
            
'''#第七章####web应用开发的发展趋势  前后端的开发与前后端的测试

'''
1）!!!!!!!!!!!请求的方式和数据格式，又称为API接口：
                请求方式——数据传输协议的选择（HTTP/SOAP）
                数据格式——（XML & JSON & CSV）主流的接口数据格式是 JSON
web接口：由后端开发的接口可以提供给web页面调用，也可以提供给移动App调用；
'''#第八章####web应用开发的发展趋势  前后端的开发与前后端的测试

'''
RF介绍
    目前主流的的自动化测试技术一般基于Python实现
    RobotFramework，简称RF是纯粹基于Python来实现的一款自动化测试框架，是完全开源跨平台的一款自动化测试框架
    本身是完全基于关键字驱动+数字驱动的形式来实现的，是基于自己独有的表格式编程形式来实现的 

部署环境 
    1.安装python3.7
    2.基于pip 来安装rf环境
    
    pip install robotframework -i https://pypi.tuna.tsinghua.edu.cn/simple/

    C:\Users\Administrator>pip install robotframework -i https://pypi.tuna.tsinghua.edu.cn/simple/
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple/
Collecting robotframework
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/38/43/e03efaa547a3158f0745c5ea7f1eafebd69d46f2c9aece3a8ba21992adc9/robotframework-3.2.2-py2.py3-none-any.whl (623 kB)
     |████████████████████████████████| 623 kB 819 kB/s
Installing collected packages: robotframework
Successfully installed robotframework-3.2.2

    安装完后在这个路径下——C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\robotframework-3.2.2.dist-info
    
    !!!以上安装错误：Python3.7对应robotframework3.1.2的版本
    
    
    卸载：
    C:\Users\Administrator>pip install --upgrade robotframework
Requirement already satisfied: robotframework in c:\users\administrator\appdata\local\programs\python\python37\lib\site-packages (3.2.2)

        C:\Users\Administrator>pip uninstall robotframework
Found existing installation: robotframework 3.2.2
Uninstalling robotframework-3.2.2:
  Would remove:
    c:\users\administrator\appdata\local\programs\python\python37\lib\site-packages\robot\*
    c:\users\administrator\appdata\local\programs\python\python37\lib\site-packages\robotframework-3.2.2.dist-info\*
    c:\users\administrator\appdata\local\programs\python\python37\scripts\rebot.exe
    c:\users\administrator\appdata\local\programs\python\python37\scripts\robot.exe
Proceed (y/n)? y
  Successfully uninstalled robotframework-3.2.2
  
  
   重新安装：
   C:\Users\Administrator>pip install robotframework==3.1.2
Collecting robotframework==3.1.2
  Downloading robotframework-3.1.2-py2.py3-none-any.whl (602 kB)
     |████████████████████████████████| 602 kB 364 kB/s
Installing collected packages: robotframework
Successfully installed robotframework-3.1.2
    
    再听安装包安装
    Processing dependencies for robotframework==3.1.2
    Finished processing dependencies for robotframework==3.1.2

    安装 ride
    pip install robotframework-ride
C:\Users\Administrator>pip install robotframework-ride
Collecting robotframework-ride
  Downloading robotframework-ride-1.7.4.2.tar.gz (846 kB)
     |████████████████████████████████| 846 kB 297 kB/s
Collecting Pygments
  Downloading Pygments-2.7.3-py3-none-any.whl (950 kB)
     |████████████████████████████████| 950 kB 504 kB/s
Collecting PyPubSub
  Downloading Pypubsub-4.0.3-py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 1.3 MB/s
Collecting Pywin32
  Downloading pywin32-300-cp37-cp37m-win_amd64.whl (9.2 MB)
     |████████████████████████████████| 9.2 MB 273 kB/s
Collecting wxPython<=4.0.7.post2
  Downloading wxPython-4.0.7.post2-cp37-cp37m-win_amd64.whl (23.0 MB)
     |████████████████████████████████| 23.0 MB 297 kB/s
Collecting numpy
  Downloading numpy-1.19.4-cp37-cp37m-win_amd64.whl (12.9 MB)
     |████████████████████████████████| 12.9 MB 384 kB/s
Collecting pillow
  Downloading Pillow-8.0.1-cp37-cp37m-win_amd64.whl (2.1 MB)
     |████████████████████████████████| 2.1 MB 435 kB/s
Collecting six
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Using legacy 'setup.py install' for robotframework-ride, since package 'wheel' is not installed.
Installing collected packages: six, pillow, numpy, wxPython, Pywin32, PyPubSub, Pygments, robotframework-ride
    Running setup.py install for robotframework-ride ... done
Successfully installed PyPubSub-4.0.3 Pygments-2.7.3 Pywin32-300 numpy-1.19.4 pillow-8.0.1 robotframework-ride-1.7.4.2 six-1.15.0 wxPython-4.0.7.post2


C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Scripts\ride.py
'''#第九章 PF的环境搭建 +ride

'''
pip安装的包的路径  Python37/lib/site-packages
web自动化——导入SeleniumLibrary
    pip install robotframework-seleniumlibrary  #较稳定，两个版本无缝衔接
    pip install robotframework-selenium2library #更新的版本

app自动化——导入AppiumLibrary
接口自动化——导入Requests

C:\Users\Administrator>cd Desktop\Sublime

C:\Users\Administrator\Desktop\Sublime>dir
 驱动器 C 中的卷没有标签。
 卷的序列号是 7C56-ABA8

 C:\Users\Administrator\Desktop\Sublime 的目录

2020/12/17  07:14    <DIR>          .
2020/12/17  07:14    <DIR>          ..
2020/12/17  11:22                76 test.robot
               1 个文件             76 字节
               2 个目录 25,999,667,200 可用字节

C:\Users\Administrator\Desktop\Sublime>pybot test.robot
==============================================================================
Test
==============================================================================
testcase                                                              | PASS |
------------------------------------------------------------------------------
Test                                                                  | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output:  C:\Users\Administrator\Desktop\Sublime\output.xml
Log:     C:\Users\Administrator\Desktop\Sublime\log.html
Report:  C:\Users\Administrator\Desktop\Sublime\report.html


cmd下pybot常用指令补充
                        pybot test.rebot        # 运行指定文件
                        *.rebot                 # 运行当前目录下以.robot为后缀名的测试文件
                        pybot test_a            # 运行当前test_a目录下所有用例
                        pbot ./                 # 运行当前目录下所有的测试文件
'''#第九章 RF的实操01



             

