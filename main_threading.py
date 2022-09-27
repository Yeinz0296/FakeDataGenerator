from datetime import datetime
import time
from faker import Faker
import pandas as pd
from random import uniform, randrange
import threading

fake_data ={
    "Timestamp":[],
    "Temperature":[],
    "Humidity":[],
}


def fakedate():
    Faker.seed(randrange(10))
    for _ in range(2500):
        random_date = Faker().date_time_between_dates(datetime_start=datetime(2022, 9, 1,00,00,00),datetime_end=datetime(2022, 9, 30,00,00,00))
        
        fake_data['Timestamp'].append(random_date)
        #print(_)

def fakedata():
    Faker.seed(randrange(10))
    for _ in range(10000):
        random_temp = round(uniform(30,50),2)
        random_humid = round(uniform(70,100),2)
        
        fake_data['Temperature'].append(random_temp)
        fake_data['Humidity'].append(random_humid)
        print(_)

start_time = time.time()

t1 = threading.Thread(target=fakedata())
t1.start()

threads = list()
for i in range(4):
    thread = threading.Thread(target=fakedate())
    thread.start()
    threads.append(thread)

t1.join()
for thread in threads:
    thread.join()

fake_data['Timestamp'].sort()
timestamp = pd.DataFrame(fake_data)
timestamp.to_csv('fastdata.csv',index=False, header=['Timestamp','Temperature','Humidity'])
print("--- {} seconds ---".format(time.time() - start_time))