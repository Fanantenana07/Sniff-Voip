from PyQt5.QtSql import  QSqlQuery
import json
import os

    
def Authentification(username,password,db) :
    if db.open():
        find = {}
        query = "select * from users"
        cursor = QSqlQuery()
        cursor.prepare(query)
        if cursor.exec():
                while cursor.next():
                    if username == cursor.value("username") and password == cursor.value("password") :
                            find = {"value" : True,"username":cursor.value("username"),"ID":cursor.value("ID"),"state":cursor.value("State")}
                            break
                    else :
                            find = {"value" : False}
                return find                
        else :
                return QSqlQuery.lastError()
    else:
        return QSqlQuery.lastError()

def Get_All_User(db):
    if db.open():
        cursor = QSqlQuery()
        query = "select *  from users"
        cursor.prepare(query)
        item = []
        if cursor.exec() :
                if cursor.next :
                        while cursor.next() :
                                id = str(cursor.value("ID"))
                                username = cursor.value("username")
                                password = cursor.value("password")
                                date = str(cursor.value("date"))
                                state = cursor.value("State")
                                data = {"ID":id,"username":username,"password":password,"date":date,"state":state}
                                item.append(data)
                        return item
        else :
                QSqlQuery.lastError()
    else :
            db.lastError().text()

def Get_All_Audio(db):
        if db.open():
                cursor = QSqlQuery()
                query = "select *  from audio"
                cursor.prepare(query)
                item = []
                if cursor.exec() :
                        if cursor.next :
                                while cursor.next() :
                                        ID_audio = str(cursor.value("ID_audio"))
                                        Designation_audio = cursor.value("Designation_audio")
                                        Designation_capture = cursor.value("Designation_capture")
                                        Date_audio = str(cursor.value("Date_audio"))
                                        data = {"ID_audio":ID_audio,"Designation_audio":Designation_audio,"Designation_capture":Designation_capture,"Date_audio":Date_audio}
                                        item.append(data)
                                return item
                else :
                        QSqlQuery.lastError()

def Add_New_User(db,username,password,state,date):
        if db.open():
                cursor = QSqlQuery()
                query = "insert into users ('Username','Password','Date',State) values(:username,:password,:date,:state)"
                cursor.prepare(query)
                cursor.bindValue(":username",username)
                cursor.bindValue(":password",password)
                cursor.bindValue(":date",date)
                cursor.bindValue(":state",state)
                if cursor.exec() :
                        return True
                else :
                        return False
        else :
                return db.lastError().text()

def remove_user(db,ID):
        
        if db.open():
                cursor = QSqlQuery()
                query = "delete from users where ID = '"+ID+"'"
                cursor.prepare(query)
                if cursor.exec():
                        return True  
                else :
                        return False
        else :
                print(QSqlQuery.lastError())

def remove_cap(db,item):
        
        if db.open():
                raw = item.replace(".pcap",".raw")
                cursor = QSqlQuery()
                query = "delete from capture where Designation_capture = '"+item+"'"
                cursor.prepare(query)
                
                try :
                        os.remove("Pcap/"+item)
                        os.remove("Raw/"+raw)
                        if cursor.exec():
                                return True
                        else :
                                return False
                except FileNotFoundError as err:
                        return str(err)
                        
                
        else :
                print(QSqlQuery.lastError())

def remove_item_capture(db,item):
        
        if db.open():
                cursor = QSqlQuery()
                query = "delete from capture where Designation_capture = '"+item+"'"
                cursor.prepare(query)
                if cursor.exec():
                        return True
                else :
                        return False                       
        else :
                print(QSqlQuery.lastError())

def remove_item_Audio(db,item):
        if db.open():
                cursor = QSqlQuery()
                query = "delete from audio where Designation_Audio = '"+item+"'"
                cursor.prepare(query)
                if cursor.exec():
                        return True
                else :
                        return False                       
        else :
                print(QSqlQuery.lastError())

def remove_audio(db,item,name):
        if db.open():
                raw = item.replace(".pcap",".raw")
                cursor = QSqlQuery()
                query = "delete from audio where ID_audio = '"+item+"'"
                cursor.prepare(query)
                try :
                        os.remove("Audio/"+name)
                        if cursor.exec():
                                return True
                        else :
                                return False
                except FileNotFoundError as err:
                        return str(err)
        else :
                print(QSqlQuery.lastError())


