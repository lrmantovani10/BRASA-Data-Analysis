import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import random as rd
from datetime import datetime as dt

def navigate():
    global df
    try:
        u_file = input('Please enter the file desired (Hacks, Global_Summit, PRÉ_AMÉRICAS,etc.): ')
        df = pd.read_csv('Data/T_'+u_file+'.csv')
        df.fillna(0, inplace=True)
        process(df)
    except Exception as e:
        print('Operation failed. Please try again.')
        print(e)
        navigate()

def fix_func(column):
    i = 0
    c_list = list()
    while i< len(df[column]):
        c_list.append(1)
        i+=1
    #Cleaning up data
    temp_list = list()
    proxy_list = list()
    s_list = list()
    for el in df[column]:
        el = dt.strptime(el, '%Y-%m-%d %H:%M:%S').strftime("%d/%m/%Y")
        temp_list.append(el)
    for daty in temp_list:
        if daty not in proxy_list:
            proxy_list.append(daty)
            s_list.append(c_list[temp_list.index(daty)])
            temp_list[temp_list.index(daty)] = 0
        else:
            s_list[proxy_list.index(daty)] += c_list[temp_list.index(daty)]
            temp_list[temp_list.index(daty)] = 0
    s_list = [x for _, x in sorted(zip(proxy_list,s_list), key=lambda date: dt.strptime(date[0], "%d/%m/%Y"))]
    proxy_list.sort(key=lambda date: dt.strptime(date, "%d/%m/%Y"))
    cols = ['red', 'blue', 'purple', 'yellow', 'green', 'orange']
    r_col = rd.choice(cols)
    cols1 = cols
    cols1.pop(cols.index(r_col))
    r_col1 = rd.choice(cols1)
    return [proxy_list,s_list,r_col,r_col1]


def process(df):
    try:
        fig, (ax1, ax2) = plt.subplots(2,1, constrained_layout = True)
        els = fix_func('Submit Date (UTC)')
        ax1.bar(els[0], els[1], color = els[2])
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Responses')
        ax1.set_xticklabels(els[0], rotation= 'vertical')
        ax1.set_title('Submitted Responses Over Time', fontweight='bold')
        ax2.plot(els[0], els[1], c = els[2], zorder = 0)
        ax2.scatter(els[0],els[1], c = els[3], zorder = 1)
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Responses')
        ax2.set_xticklabels(els[0], rotation= 'vertical')
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        fig.canvas.set_window_title('Responses')
        
        fig1, (i_ax1, i_ax2) = plt.subplots(2,1, constrained_layout = True)
        els1 = fix_func('Start Date (UTC)')      
        i_ax1.bar(els1[0],els1[1], color = els1[2])
        i_ax1.set_xlabel('Date')
        i_ax1.set_ylabel('Started Responses')
        i_ax1.set_xticklabels(els1[0], rotation= 'vertical')
        i_ax1.set_title('Responses Started Over Time', fontweight='bold')
        i_ax2.plot(els1[0],els1[1], c = els1[2], zorder = 0)
        i_ax2.scatter(els1[0],els1[1], c = els1[3], zorder = 1)
        i_ax2.set_xlabel('Date')
        i_ax2.set_ylabel('Started Responses')
        i_ax2.set_xticklabels(els1[0], rotation= 'vertical')
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        fig1.canvas.set_window_title('Starts of Responses')
        style.use('seaborn')
        plt.show()
        navigate()
    except Exception as e:
        print('Operation failed. Please try again.')
        print(e)
        process(df)

navigate()

