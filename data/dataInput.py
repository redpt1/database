from openpyxl import load_workbook

import sqlConnect
import xlrd
import pandas as pd
import openpyxl

'''
    连接数据库
    args：db_name（数据库名称）
    returns:db

'''


i = 0
rnum = 0


def mysql_link():
    try:
        db = sqlConnect.connectdb()
        return db
    except:
        print("could not connect to mysql server")


def type_judge(data, stdtype, row):
    flag = 1
    for i in range(len(data)):
        if data[i] == stdtype[i]:
            continue
        else:
            if i>=4 and data[i]==1:
                continue
            else:
                #print("第%s列第%s行出现格式错误，预期是%s，实际输入%s" % (i,row,stdtype[i],data[i]))
                flag = 0
    return flag


def type_judgetb(data, stdtype, row):
    flag = 1
    for i in range(len(data)):
        if data[i] == stdtype[i]:
            continue
        else:
            #print("第%s列第%s行出现格式错误，预期是%s，实际输入%s" % (i,row,stdtype[i],data[i]))
            flag = 0
    return flag

def type_judgeprb(data, stdtype, row):
    flag = 1
    for i in range(len(data)):
        if type(data[i]) == type(stdtype[i]):
            continue
        else:
            print("第%s列第%s行出现格式错误，预期是%s，实际输入%s" % (i,row,stdtype[i],data[i]))
            flag=0
    return flag

def sql_assemble(stdtype,tablename,heads):
    sql = "INSERT INTO " + tablename +" ("
    for i in range(len(stdtype)-1):
        sql = sql + '`'+heads[i] +'`'+","
    sql = sql + '`'+heads[i+1]+'`'
    sql = sql + ") VALUES("
    for i in range(len(stdtype)-1):
        sql = sql + "%s,"
    sql = sql + "%s)"
    print(sql)
    return sql


def tbCell_cleaning(excel_file):
    global i
    global rnum
    book = xlrd.open_workbook(excel_file)
    sh = book.sheets()[0]
    db = mysql_link()
    cursor = db.cursor()
    cursor2=db.cursor()
    list = []
    rnum = sh.nrows
    std_type = sh.row_types(1)
    num = 0
    log = open('log_tbcell.txt', mode='w')

    sql = sql_assemble(std_type, "`tbCell`", sh.row_values(0))

    for i in range(1, rnum):
        row_data = sh.row_values(i)
        flag = type_judgetb(sh.row_types(i), std_type, i)
        if flag == 0:
            log.write("\n格式错误：%s行"%i)
        elif flag == 1:
            if float(sh.row_values(i)[11]) > 120 or float(sh.row_values(i)[12]) > 40:
                #print("经纬度错误：第%s行" % i)
                log.write("\n经纬度错误：第%s行" % i)
                log.write(str(sh.row_values(i)))
            else:
                rep_check = "SELECT * FROM `tbCell` WHERE SECTOR_ID='%s'"%sh.row_values(i)[1]
                cursor2.execute(rep_check)
                check = cursor2.fetchone()
                db.commit()
                if check!=None:
                    #print("发现重复：%s（第%d行）"%(sh.row_values(i),i))
                    rep_delete = "DELETE FROM `tbCell` WHERE SECTOR_ID='%s'" % sh.row_values(i)[1]
                    cursor.execute(rep_delete)
                    db.commit()
                    #print("删除重复完成")
                row_data[3] = int(row_data[3])
                row_data[3]=str(row_data[3])
                rdata = tuple(row_data)
                list.append(rdata)
                num += 1
        if num>=1000:
            #print("插入100条数据，到%s"%i)
            cursor.executemany(sql,list)
            list.clear()
            num=0
            db.commit()

    cursor.executemany(sql,list)
    #print("插入剩余不足1000条的数据，到%s"%i)
    db.commit()

    cursor.close()
    log.close()
    cursor2.close()
    db.close()

