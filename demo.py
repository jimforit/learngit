import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","","mysql" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT user,password from user where user='jim'")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print "The user is %s, the password is %s" % (data[0],data[1])
:
# 关闭数据库连接
db.close()

