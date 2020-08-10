import pandas as pd 
from datetime import datetime as dt
from unidecode import unidecode as ud
import csv, xlrd
f_path = 'Data//'
file_list = ['Fb1', 'Fb2', 'Lk1','Lk2', 'Lk3']
def cleanup(d_df):
    global f_path, file_list
    lis_val = list() 
    if d_df !=1:
        par = None
    else:
        par = 'utf-8'
    with open(f_path+file_list[d_df]+'.csv', encoding = par) as m_file:
        reader = csv.reader(m_file)
        gh = 0
        for item in reader:
            gh+=1
            if gh==1 and d_df == 0:
                try:
                    item[0] = ud(item[0]).split('?')[1]
                except:
                    pass
            lis_val.append(item)
    #Cleaning up list
    if d_df == 3 and 'Aggregated engagement metrics for your' in lis_val[0][0]:
        lis_val.pop(0)
    t_list = list()
    for element in lis_val:
        t_list.append([])
        for items in element:
            if len(items)==0:
                k_items = 0
            else:
                try:
                    if float(items) == int(float(items)):
                        k_items = int(float(items))
                    else:
                        k_items = float(items)
                except:
                    try:
                        k_items = str(ud(items))
                    except:
                        k_items = str(items)
            t_list[-1].append(k_items)
    with open(f_path+file_list[d_df]+'.csv', 'w', newline='') as outfile:
        mywriter = csv.writer(outfile)
        for row in t_list:
            mywriter.writerow(row)
# Turning xls files to csv
def xls_to_csv(wbk):
    global f_path
    wb = xlrd.open_workbook(f_path+wbk+'.xls')
    # Writing to file
    csv_file = open(f_path+wbk+'.csv', 'w', newline='')
    wr = csv.writer(csv_file)
    item = wb.sheet_names()[0]
    item = wb.sheet_by_name(item)
    for rownum in range(item.nrows):
        wr.writerow(item.row_values(rownum))
    csv_file.close()

#Converting LinkedIn files to csv
for u in [2,3,4]:
    xls_to_csv(file_list[u])

#Cleaning up all Facebook and LinkedIn csv files
for item in range(0, len(file_list)):
    cleanup(item)
dfs_list = [pd.read_csv(f_path+fily+'.csv').dropna() for fily in file_list]
# Filtering Data Function
def filter(df, d_cols):
    for col in list(df.columns):
        if col not in d_cols:
            df = df.drop([col], axis=1)
        m_listy = list()
    return df
metrics = [
['Date','Daily New Likes', 'Daily Page Engaged Users', 'Daily Total Reach', 'Daily Total Impressions', 'Daily Organic Reach of Page Posts', 'Daily Total Impressions of your posts'],
['Post Message', 'Posted', 'Lifetime Post Total Reach', 'Lifetime Post Total Impressions', 'Lifetime Post Impressions by people who have liked your Page', 'Lifetime Post reach by people who like your Page', 'Lifetime Talking About This (Post) by action type - like'],
[cols for cols in dfs_list[2].columns],
[cols for cols in dfs_list[3].columns],
[cols for cols in dfs_list[4].columns]
]
index = 0
for item in dfs_list:
    (filter(item,metrics[index])).to_csv(f_path+file_list[index]+'.csv',index=False)
    index+=1