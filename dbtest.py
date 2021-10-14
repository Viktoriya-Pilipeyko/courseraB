from pymysql import cursors
import pymysql
from pymysql.cursors import DictCursor
from pymysql import Error

list_releaseid = [['WEB' + str(490+i*10), ['beta'], ['freeze'], ['psi-finish'], ['psi-start'], ['publication'], ['publication-fact'], ['regress-finish'], ['regress-start']] for i in range(12)]

#print(list_releaseid)
#print(list_datetype)
list_beta = ['2021-12-02','2022-01-20','2022-02-17','2022-03-24','2022-04-21','2022-05-19','2022-06-23','2022-07-21','2022-08-18','2022-09-22','2022-10-20','2022-11-17']
list_freeze = ['2022-01-18','2022-02-15','2022-03-22','2022-04-19','2022-05-17','2022-06-21','2022-07-19','2022-08-16','2022-09-20','2022-10-18','2022-10-15','2022-12-06']
list_psifinish = ['2022-01-20','2022-02-17','2022-03-24','2022-04-21','2022-05-19','2022-06-23','2022-07-21','2022-08-18','2022-09-22','2022-10-20','2022-11-17','2022-12-08']
list_psistart = ['2022-01-10','2022-02-07','2022-03-14','2022-04-11','2022-05-11','2022-06-14','2022-07-11','2022-08-08','2022-09-12','2022-10-10','2022-11-07','2022-11-28']
list_publication = ['2022-01-20','2022-02-17','2022-03-24','2022-04-21','2022-05-19','2022-06-23','2022-07-21','2022-08-18','2022-09-22','2022-10-20','2022-11-17','2022-12-08']
list_publicationfact = ['2022-01-30','2022-02-27','2022-04-03','2022-05-15','2022-05-29','2022-07-03','2022-07-31','2022-08-28','2022-10-02','2022-10-30','2022-11-27','2022-12-18']
list_regressfinish = ['2022-01-10','2022-02-07','2022-03-14','2022-04-11','2022-05-11','2022-06-14','2022-07-11','2022-08-08','2022-09-12','2022-10-10','2022-11-07','2022-11-28']
list_regressstart = ['2021-12-02','2022-01-20','2022-02-17','2022-03-24','2022-04-21','2022-05-19','2022-06-23','2022-07-21','2022-08-18','2022-09-22','2022-10-20','2022-11-17']
for i in range(len(list_releaseid)):
    list_releaseid[i][1].append(list_beta[i])
    list_releaseid[i][2].append(list_freeze[i])
    list_releaseid[i][3].append(list_psifinish[i])
    list_releaseid[i][4].append(list_psistart[i])
    list_releaseid[i][5].append(list_publication[i])
    list_releaseid[i][6].append(list_publicationfact[i])
    list_releaseid[i][7].append(list_regressfinish[i])
    list_releaseid[i][8].append(list_regressstart[i])


class MDB_conn:
    def __init__(self, host, user, password, db, charset = 'utf8mb4', cursorclass = DictCursor):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.cursorclass = cursorclass
    try:
        def __enter__(self):
            self.connection = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            db = self.db,
            charset = self.charset,
            cursorclass = self.cursorclass
            )
            return self.connection
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        def __exit__(self, exc_type, exc_val, exc_tb):
            """
            Закрываем подключение.
            """
            self.connection.close()
            if exc_val:
                raise

with MDB_conn() as connection:
    cur = connection.cursor()
    for i in range(len(list_releaseid)):
        idrel = list_releaseid[i][0]
        betadate = list_releaseid[i][1][1]
        freezedate = list_releaseid[i][2][1]
        psifinishdate = list_releaseid[i][3][1]
        psistartdate = list_releaseid[i][4][1]
        publicationdate = list_releaseid[i][5][1]
        publicationfactdate = list_releaseid[i][6][1]
        regressfinishdate = list_releaseid[i][7][1]
        regressstartdate = list_releaseid[i][8][1]
        #cur.execute("select * from `releasedates` where `release_id` = 'Swell103'")
        #print(cur.fetchall())
        cur.execute(f"insert into `releasedates` values('{idrel}', 'beta', 'web', '{betadate}'),('{idrel}', 'freeze', 'web', '{freezedate}'),('{idrel}', 'psi-finish', 'web', '{psifinishdate}'),('{idrel}', 'psi-start', 'web', '{psistartdate}'),('{idrel}', 'publication', 'web', '{publicationdate}'),('{idrel}', 'publication-fact', 'web', '{publicationfactdate}'),('{idrel}', 'regress-finish', 'web', '{regressfinishdate}'),('{idrel}', 'regress-start', 'web', '{regressstartdate}')")
        connection.commit()
    #print(cur.fetchall())



        #cur.execute(f"select * from `release` where `release_id` like '{t}%'")