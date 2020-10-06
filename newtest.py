#new pandas things


#import thu vien pandas
import pandas as pd

#read sample csv file
filecsv = pd.read_csv("thongtinlienhe.csv")

#hien thi 5 hang dau
print('hien thi 5 hang dau tien')
print('--------------------------')
print(filecsv.head(5))
print('-------------*******-------------')
#hien thi 5 hang dau
print('hien thi 2 cot co ten STT va Email')
print('--------------------------')
print(filecsv[["STT","Email"]])
print('-------------*******-------------')
#lay du lieu theo dieu kien STT la 5
print('lay du lieu theo dieu kien STT la 5')
print('--------------------------')
print(filecsv[filecsv.STT == 5])
print('-------------*******-------------')

#lay du lieu theo dieu kien: STT lon hon 2 nho hon 5
print('lay du lieu theo dieu kien STT lon hon 2 nho hon 5')
print('--------------------------')
print(filecsv[(filecsv.STT >= 2) & (filecsv.STT <= 5)])
print('-------------*******-------------')

#hien thi nhung email co chua chu a
print('hien thi nhung email co chua chu a, bo qua nhung o trong')
print('--------------------------')
print(filecsv[filecsv.Email.str.contains('a').fillna(False)])
print('-------------*******-------------')
