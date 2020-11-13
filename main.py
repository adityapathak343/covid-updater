import requests
import json
import os
import time
import matplotlib.pyplot as plt
import sql_handler as sql

pretotal = None

def GetData():
    print('Receiving Data...')
    try:
        raw_data = requests.get("https://api.covid19india.org/raw_data.json")
        print('Data Received!')
    except:
        print('Unable to receive data. Bad connection or server overload.')
        raise SystemExit
    return raw_data.json()


def FinalList(data_dict):
    lst = data_dict['raw_data']
    state_data = {}
    for i in lst:
        state_data[i['detectedstate']] = []
    for i in lst:
        state_data[i['detectedstate']].append({'age': i['agebracket'], 'gender': i['gender'], 'city': i['detectedcity'], 'patientnumber': i['patientnumber'], 'status': i['currentstatus']})
    return state_data


def PrintStateWise():
    global pretotal
    count_dict = {}
    for state in state_data:
        if state == '':
            unknown = len(state_data[''])
            count_dict['Unknown'] = len(state_data[''])
        else:
            count_dict[state] = len(state_data[state])
    alpha_list = sorted(count_dict)
    alpha_count = []
    for i in alpha_list:
        alpha_count.append(count_dict[i])
    plt.plot(alpha_list, alpha_count)
    plt.savefig('data.pdf')
    for i in alpha_list:
        print(i, '-' ,count_dict[i])
    total = len(data['raw_data'])
    if pretotal == None:
        pretotal = len(data['raw_data'])-unknown
    return "Total " + '- ' + str(total-unknown) + ' (+'+ str(total-pretotal) + ')'

#def CityData():


iter = 0
while True:
    print('Time since start:', 20*iter, 'seconds')
    data = GetData()
    state_data = FinalList(data)
    print(PrintStateWise())
    time.sleep(20)
    total = len(data['raw_data'])
    if iter%720 == 0:
        pretotal = total
    os.system('clear')
    sql.insertion_function(state_data)
    iter+=1
