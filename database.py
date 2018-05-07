import pymysql
try:
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='1501002670_kvikmyndir')
    class saekjaGogn:
        def allarMyndir(self):
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM biomyndir")
            myndir = []
            for x in cur:
                myndir.append(list(x))
            return myndir
        def finnaMynd(self,myndID):
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM biomyndir WHERE myndID = %s",myndID)
            mynd = None
            for x in cur:
                mynd = list(x)
            return mynd
        def leitMynd(self,leit):
            if leit != "" and leit != " ":
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM biomyndir WHERE titill LIKE '%"+leit+"%'")
                myndir = []
                for x in cur:
                    myndir.append(list(x))
                if len(myndir) == 0:
                    return None
                else:
                    return myndir
        def dirMynd(self,myndID):
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM biodir WHERE myndID = %s",myndID)
            dir = []
            for x in cur:
                dir.append(list(x))
            if len(dir) == 0:
                return None
            else:
                return dir
        def allirDir(self):
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM directors")
            dir = []
            for x in cur:
                dir.append(list(x))
            return dir
        def finnaDir(self,dirID):
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM directors WHERE dirID = %s",dirID)
            dir = None
            for x in cur:
                dir = list(x)
            return dir
        def allarSenur(self):
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM senur")
            senur = []
            for x in cur:
                senur.append(list(x))
            return senur
        def finnaSenu(self,senID):
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM senur WHERE senID = %s",senID)
            sena = None
            for x in cur:
                sena = list(x)
            return sena
        def senurMynd(self,myndID):
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM biosen WHERE myndID = %s",myndID)
            senur = []
            for x in cur:
                senur.append(list(x))
            if len(senur) == 0:
                return None
            else:
                return senur
        def alltMynd(self,myndID):
            mynd = self.finnaMynd(myndID)
            if mynd:
                dirm = self.dirMynd(myndID)
                directors = []
                for x in dirm:
                    directors.append(self.finnaDir(x[1]))
                senm = self.senurMynd(myndID)
                senur = []
                for x in senm:
                    senur.append(self.finnaSenu(x[1]))
                allt = [mynd,directors,senur]
                return allt
            else:
                return None

    class baetaVid:
        def biomynd(self,titill,aldurstakmark,gefidUt,rating,lengd,framleidandi,myndarskjal,lysing):
            with conn.cursor() as cur:
                sql = "insert into biomyndir(titill,aldurstakmark,gefidUt,rating,lengd,framleidandi,myndarskjal,lysing) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(sql,(titill,aldurstakmark,gefidUt,rating,lengd,framleidandi,myndarskjal,lysing))
                conn.commit()
            if conn.affected_rows() > 0:
                return True
            else:
                return False
        def director(self,movieID,dirName):
            with conn.cursor() as cur:
                sql = "select dirID from directors where dirName = %s"
                cur.execute(sql,dirName)
                dirID = None
                for x in cur:
                    for i in x:
                        if i != None:
                            dirID = i
                if dirID:
                    sql = "select * from bioDir where myndID = %s and dirID = %s"
                    cur.execute(sql,(movieID,dirID))
                    if cur.fetchone():
                        return None
                    else:
                        sql = "insert into bioDir values(%s,%s)"
                        cur.execute(sql,(movieID,dirID))
                        conn.commit()
                        if conn.affected_rows() > 0:
                            return True
                else:
                    sql = "insert into directors(dirName) values(%s)"
                    cur.execute(sql,dirName)
                    dirID = cur.lastrowid
                    sql = "insert into bioDir values(%s,%s)"
                    cur.execute(sql,(movieID,dirID))
                    conn.commit()
                    if conn.affected_rows() > 0:
                        return True
        def senu(self,movieID,sena):
            with conn.cursor() as cur:
                sql = "select senID from senur where sena = %s"
                cur.execute(sql,sena)
                senID = None
                for x in cur:
                    for i in x:
                        if i != None:
                            senID = i
                if senID:
                    sql = "select * from bioSen where myndID = %s and senID = %s"
                    cur.execute(sql,(movieID,senID))
                    if cur.fetchone():
                        return None
                    else:
                        sql = "insert into bioSen values(%s,%s)"
                        cur.execute(sql,(movieID,senID))
                        conn.commit()
                        if conn.affected_rows() > 0:
                            return True
                else:
                    sql = "insert into senur(sena) values(%s)"
                    cur.execute(sql,sena)
                    senID = cur.lastrowid
                    sql = "insert into bioSen values(%s,%s)"
                    cur.execute(sql,(movieID,senID))
                    conn.commit()
                    if conn.affected_rows() > 0:
                        return True

    class uppfaera:
        def biomynd(self,titill,aldurstakmark,gefidUt,rating,lengd,framleidandi,myndarskjal,lysing,myndID):
            with conn.cursor() as cur:
                sql = "update biomyndir set titill = %s, aldurstakmark = %s, gefidUt = %s, rating = %s, lengd = %s, framleidandi = %s, myndarskjal = %s, lysing = %s where myndID = %s"
                cur.execute(sql,(titill,aldurstakmark,gefidUt,rating,lengd,framleidandi,myndarskjal,lysing,myndID))
                conn.commit()
            if conn.affected_rows() > 0:
                return True
            else:
                return False
        def director(self,movieID,dirName,nyttDirName):
            with conn.cursor() as cur:
                sql = "select dirID from directors where dirName = %s"
                cur.execute(sql,dirName)
                dirID = None
                for x in cur:
                    for i in x:
                        if i != None:
                            dirID = i
                sql = "select dirID from directors where dirName = %s"
                cur.execute(sql,nyttDirName)
                nyttDirID = None
                for x in cur:
                    for i in x:
                        if i != None:
                            nyttDirID = i
                if nyttDirID:
                    sql = "update bioDir set dirID = %s where myndID = %s and dirID = %s"
                    cur.execute(sql,(nyttDirID,movieID,dirID))
                    conn.commit()
                    if conn.affected_rows() > 0:
                        return True
                else:
                    sql = "insert into directors(dirName) values(%s)"
                    cur.execute(sql,nyttDirName)
                    nyttDirID = cur.lastrowid
                    sql = "update bioDir set dirID = %s where myndID = %s and dirID = %s"
                    cur.execute(sql,(nyttDirID,movieID,dirID))
                    conn.commit()
                    if conn.affected_rows() > 0:
                        return True
        def senu(self,movieID,sena,nySena):
            with conn.cursor() as cur:
                sql = "select senID from senur where sena = %s"
                cur.execute(sql,sena)
                senID = None
                for x in cur:
                    for i in x:
                        if i != None:
                            senID = i
                sql = "select senID from senur where sena = %s"
                cur.execute(sql,nySena)
                nySenID = None
                for x in cur:
                    for i in x:
                        if i != None:
                            nySenID = i
                if nySenID:
                    sql = "update bioSen set senID = %s where myndID = %s and senID = %s"
                    cur.execute(sql,(nySenID,movieID,senID))
                    conn.commit()
                    if conn.affected_rows() > 0:
                        return True
                else:
                    sql = "insert into senur(sena) values(%s)"
                    cur.execute(sql,nySena)
                    nySenID = cur.lastrowid
                    sql = "update bioSen set senID = %s where myndID = %s and senID = %s"
                    cur.execute(sql,(nySenID,movieID,senID))
                    conn.commit()
                    if conn.affected_rows() > 0:
                        return True

    class eyda:
        def biomynd(self,myndID):
            with conn.cursor() as cur:
                sql = "delete from biomyndir where myndID = %s"
                cur.execute(sql,myndID)
                conn.commit()
            if conn.affected_rows() > 0:
                return True
            else:
                return False
        def director(self,movieID,dirID):
            with conn.cursor() as cur:
                sql = "delete from bioDir where myndID = %s and dirID = %s"
                cur.execute(sql,(movieID,dirID))
                conn.commit()
            if conn.affected_rows() > 0:
                return True
            else:
                return False
        def senu(self,movieID,senID):
            with conn.cursor() as cur:
                sql = "delete from bioSen where myndID = %s and senID = %s"
                cur.execute(sql,(movieID,senID))
                conn.commit()
            if conn.affected_rows() > 0:
                return True
            else:
                return False
finally:
    conn.close()
