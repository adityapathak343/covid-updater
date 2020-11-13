import mysql.connector as sql

try:
    conn = sql.connect(host='localhost', user='covid', password='covid', database='covid_database_covid19indiaorg')
    c = conn.cursor()
except ConnectionError:
    print('Connection Error')
    raise SystemExit

def insertion_function(data_dict):
    for i in data_dict:
        if i == '':
            pass
        else:
            for j in data_dict[i]:
                execs = 'insert ignore into covid_patient_table values({},{},{},{},{},{});'
                if j['age'] == '':
                    age = 'NULL'
                else:
                    age = j['age']
                c.execute(execs.format(j['patientnumber'], '"'+j['gender']+'"', age, '"'+i+'"', '"'+j['city']+'"', '"'+j['status']+'"'))
        conn.commit()


