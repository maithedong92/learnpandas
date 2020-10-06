#new pandas things


#import thu vien pandas
import pandas as pd

#read sample csv file
filecsv = pd.read_csv("thongtin.csv")
print(filecsv)
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
lenlen = len(filecsv)

birth_year = [(2020 - filecsv.fillna(2020).iloc[i].Ext*2 + 1) for i in range(lenlen)]
filecsv["NamSinh"] = birth_year
print(filecsv.head(5))	
print('-------------*******-------------')
