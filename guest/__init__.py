# import pymysql
# pymysql.install_as_MySQLdb()
import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库
"""
如果你使用pymysql驱动的话，上面两行必须添加。
"""
