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
    class baetaVid:
        def biomynd(self):
            pass
finally:
    conn.close()