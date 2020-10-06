#new pandas things


#import thu vien pandas
import pandas as pd
import random

#read sample csv file
filecsv = pd.read_csv("thongtin.csv")
#dem va in ra so cot
print('dem va in ra so hàng')
print('--------------------------')
lenlen = len(filecsv)
print(lenlen)
print('-------------*******-------------')
#them hoac xoa cot du lieu
#nam sinh tinh bang cach lay 2000 - ext*2, bo qua nhung o trong
print('them mot cot du lieu - nam sinh')
print('--------------------------')


birth_year = [(2020 - filecsv.fillna(2020).iloc[i].Ext*2 + 1) for i in range(lenlen)]
filecsv["NamSinh"] = birth_year
print('-------------*******-------------')

print('them mot cot du lieu - nam sinh 2')
print('--------------------------')
birthday = [random.randrange(1980, 2000, 1) for i in range(lenlen)]
filecsv['birthday'] = birthday
print(filecsv.tail(5))