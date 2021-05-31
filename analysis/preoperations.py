import pandas as pd
csv_data = pd.read_csv(r"tbCell.csv", usecols=['SECTOR_ID','LONGITUDE','LATITUDE' ])
save_path = r"coordinate.txt"
coordinate_dict = {}
for index,row in csv_data.iterrows():
     coordinate_dict[str(row['SECTOR_ID'])] = [row['LONGITUDE'], row['LATITUDE']]
with open(save_path,"a+", encoding='utf-8') as f:
     f.write(str(coordinate_dict))