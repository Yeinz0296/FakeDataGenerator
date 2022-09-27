from datetime import datetime
import time
from faker import Faker
import pandas as pd
from random import uniform

ts = []
temp_random=[]
humid_random=[]

fake_data ={
    "Timestamp":[],
    "Temperature":[],
    "Humidity":[],
}


start_time = time.time()
Faker.seed(0)
for _ in range(10):
    random_date = Faker().date_time_between_dates(datetime_start=datetime(2022, 9, 1,00,00,00),datetime_end=datetime(2022, 9, 30,00,00,00))
    random_temp = round(uniform(30,50),2)
    random_humid = round(uniform(70,100),2)
    
    fake_data['Timestamp'].append(random_date)
    fake_data['Temperature'].append(random_temp)
    fake_data['Humidity'].append(random_humid)
    print(_)

fake_data['Timestamp'].sort()
timestamp = pd.DataFrame(fake_data)
timestamp.to_csv('fastdata.csv',index=False, header=['Timestamp','Temperature','Humidity'])
print("--- {} seconds ---".format(time.time() - start_time))
