# Program I created for graphing relevant metrics provided by Facebook through Python's Pandas and Matplotlib libraries. 
# Also includes a Typeform data grapher that traces initiated/submitted responses over time. 
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style
import random as rd
from datetime import datetime as dt
import unidecode, os, csv, ast

path = 'C:/Users/Username/BRASA_Tech/Data/'
fb = pd.read_csv(path+'Fb1.csv')
fb1 = pd.read_csv(path+'Fb2.csv')
lk1 = pd.read_csv(path+'Lk3.csv')
lk2 = pd.read_csv(path+'Lk2.csv')
lk3 = pd.read_csv(path+'Lk1.csv')
m_choice = ''
r = list()
l_names = list()
f_path = path+'BRASA_Teams.csv'

#Dictionary I had for Facebook dates before automatization
name_dic = {
'BRASA Pré':[],
'BRASA Pré Mestrado e Doutorado': [],
'NEXT' : [],
'Embaixadores': [],
'BRASA Summit' : [],
'Global Summit' : [],
'BRASA Em Casa' : [],
'Talks' : [],
'Hacks' : [],
'Bolsas BRASA' : [],
'Summer Journey': []
}
if os.path.exists(f_path):
    with open(f_path) as file:
        reader = csv.reader(file)
        for row in reader:
            for itemz in row:
                if itemz not in name_dic.keys():
                    name_dic[itemz] = []
