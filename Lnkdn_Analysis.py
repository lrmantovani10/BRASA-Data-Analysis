import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import random as rd

def navigate():
    global df
    try:
        u_file = input('Please enter the file desired (Updates, Followers, or Visits): ')
        u_file = u_file.title().replace(' ','')
        df = pd.read_csv('Data/L_'+u_file+'.csv')
        df.fillna(0, inplace=True)
        process(df, u_file)
        navigate()
    except Exception as e:
        print('Operation failed. Please try again.')
        print(e)
        navigate()

def process(df, u_file):
    try:
        met = input('Please enter the metric analyzed (y - axis): ')
        met = met.strip()
        s_met = met.split(' ')
        met = ''
        mety = list()
        for word in s_met:
            if len(word) >=1:
                mety.append(word)
        for word in mety:
            mam = mety.index(word)
            if mam == 0:
                mety[0] = word.title()
            else:
                mety[mam] = word.lower()
        for word in mety:
            uu = mety.index(word)
            if uu!=len(mety) and uu!=0:
                met+=(' '+word)
            else:
                met+=word
        met1 = met.title()
        fig, (ax1, ax2) = plt.subplots(2,1,constrained_layout=True)
        cols = ['red', 'blue', 'purple', 'yellow', 'green', 'orange']
        r_col = rd.choice(cols)
        cols1 = cols
        cols1.pop(cols.index(r_col))
        r_col1 = rd.choice(cols1)
        ax1.bar(df['Date'],df[met], color = r_col)
        ax1.set_xlabel('Date')
        ax1.set_ylabel(met1)
        ax1.set_xticklabels(df['Date'], rotation= 'vertical')
        ax1.set_title(met1+' Over Time', fontweight='bold')

        ax2.plot(df['Date'],df[met], c = r_col, zorder = 0)
        ax2.scatter(df['Date'],df[met], c = r_col1, zorder = 1)
        ax2.set_xlabel('Date')
        ax2.set_ylabel(met1)
        ax2.set_xticklabels(df['Date'], rotation= 'vertical')

        style.use('seaborn')
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        fig.canvas.set_window_title(met1)
        plt.show()

    except Exception as e:
        print('Operation failed. Please try again.')
        print(e)
        process(df, u_file)

navigate()

