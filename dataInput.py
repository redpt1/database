import pymysql
import xlrd
import sys

'''
    连接数据库
    args：db_name（数据库名称）
    returns:db

'''


def mysql_link():
    try:
        db = pymysql.connect(host="39.102.140.167", user="root",
                             passwd="whatafuck123924",
                             db="my_db",
                             charset='utf8')
        return db
    except:
        print("could not connect to mysql server")


'''
    读取excel函数
    args：excel_file（excel文件，目录在py文件同目录）
    returns：book
'''


def open_excel(excel_file):
    try:
        book = xlrd.open_workbook(excel_file)  # 文件名，把文件与py文件放在同一目录下
        print(sys.getsizeof(book))
        return book
    except:
        print("open excel file failed!")


'''
    执行插入操作
    args:db_name（数据库名称）
         table_name(表名称）
         excel_file（excel文件名，把文件与py文件放在同一目录下）

'''


def type_judge(data, stdtype, num,row):
    flag = 1
    for i in range(num):
        if data[i] == stdtype[i]:
            continue
        else:
            print("第%s列第%s行出现格式错误，预期是%s，实际输入%s" % (num,row,stdtype[i],data[i]))
            flag = 0
    return flag

def sql_assemble(stdtype,tablename,heads):
    sql = "INSERT INTO " + tablename +" ("
    for i in range(len(stdtype)-1):
        sql = sql + heads[i] +","
    sql = sql + heads[i+1]
    sql = sql + ") VALUES("
    for i in range(len(stdtype)-1):
        #if stdtype[i]==1:
        sql = sql + "%s,"
        #else:
        #    sql = sql + "%d,"
    sql = sql + "%s);"
    print (sql)
    return sql

def tbKPI_cleaning(excel_file):
    book = xlrd.open_workbook(excel_file)
    sh = book.sheets()[0]
    db = mysql_link()
    cursor = db.cursor()
    cursor2 = db.cursor()
    list = []
    rnum = sh.nrows
    std_type = sh.row_types(1)
    num = 0

def tbCell_cleaning(excel_file):
    book = xlrd.open_workbook(excel_file)
    sh = book.sheets()[0]
    db = mysql_link()
    cursor = db.cursor()
    cursor2=db.cursor()
    list = []
    rnum = sh.nrows
    std_type = sh.row_types(1)
    num = 0

    sql = sql_assemble(std_type, "`tbCell`", sh.row_values(0))
    for i in range(1, rnum):
        row_data = sh.row_values(i)
        flag = type_judge(sh.row_types(i), std_type, sh.row_len(i),i)
        if flag == 0:
            continue
        elif flag == 1:
            if float(sh.row_values(i)[11]) > 120 or float(sh.row_values(i)[12]) > 40:
                print("经纬度错误：第%s行" % i)
            else:
                rep_check = "SELECT * FROM `tbCell` WHERE SECTOR_ID='%s'"%sh.row_values(i)[1]
                cursor2.execute(rep_check)
                check = cursor2.fetchone()
                db.commit()
                if check!=None:
                    print("发现重复：%s（第%d行）"%(sh.row_values(i),i))
                    rep_delete = "DELETE FROM `tbCell` WHERE SECTOR_ID='%s'" % sh.row_values(i)[1]
                    cursor.execute(rep_delete)
                    db.commit()
                    print("删除重复完成")
                row_data[3]=str(row_data[3])
                rdata = tuple(row_data)
                list.append(rdata)
                num += 1
                print(num)
        if num>=1000:
            print("插入1000条数据，到%s"%i)
            cursor.executemany(sql,list)
            list.clear()
            num=0
            db.commit()
    cursor.executemany(sql,list)
    print("插入剩余不足1000条的数据，到%s"%i)
    cursor.close()
    cursor2.close()
    db.close()


def store_to(table_name, excel_file):
    db = mysql_link()  # 打开数据库连接
    cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
    list = []  # 定义列表用来存放数据

    book = open_excel(excel_file)  # 打开excel文件
    sheets = book.sheet_names()  # 获取所有sheet表名
    for sheet in sheets:
        sh = book.sheet_by_name(sheet)  # 打开每一张表
        row_num = sh.nrows
        print(row_num)

        num = 0  # 用来控制每次插入的数量
        for i in range(1, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
            row_data = sh.row_values(i)  # 按行获取excel的值
            value = (row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5],
                     row_data[6], row_data[7], row_data[8], row_data[9], row_data[10], row_data[11], row_data[12],
                     row_data[13], row_data[14])
            list.append(value)  # 将数据暂存在列表
            num += 1
            if (num >= 10000):  # 每一万条数据执行一次插入
                print(sys.getsizeof(list))
                sql = "INSERT INTO " + table_name + " (time, xingbie, afdd, xzb, yzb, cfbj, jjlbmc, \
                bjlbmc, bjlxmc, bjlxxlmc, gxqymc,gxdwmc, afql, afxqxx, cjdwmc)\
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.executemany(sql, list)  # 执行sql语句

                num = 0  # 计数归零
                list.clear()  # 清空list
                print("worksheets: " + sheet + " has been inserted 10000 datas!")  # 将剩下不足10000的数据执行插入　　
        sql = "INSERT INTO " + table_name + " (time, xingbie, afdd, xzb, yzb, cfbj, jjlbmc, \
                bjlbmc, bjlxmc, bjlxxlmc, gxqymc,gxdwmc, afql, afxqxx, cjdwmc)\
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql, list)  # 执行sql语句
        print("worksheets: " + sheet + " has been inserted " + len(list) + " datas!")
        list.clear()  # 清空list
    print("worksheets: " + sheet + " has been inserted " + str(row_num) + " datas!")
    db.commit()  # 提交
    cursor.close()  # 关闭连接
    db.close()