else:
    with open(f_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([key for key in name_dic.keys()])

#Facebook Data cleanup
fb1['Post Message'].fillna('', inplace = True)
fb1['Posted'].fillna('00/00/0000',inplace = True)
for f in [lk1,lk2,lk3]:
    f['Date'].fillna('00/00/0000',inplace = True)
#Facebook Data Automatization
dindx = 1
n_lis = [name for name in name_dic.keys()]
g_list = [value for value in name_dic.values()]
for ite in fb1['Post Message'][1:]:
    try:
        mind = 0
        for key in name_dic.keys():
            kk = key.title()
            ite = ite.title()
            mdate = fb1['Posted'][dindx]
            splitzr = mdate.split(' ')[0]
            mdate = splitzr[:-4]+splitzr[-2:]
            mdate = dt.strptime(mdate, '%m/%d/%y').strftime('%d/%m/%y')
            m_split = ite.split(' ')
            i_fac = dindx-1
            for item in m_split:
                if kk in item:
                    if (i_fac) not in g_list[mind]:
                        g_list[mind].append(i_fac)
                    if mdate not in name_dic[key]:
                        name_dic[key].append(mdate)
                else:
                    k_split = kk.split(' ')
                    s_list = list()
                    for i in k_split:
                        if len(i) !=  0:
                            s_list.append(i)
                    hjindx = 0
                    for w in s_list:
                        for itm in m_split:
                            if w in itm: 
                                hjindx+=1
                                if hjindx!=len(s_list):
                                    break
                                else:
                                    if i_fac not in g_list[mind]:
                                        g_list[mind].append(i_fac)
                                    if mdate not in name_dic[key]:
                                        name_dic[key].append(mdate)
            mind+=1
        dindx+=1
    except:
        pass
h_list = list()
#Cleaning up list
for elo in g_list:
    h_list.append([])
    for tr in elo:
        try:
            h_list[-1].append(int(tr))
        except:
            pass
g_list = h_list
# Cleaning up dictionary
for k, v in name_dic.items():
    cc_list = list()
    for els in v:
        try:
            int(els)
        except:
            cc_list.append(els) 
    name_dic[k] = cc_list
print(name_dic)
print('Bem-vindo ao form de feedback do marketing!')
def standardize(var):
    var = var.title().replace(' ','')
    var = unidecode.unidecode(var)
    return var
def arrange(a, b, c, d, e, pk):
    global fb, fb1, name_dic, m_choice, lk1, lk2, lk3, r, g_list, n_lis
    gg = list()
    #Color management
    cols = ['red','maroon', 'blue', 'cyan', 'purple', 'blueviolet', 'yellow', 'orangered', 'green', 'lime', 'crimson', 'fuchsia']
    for j in range(0,4):
        h = rd.choice(cols)
        if cols.index(h) % 2 ==0:
            del cols[cols.index(h) : cols.index(h)+2]
        else:
            del cols[cols.index(h) - 1 : cols.index(h)+1]
        gg.append(h)
    # Sorting the dates in the user's group
    r = name_dic[m_choice]
    r_l = list()
    for ds in r:
        if ds not in r_l:
            r_l.append(ds)
    r = r_l
    r.sort(key=lambda date: dt.strptime(date, "%d/%m/%y"))
    gg.append(r)

    # Start date of data's time interval. Program will find right limit.
    start_date = fb['Date'][1]
    start_date = dt.strptime(start_date, '%Y-%m-%d')
    temp_l = [dt.strptime(l, '%d/%m/%y') for l in r]
    try: 
        if e == 0:
            ms = [fb[a], fb[b]]
            ooi = 'Facebook'
            i_arrange = [7, 8, 5, 6, 4]
            for ghi in [c, d]:
                fb1[ghi].fillna(0, inplace = True)
            mod_li = [gh.split(' ')[0][:-4]+gh.split(' ')[0][-2:] for gh in fb1['Posted'][1:]]
            mod_li = [dt.strptime(vy, '%m/%d/%y').strftime('%d/%m/%y') for vy in mod_li]
            cc_dic = dict()
            df_l = [[int(yu) for yu in fb1[c][1:]], [int(fg) for fg in fb1[d][1:]]]
            temp = 0
            #Working with repeated elements
            for ele in mod_li:
                if ele in r and temp in  g_list[n_lis.index(m_choice)]:
                    if ele in cc_dic.keys():
                        cc_dic[ele][0]+=df_l[0][temp]
                        cc_dic[ele][1]+=df_l[1][temp]
                    else:
                        cc_dic[ele] = []
                        for element in range(0, len(df_l)):
                            cc_dic[ele].append(df_l[element][temp])
                temp+=1 
            al = list()
            bl = list()
            for key, value in cc_dic.items():
                al.append(key)
                bl.append(value)
            bl = [x for _, x in sorted(zip(al,bl), key=lambda date: dt.strptime(date[0], "%d/%m/%y"))]
            al.sort(key=lambda item: dt.strptime(item, "%d/%m/%y"))
            gg[-1] = al
            bold = True
            for ac in bl:
                if bold:
                    gg.append([ac[0]])
                    gg.append([ac[1]])
                    bold = False
                else:
                    gg[-2].append(ac[0])
                    gg[-1].append(ac[1])
        elif e == 1:
            ms = [lk1[a], lk2[b], lk2[c], lk3[d]]
            ooi = 'LinkedIn'
            i_arrange = [5, 6, 7, 8, 4]
        cc = 0
        for v in ms:
            v.fillna(0, inplace = True)
            if not (cc == 2 and e == 1):
                try:
                    j_p = [int(v[(dx - start_date).days]) for dx in temp_l]
                except:
                    pass
            else:
                try:
                    j_p = [float(v[(dx - start_date).days])*100 for dx in temp_l]
                except:
                    pass
            if e == 1:
                gg.append(j_p)
            else: 
                gg.append([[int(k) for k in v[1:]][(iy-start_date).days] for iy in temp_l])
            cc+=1
    except:
        print('Há alguns dias no dicionário para os quais não há posts do LinkedIn correspondentes em nosso banco de dados. Tente baixar os dados do Facebook novamente com faixa de datas que incluam todas as presentes no dicionário ou altere a(s) data(s) equivocadas lá.')
        #raise SystemExit
        run(0)
    try:
        fig, ((ax1, ax2),( ax3, ax4)) = plt.subplots(2,2,constrained_layout=True)
        ax1.bar(gg[i_arrange[4]],gg[i_arrange[0]], color = gg[0])
        ax1.set_xlabel('Data')
        ax1.set_xticklabels(gg[i_arrange[4]],rotation = 'vertical')
        ax1.set_ylabel(pk[0])
        ax1.set_title(pk[1], fontweight='bold')

        ax2.bar(gg[i_arrange[4]],gg[i_arrange[1]], color = gg[1])
        ax2.set_xlabel('Data')
        ax2.set_xticklabels(gg[i_arrange[4]],rotation = 'vertical')
        ax2.set_ylabel(pk[2])
        ax2.set_title(pk[3], fontweight='bold')

        ax3.bar(gg[i_arrange[4]],gg[i_arrange[2]], color = gg[2])
        ax3.set_xlabel('Data')
        ax3.set_xticklabels(gg[i_arrange[4]],rotation = 'vertical')
        ax3.set_ylabel(pk[4])
        ax3.set_title(pk[5], fontweight='bold')

        ax4.bar(gg[i_arrange[4]], gg[i_arrange[3]], color = gg[3])
        ax4.set_xlabel('Data')
        ax4.set_xticklabels(gg[i_arrange[4]],rotation = 'vertical')
        ax4.set_ylabel(pk[6])
        ax4.set_title(pk[7], fontweight='bold')

        style.use('seaborn')
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        fig.canvas.set_window_title('Dados do '+ ooi)
        plt.show()
    except:
        print('Operação falhou. Tente novamente.')
        run(2)

def run(f_index):
    global name_dic, m_choice, f_path, g_list
    if f_index==0:
        print(''' 
        Indique o número de sua campanha, conforme listado abaixo.
        Para adicionar uma nova campanha ou data não abordada no gráfico, insira "0".
        Para visualizar dados do Typeform, insira 'T'.

        ''')
        idx = 0
        for el in name_dic:
            idx+=1
            print(el+' - '+str(idx))
            if idx == len(name_dic):
                print('')
            l_names.append(el)

        run(1)
    elif f_index == 1:
        n_choice = input('Digite um número: ')
        try:
            n_choice = int(n_choice)
        except:
            if n_choice!='T':
                print('Você não inseriu um número. Tente novamente.')
            else:
                def navigate():
                    global pf
                    try:
                        u_file = input('Insira o nome do arquivo desejado (Hacks, Global_Summit, PRÉ_AMÉRICAS,etc.): ')
                        pf = pd.read_csv(path+u_file+'.csv')
                        pf.fillna(0, inplace=True)
                        process(pf)
                    except Exception as e:
                        print('Operação falhou. Tente novamnte.')
                        print(e)
                        navigate()

                def fix_func(column):
                    i = 0
                    c_list = list()
                    while i< len(pf[column]):
                        c_list.append(1)
                        i+=1
                    #Cleaning up data
                    temp_list = list()
                    proxy_list = list()
                    s_list = list()
                    for el in pf[column]:
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


                def process(pf):
                    try:
                        fig, (ax1, ax2) = plt.subplots(2,1, constrained_layout = True)
                        els = fix_func('Submit Date (UTC)')
                        ax1.bar(els[0], els[1], color = els[2])
                        ax1.set_xlabel('Data')
                        ax1.set_ylabel('Forms')
                        ax1.set_xticklabels(els[0], rotation= 'vertical')
                        ax1.set_title('Forms enviados ao longo do tempo', fontweight='bold')
                        ax2.plot(els[0], els[1], c = els[2], zorder = 0)
                        ax2.scatter(els[0],els[1], c = els[3], zorder = 1)
                        ax2.set_xlabel('Data')
                        ax2.set_ylabel('Forms enviados')
                        ax2.set_xticklabels(els[0], rotation= 'vertical')
                        mng = plt.get_current_fig_manager()
                        mng.resize(*mng.window.maxsize())
                        fig.canvas.set_window_title('Forms finalizados')
                        
                        fig1, (i_ax1, i_ax2) = plt.subplots(2,1, constrained_layout = True)
                        els1 = fix_func('Start Date (UTC)')      
                        i_ax1.bar(els1[0],els1[1], color = els1[2])
                        i_ax1.set_xlabel('Data')
                        i_ax1.set_ylabel('Forms')
                        i_ax1.set_xticklabels(els1[0], rotation= 'vertical')
                        i_ax1.set_title('Forms iniciados ao longo do tempo', fontweight='bold')
                        i_ax2.plot(els1[0],els1[1], c = els1[2], zorder = 0)
                        i_ax2.scatter(els1[0],els1[1], c = els1[3], zorder = 1)
                        i_ax2.set_xlabel('Data')
                        i_ax2.set_ylabel('Forms iniciadas')
                        i_ax2.set_xticklabels(els1[0], rotation= 'vertical')
                        mng = plt.get_current_fig_manager()
                        mng.resize(*mng.window.maxsize())
                        fig1.canvas.set_window_title('Forms Iniciadas')
                        style.use('seaborn')
                        plt.show()
                        run(0)
                    except Exception as e:
                        print('Operation falhou. Tente novamente.')
                        print(e)
                        run(0)

                navigate()

            run(1)
        if n_choice==0:
            n_c = input('Insira o nome da campanha que deseja adicionar: ')
            if n_c not in name_dic.keys():
                name_dic[n_c] = []
                with open(f_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([key for key in name_dic.keys()])
                m_choice = name_dic[n_c]
                print('Campanha adicionada com sucesso!')
                run(0)
            else:
                print('Campanha já está no sistema. Tente novamente')
                run(1)
        else:
            try:
                m_choice = l_names[n_choice-1]
            except:
                print('Número não relacionado a uma campanha. Tente novamente.')
                run(1)
        run(2)
    elif f_index==2:
        bi_choice = input('Deseja ver dados da campanha? (digite "s") ou adicionar data que faltou no gráfico (digite "n")? Para escolher outra campanha, digite "0". ')
        bi_choice = standardize(bi_choice)
        if bi_choice == 'S':
            run(3)
        elif bi_choice == 'N':
            n_p = input('Insira o dia, mês e ano do post, no formato dd/mm/yy. ')
            n_b = input('Deseja adicionar a data de outro post (digite "s") ou ver a evolução da campanha já existente(digite "n")? ')
            n_b = standardize(n_b)
            if n_b == 'S':
                n_p = input('Insira o dia, mês e ano do post, no formato "d/m/a". (Ex: 10/03/20) ')
                try:
                    n_p = dt.strptime(n_p, "%d/%m/%y").strftime('%d/%m/%y')
                    name_dic[m_choice].append(n_p)
                    print('Data Adicionada com sucesso. ')
                    run(0)
                except:
                    print('Erro na formatação dessa data. Tente novamente.')
                    run(2)
            else:
                run(3)
        elif bi_choice=='0':
            run(0)
        else:
            print('Houve um erro em sua resposta. Tente novamente.')
            run(2)
    elif f_index == 3:
        arrange('Daily Total Reach', 'Daily Total Impressions', 'Lifetime Post Total Reach', 'Lifetime Post Total Impressions', 0, ['Reach', 'Reach Diário Total', 'Visualizações', 'Visualizações Diárias Totais da Página', 'Visualizações', 'Visualizações totais dos posts ao longo do tempo', 'Reach', 'Reach total dos posts ao longo do tempo'])
        #Disclaimer
        repeated_list = list()
        v1 = n_lis.index(m_choice)
        nlis1 = list()
        for u in n_lis:
            if n_lis.index(u)!=v1:
                nlis1.append(u)
        v2 = [int(jd) for jd in g_list[v1]]
        gg2 = list()
        for element in g_list:
            if g_list.index(element) != v1:
                gg2.append(element)
        kc = 0
        for rt in gg2:
            for itemy in rt:
                ity = int(itemy)
                if ity in v2:
                    mdate = fb1['Posted'][ity+1]
                    splitr = mdate.split(' ')[0]
                    mdate = splitr[:-4]+splitr[-2:]
                    mdate = dt.strptime(mdate, '%m/%d/%y').strftime('%d/%m/%y')
                    repeated_list.append([mdate,nlis1[kc]])
            kc+=1
                        
        if len(repeated_list) != 0:
            print('''
Outras campanhas podem ter interferido nas métricas analisadas nos gráficos, por terem sido citados no mesmo post que a sua, conforme apresentado abaixo:
            ''')
            repeated_list.sort(key=lambda item: dt.strptime(item[0], "%d/%m/%y"))
            for a in repeated_list:
                if m_choice in  a:
                    a.pop(a.index(m_choice))
                m_txt = ''
                for b in a[1:]:
                    if a.index(b) == 1:
                        m_txt+=b
                    else:
                        m_txt+=(', '+b)
                if len(m_txt) !=0:
                    print(a[0], ':', m_txt)
            print()
        run(4)
        
    elif f_index == 4:
        arrange('Total followers','Impressions (total)', 'Engagement rate (total)','Total unique visitors (total)', 1, ['Seguidores', 'Seguidores novos por dia', 'Visualizações', 'Visualizações da página ao longo do tempo', 'Engajamento (%)', 'Engajamento com a página ao longo do tempo', 'Visitantes', 'Visitantes únicos da página (total)'])
        print('Gráficos traçados com sucesso.')
        run(0)

run(0)