def on_edit(db,ID,username,password,state,date):
        if db.open():
                query = "update users set Username = '"+username+"', Password = '"+password+"',State = '"+state+"',Date = '"+date+"' where ID = '"+ID+"'"
                cursor = QSqlQuery()
                cursor.prepare(query)
                if cursor.exec():
                        return True  
                else :
                        return False
        else :
                print(QSqlQuery.lastError())

def search_result(db,key):
        if db.open():
                cursor = QSqlQuery()
                query = "select *  from users where Designation like '%"+key+"%' or Marque like '%"+key+"%' or Volume like '%"+key+"%' or prixA like '%"+key+"%' or prixV like '%"+key+"%'"
                cursor.prepare(query)
                item = []
                if cursor.exec() :
                        if cursor.next :
                                while cursor.next() :
                                        id = str(cursor.value("ID"))
                                        username = cursor.value("username")
                                        password = cursor.value("password")
                                        date = str(cursor.value("date"))
                                        state = cursor.value("State")
                                        data = {"ID":id,"username":username,"password":password,"date":date,"state":state}
                                        item.append(data)
                                return item
                else :
                        QSqlQuery.lastError()
        else :
                db.lastError().text()

def search_result_cap (db,query):
        if db.open():
                cursor = QSqlQuery()
                cursor.prepare(query)
                item = []
                if cursor.exec() :
                        if cursor.next :
                                while cursor.next() :
                                        Designation_capture = str(cursor.value("Designation_capture"))
                                        ID_user = cursor.value("ID_user")
                                        Ip_src = cursor.value("Ip_src")
                                        Ip_dst = str(cursor.value("Ip_dst"))
                                        Date_capture = cursor.value("Date_capture")
                                        Port = cursor.value("Port")
                                        data = {"ID_user":ID_user,"Designation_capture":Designation_capture,"Ip_src":Ip_src,"Ip_dst":Ip_dst,"Date_capture":Date_capture,"Port":Port}
                                        item.append(data)
                                return item
                else :
                        QSqlQuery.lastError().text()
        else :
                db.lastError().text()
        
def Save_Call(db,name,ID_user,ip_source,ip_destination,port,date):
        if db.open():
                cursor = QSqlQuery()
                query = "insert into capture ('Designation_capture','ID_user','Ip_src','Ip_dst','Date_capture','Port') values(:name,:id,:ip_src,:ip_dst,:date,:prt)"
                cursor.prepare(query)
                cursor.bindValue(":name",name)
                cursor.bindValue(":id",ID_user)
                cursor.bindValue(":ip_src",str(ip_source))
                cursor.bindValue(":ip_dst",str(ip_destination))
                cursor.bindValue(":date",date)
                cursor.bindValue(":prt",str(port))
                cursor.exec()

def Get_All_Capture(db):
    if db.open():
        cursor = QSqlQuery()
        query = "select *  from capture"
        cursor.prepare(query)
        item = []
        if cursor.exec() :
                if cursor.next :
                        while cursor.next() :
                                Designation_capture = str(cursor.value("Designation_capture"))
                                ID_user = cursor.value("ID_user")
                                Ip_src = cursor.value("Ip_src")
                                Ip_dst = str(cursor.value("Ip_dst"))
                                Date_capture = cursor.value("Date_capture")
                                Port = cursor.value("Port")
                                data = {"Designation_capture":Designation_capture,"ID_user":ID_user,"Ip_src":Ip_src,"Ip_dst":Ip_dst,"Date_capture":Date_capture,"Port":Port}
                                item.append(data)
                        return item
        else :
                QSqlQuery.lastError()
    else :
            db.lastError().text()

def Add_New_Audio(db,designation_audio,designation_cap,date):
        if db.open():
                cursor = QSqlQuery()
                print("designation_audio"+designation_audio + "  designation_cap" + designation_cap)
                query = "insert into audio ('Designation_capture','Designation_Audio','Date_Audio') values(:cap,:audio,:date)"
                cursor.prepare(query)
                cursor.bindValue(":cap",designation_cap)
                cursor.bindValue(":audio",designation_audio)
                cursor.bindValue(":date",date)
                if cursor.exec() :
                        return True
                else :
                        return False
        else :
                return db.lastError().text()