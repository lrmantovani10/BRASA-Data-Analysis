import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style
import random as rd
import datetime, unidecode

df = pd.read_csv('Data/Facebook.csv')
m_list = list()
for val in df.columns:
    c = val.title()
    c = unidecode.unidecode(c)
    m_list.append(c)
df.columns = m_list

def gx(p1, p2):
    global cols
    p1 = unidecode.unidecode(p1)
    p1 = p1.title()
    p2 = unidecode.unidecode(p2)
    p2 = p2.title()
    p1w = ''
    p2w = ''
    for val in p1.split():
        p1w+=val
        if not p1.split().index(val) == len(p1.split()) -1:
            p1w+=' '
    for val in p2.split():
        p2w+=val
        if not p2.split().index(val) == len(p2.split()) -1:
            p2w+=' '
    p1 = p1w
    p2 = p2w
    df[p1].fillna(0, inplace=True)
    dy = list([int(k) for k in df[p1][1:]])
    #left border of data's time interval. Program will find right border.
    start_date = df['Date'][1]
    start_period = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_period = start_period + datetime.timedelta(days=(len(dy)-1))
    r = pd.date_range(start=start_date, end = end_period, freq="D").strftime('%d/%m')
    r_col = rd.choice(cols)
    #Graphics
    fig, (ax1, ax2) = plt.subplots(2,1, constrained_layout=True)
    ax1.bar(r,dy, color = r_col)
    ax1.set_xlabel('Date')
    ax1.set_ylabel(p2)
    ax1.set_xticklabels(r, rotation= 'vertical')
    ax1.set_title(p1, fontweight='bold')

    cols1 = cols
    cols1.pop(cols.index(r_col))
    r_col1 = rd.choice(cols1)
    ax2.plot(r,dy, c = r_col, zorder = 0)
    ax2.scatter(r,dy, c = r_col1, zorder = 1)
    ax2.set_xlabel('Date')
    ax2.set_ylabel(p2)
    ax2.set_xticklabels(r, rotation= 'vertical')

    style.use('seaborn')
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    fig.canvas.set_window_title(p1)
    plt.show()

cols = ['red', 'blue', 'purple', 'yellow', 'green', 'orange']

def M_Choices():
    param = input("Please enter what data you wish to find and the evaluated variable (Example: Daily Unlikes). Enter 'Territory Reach' for territory-specific data. ")
    param = param.title()
    k = ''
    for val in param.split():
        k+=val
        if not param.split().index(val) == len(param.split()) -1:
            k+=' '
    param = k
    if param == 'Territory Reach':
        c_choice(0)
    else:
        varb = input("Enter the graph's y-axis label (Example: 'Unlikes' for a graph of Daily Unlikes). ")
    try:
        gx(param, varb)
        M_Choices()
    except:
        print('No data available in database for the specification provided.')
        M_Choices()

def c_choice(p1):
    if p1==0:
        bol = input('Do you want to know the reach in other countries besides Brazil? (y = Yes/ n = No, I want data for Brazil. / Other: Back to broad questions.) ')
        bol = unidecode.unidecode(bol)
        bol = bol.replace(' ','')
        if bol=='y':
            c_choice(1)
        elif bol=='n':
            c_choice(2)
        else:
            M_Choices()
    elif p1==1:
        lo = input('Enter country ISO 3166 code (ex: BR for Brazil) ')
        try:
            gx('Weekly Reach by Country - '+lo, 'Reach')
            c_choice(4)
        except:
            print('Country not found. Please try again.')
        try:
            gx('Lifetime likes by Country - '+lo, 'Likes')
        except:
            print("No lifetime likes data for this country.")
        c_choice(0)

    elif p1==2:
        s_c = input("Do you want to locate Brazilian cities' reach? (y = Brazilian / n = International / Other: Go back to country selection.) ")
        s_c = unidecode.unidecode(s_c)
        s_c = s_c.replace(' ','')
        if s_c=='y':
            c_choice(p1=3)
        elif s_c=='n':
            c_choice(p1=4)
        else:
            c_choice(0)
    elif p1==3:
        b_s = input('Enter city and state (ex: Uberlândia, MG) ')
        try:
            gx('Weekly Reach by City - '+b_s+', Brazil', 'Reach')
            gx( 'Lifetime likes by City - '+b_s+', Brazil', 'Likes')
            c_choice(0)
        except:
            print('Missing data. Please try again.')
            c_choice(p1=3)
    else:
        b_c = input('Enter international city and state (ex: Dallas, TX / Palo Alto, CA for US cities or or Berlin, Germany / Montpellier, France for European cities). Leave blank if you want to find a Brazilian city. ')
        if len(b_c)==0:
            c_choice(3)
        else:
            try:
                gx('Weekly Reach by City - '+b_c, 'Reach')
                c_choice(0)
            except:
                print('City not found. Please try again.')
                c_choice(2)

M_Choices()
