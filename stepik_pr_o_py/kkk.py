list_releaseid = [['WEB' + str(490+i*10), ['beta'], ['freeze'], ['psi-finish'], ['psi-start'], ['publication'], ['publication-fact'], ['regress-finish'], ['regress-start']] for i in range(12)]

print(list_releaseid)
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
#print(list_releaseid)

for i in range(len(list_releaseid)):
    print(list_releaseid[i][0], #ид релиза
    list_releaseid[i][1][0], #beta
    list_releaseid[i][1][1], #beta date
    list_releaseid[i][2][0], #freeze
    list_releaseid[i][2][1], #freeze date
    list_releaseid[i][3][0], #psi-finish
    list_releaseid[i][3][1], #psi-finish date
    list_releaseid[i][4][0], #psi-start
    list_releaseid[i][4][1], #psi-start date 
    list_releaseid[i][5][0], #publication
    list_releaseid[i][5][1], #publication date
    list_releaseid[i][6][0], #publication-fact
    list_releaseid[i][6][1], #publication-fact date
    list_releaseid[i][7][0], #regress-finish
    list_releaseid[i][7][1], #regress-finish date
    list_releaseid[i][8][0], #regress-start
    list_releaseid[i][8][1] #regress-start date
    )