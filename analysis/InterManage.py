from PySide2.QtWidgets import QInputDialog, QDialog, QLineEdit

from data.dataInput import mysql_link
def inputx():
    getx = QDialog()
    i, okPressed = QInputDialog.getInt(getx,"选择阈值","x%:", 0, 0, 1000, 1)
    if okPressed:
        inter(float(i/100))


def inter(limit):
    db = mysql_link()
    a = set()
    l = []
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS `tbC2I3`;")
    cursor.execute("CREATE TABLE `tbC2I3`(SectorA text,SectorB text,SectorC text); ")

    sql1 = "SELECT distinct ServingSector,InterferingSector,PrbABS6 FROM `tbC2Inew` where PrbABS6>'%s'" % limit
    cursor.execute(sql1)
    lvl1 = cursor.fetchall()
    for i in range(0, len(lvl1)):
        sql2 = "SELECT DISTINCT ServingSector,InterferingSector,PrbABS6 FROM `tbC2Inew` where (ServingSector='%s' AND PrbABS6>'%s') or (InterferingSector='%s' AND PrbABS6>'%s' and ServingSector!='%s')" % (
        lvl1[i][1], limit, lvl1[i][1], limit, lvl1[i][0])
        cursor1.execute(sql2)
        lvl2 = cursor1.fetchall()
        for j in range(0, len(lvl2)):
            if lvl1[i][0] == lvl2[j][0]:
                sql = "SELECT DISTINCT ServingSector,InterferingSector From `tbC2Inew` where (ServingSector='%s' AND InterferingSector='%s' and PrbABS6>'%s')or (ServingSector='%s' AND InterferingSector='%s' and PrbABS6>'%s')" % (
                lvl1[i][1], lvl2[j][1], limit, lvl2[j][1], lvl1[i][1], limit)
            elif lvl1[i][0] == lvl2[j][1]:
                sql = "SELECT DISTINCT ServingSector,InterferingSector From `tbC2Inew` where (ServingSector='%s' AND InterferingSector='%s' and PrbABS6>'%s')or (ServingSector='%s' AND InterferingSector='%s' and PrbABS6>'%s')" % (
                lvl1[i][1], lvl2[j][0], limit, lvl2[j][0], lvl1[i][1], limit)
            elif lvl1[i][1] == lvl2[j][0]:
                sql = "SELECT DISTINCT ServingSector,InterferingSector From `tbC2Inew` where (ServingSector='%s' AND InterferingSector='%s' and PrbABS6>'%s')or (ServingSector='%s' AND InterferingSector='%s' and PrbABS6>'%s')" % (
                lvl1[i][0], lvl2[j][1], limit, lvl2[j][1], lvl1[i][0], limit)
            elif lvl1[i][1] == lvl2[j][1]:
                sql = "SELECT DISTINCT ServingSector,InterferingSector From `tbC2Inew` where (ServingSector='%s' AND InterferingSector='%s' and PrbABS6>'%s')or (ServingSector='%s' AND InterferingSector='%s' and PrbABS6>'%s')" % (
                lvl1[i][0], lvl2[j][0], limit, lvl2[j][0], lvl1[i][0], limit)
            else:
                continue
            cursor2.execute(sql)
            lvl3 = cursor2.fetchall()
            for k in range(0, len(lvl3)):
                if lvl1[i][0] == lvl2[j][0]:
                    t = set((lvl1[i][0], lvl1[i][1], lvl2[j][1]))
                elif lvl1[i][0] == lvl2[j][1]:
                    t = set((lvl1[i][0], lvl1[i][1], lvl2[j][0]))
                elif lvl1[i][1] == lvl2[j][0]:
                    t = set((lvl1[i][0], lvl1[i][1], lvl2[j][1]))
                elif lvl1[i][1] == lvl2[j][1]:
                    t = set((lvl1[i][0], lvl1[i][1], lvl2[j][0]))
                if t.issubset(a) == False:
                    #print(t)
                    a.update(t)
                    l.append(t.pop())
                    l.append(t.pop())
                    l.append(t.pop())
                    #print(l)
                    cursor.execute(
                        "INSERT INTO `tbC2I3` (SectorA,SectorB,SectorC)values ('%s','%s','%s')" % (l[0], l[1], l[2]))
                    db.commit()
                    l.clear()
    cursor.close()
    cursor1.close()
    cursor2.close()
    db.close()