def  tbKPI_cleaning(excel_file):
    global i
    global rnum
    book = xlrd.open_workbook(excel_file)
    sh = book.sheets()[0]
    db = mysql_link()
    cursor = db.cursor()
    cursor2=db.cursor()
    list = []
    rnum = sh.nrows
    std_type = sh.row_types(8)
    num = 0
    log = open('log_tbKPI.txt', mode='w')

    sql = sql_assemble(std_type, "`tbKPI`", sh.row_values(0))
    for i in range(1, rnum):
        row_data = sh.row_values(i)
        for j in range(len(row_data)):
            if row_data[j]=='NIL':
                row_data[j]=None
        flag = type_judge(sh.row_types(i), std_type, i)
        if flag == 0:
            print(row_data)
            continue
        elif flag == 1:
            if float(sh.row_values(i)[19]) < 0:
                #print("数据内容错误：第%s行" % i)
                log.write("数据内容错误：第%s行" % i)
                log.write(str(sh.row_values(i)))
            else:
                rep_check = "SELECT * FROM `tbKPI` WHERE `起始时间`='%s' AND `小区名称`='%s'" %(sh.row_values(i)[0],sh.row_values(i)[3])
                cursor2.execute(rep_check)
                check = cursor2.fetchone()
                db.commit()
                if check != None:
                    #print("发现重复：%s（第%d行）" % (sh.row_values(i), i))
                    rep_delete = "DELETE FROM `tbKPI` WHERE `起始时间`='%s' AND `小区名称`='%s'" %(sh.row_values(i)[0],sh.row_values(i)[3])
                    cursor.execute(rep_delete)
                    db.commit()
                    #print("删除重复完成")
                rdata = tuple(row_data)
                list.append(rdata)
                num += 1
        if num >= 100:
            #print("插入100条数据，到%s" % i)
            cursor.executemany(sql, list)
            list.clear()
            num = 0
            db.commit()
    cursor.executemany(sql, list)
    #print("插入剩余不足100条的数据，到%s" % i)
    db.commit()
    cursor.close()
    log.close()
    cursor2.close()
    db.close()


def tbPRB_cleaning(excel_file2):
    global i
    global rnum
    rnum=93025
    datapd = pd.read_csv(excel_file2,nrows=5)
    db = mysql_link()
    cursor = db.cursor()
    cursor2 = db.cursor()
    list = []
    chunks = []
    std_type = datapd.iloc[1].values
    num = 0

    i_chunk = 0
    nrows = 1000
    skiprows = 0


    sql = sql_assemble(std_type, "`tbPRB`", datapd.columns.values)
    df_chunk = pd.read_csv(
            excel_file2,chunksize=1000)
        # When there is no data, we know we can break out of the loop.

    for k in df_chunk:
        for t in range(0,len(k)):
            row_data = k.iloc[t].values
            flag = type_judgeprb(k.iloc[t].values, std_type, t)
            if flag == 0:
                continue
            elif flag == 1:
                '''rep_check = "SELECT * FROM `tbPRB` WHERE `起始时间`='%s' AND `小区名`='%s'" % (
                sh.row_values(i)[0], sh.row_values(i)[3])
                    cursor2.execute(rep_check)
                    check = cursor2.fetchone()
                    db.commit()
                    if check != None:
                        print("发现重复：%s（第%d行）" % (sh.row_values(i), i))
                        rep_delete = "DELETE FROM `tbPRB` WHERE `起始时间`='%s' AND `小区名`='%s'" % (
                        sh.row_values(i)[0], sh.row_values(i)[3])
                        cursor.execute(rep_delete)
                        db.commit()
                        print("删除重复完成")'''
                rdata = tuple(row_data)
                list.append(rdata)
                num+=1
                i = num

        print("共插入数据%s" % num)
        cursor.executemany(sql, list)
        list.clear()
        db.commit()
        i_chunk += 1

    cursor.executemany(sql, list)
    db.commit()
    cursor.close()
    cursor2.close()
    db.close()