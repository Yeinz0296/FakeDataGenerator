from multiprocessing import Process
from datetime import datetime
import time
from faker import Faker
import pandas as pd
from random import uniform, randrange

fake_data ={
    "Timestamp":[],
    "Temperature":[],
    "Humidity":[],
}

def fakedate():
    Faker.seed(randrange(100))
    for _ in range(100):
        random_date = Faker().date_time_between_dates(datetime_start=datetime(2022, 9, 1,00,00,00),datetime_end=datetime(2022, 9, 30,00,00,00))
        
        fake_data['Timestamp'].append(random_date)
        #print(_)

def fakedata():
    Faker.seed(randrange(10))
    for _ in range(500):
        random_temp = round(uniform(1,100),2)
        random_humid = round(uniform(1,100),2)
        
        fake_data['Temperature'].append(random_temp)
        fake_data['Humidity'].append(random_humid)
        print(_)

def main():
    start_time = time.time()

    p1 = Process(target=fakedata())

    processes = list()
    for i in range(5):
        process = Process(target=fakedate())
        process.start()
        processes.append(process)
    for process in processes:
        process.join()

    p1.start()

    p1.join()

    fake_data['Timestamp'].sort()
    timestamp = pd.DataFrame(fake_data)
    timestamp.to_csv('fastdata.csv',index=False, header=['Timestamp','Temperature','Humidity'])
    print("--- {} seconds ---".format(time.time() - start_time))

if __name__ == '__main__':
    main()