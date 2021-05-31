import pandas as pd
csv_data = pd.read_csv(r"C:/Users/39724/Desktop/xxx地区TD-LTE网络数据-2020-09-03/10. tbC2I.csv", encoding = 'utf-8',usecols=['SCELL','NCELL','C2I_Mean' ])
save_path = r"C:/Users/39724/Desktop/xxx地区TD-LTE网络数据-2020-09-03/10. tbC2I.txt"
f = open(save_path,"a+", encoding='utf-8')
for index,row in csv_data.iterrows():
     f.write(row['SCELL'] +" "+ row['NCELL'] +" "+ str(row['C2I_Mean']) + "\n")
f.close()
