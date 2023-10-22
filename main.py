import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
digimon = pd.read_csv('DigiDB_digimonlist.csv')
moveslist = pd.read_csv('DigiDB_movelist.csv')
supportlist=pd.read_csv('DigiDB_supportlist.csv')

moveslist['Best ratio']=round(moveslist['Power']/moveslist['SP Cost'],1)
moveslist.sort_values('Best ratio',ascending=False).head(3)
digimon.sort_values('Lv50 Atk',ascending=False).head(3)
digimon.sort_values('Lv50 Def',ascending=False).head(3)
def Check(msg,ind):
    mean=digimon[msg].mean()
    i = digimon[msg][ind]
    if i<mean:
        return 'Weak'
    elif i>mean:
        return 'Strong'
    else:
        return 'Mean'
lv50=['Lv 50 HP','Lv50 SP','Lv50 Atk','Lv50 Def','Lv50 Int','Lv50 Spd']
lv={}
for i in lv50:
    lv[i]=[]
    for j in range(249):
        t=Check(i,j)
        lv[i].append(t)
temp_digi=pd.DataFrame(lv)
temp_digi['Attribute']=digimon['Attribute'].copy()
stats_dig={'Attribute':[]}
for i in temp_digi['Attribute'].unique():
    stats_dig['Attribute'].append(i)
temp_dic={}
for i in lv50:
    temp_dic[i]=[0,0]
    stats_dig[i]=[]
    for k in stats_dig['Attribute']:
        for j,l in zip(temp_digi['Attribute'],temp_digi[i]):
            if k!=j:
                continue
            if l=='Weak':
                temp_dic[i][0]=temp_dic[i][0]+1
            else:
                temp_dic[i][1]=temp_dic[i][1]+1
        if temp_dic[i][0]/1.2<temp_dic[i][1]:
            stats_dig[i].append('Great')
        if temp_dic[i][0]/1.2>temp_dic[i][1]:
            stats_dig[i].append('Weak')
        if temp_dic[i][0]/1.2==temp_dic[i][1]:
            stats_dig[i].append('MID')
df_stats=pd.DataFrame(stats_dig)
df_stats
tatype = pd.DataFrame()
tatype['Attribute'] = digimon['Attribute'].copy()
tatype['Type'] = digimon['Type'].copy()
tatype['Stage'] = digimon['Stage'].copy()
tatype.drop_duplicates(inplace=True, ignore_index=True)

xsubject = ['Ultra', 'Mega', 'Ultimate', 'Armor', 'Champion', 'Rookie', 'In-Training', 'Baby']

temp = tatype.groupby('Type').Stage.value_counts()
temp_list = []
for i in range(tatype['Type'].nunique()):
    temp_list.append([])
    for j in range(len(xsubject)):
        temp_list[i].append(0)


def asi(xstr, i, ind):
    for j in range(len(xstr)):
        if xstr[j] == temp.index[i][1]:
            temp_list[ind][j] = temp[i]


for i in range(len(temp)):
    if temp.index[i][0] == 'Data':
        asi(xsubject, i, 0)

    if temp.index[i][0] == 'Free':
        asi(xsubject, i, 1)

    if temp.index[i][0] == 'Vaccine':
        asi(xsubject, i, 2)

    if temp.index[i][0] == 'Virus':
        asi(xsubject, i, 3)

plo_df = pd.DataFrame({'Data': temp_list[0], 'Free': temp_list[1], 'Vaccine': temp_list[2], 'Virus': temp_list[3]},
                      index=xsubject)
plo_df.plot.bar(rot=0, stacked=True, figsize=(9, 3))
temp_list = []
temp = tatype.groupby('Attribute').Stage.value_counts()

for i in range(tatype['Attribute'].nunique()):
    temp_list.append([])
    for j in range(len(xsubject)):
        temp_list[i].append(0)

for i in range(len(temp)):
    if temp.index[i][0] == 'Dark':
        asi(xsubject, i, 0)

    if temp.index[i][0] == 'Earth':
        asi(xsubject, i, 1)

    if temp.index[i][0] == 'Electric':
        asi(xsubject, i, 2)

    if temp.index[i][0] == 'Fire':
        asi(xsubject, i, 3)

    if temp.index[i][0] == 'Light':
        asi(xsubject, i, 4)

    if temp.index[i][0] == 'Neutral':
        asi(xsubject, i, 5)

    if temp.index[i][0] == 'Plant':
        asi(xsubject, i, 6)

    if temp.index[i][0] == 'Water':
        asi(xsubject, i, 7)

    if temp.index[i][0] == 'Wind':
        asi(xsubject, i, 8)

plo_df = pd.DataFrame(
    {'Dark': temp_list[0], 'Earth': temp_list[1], 'Electric': temp_list[2], 'Fire': temp_list[3], 'Light': temp_list[4],
     'Neutral': temp_list[5], 'Plant': temp_list[6], 'Water': temp_list[7], 'Wind': temp_list[8]}, index=xsubject)
plo_df.plot.bar(rot=0, stacked=True, figsize=(9, 5))
digimon['HP/SP']=round(digimon['Lv 50 HP']/digimon['Lv50 SP'],2)
x=[]
for i in range(len(digimon['HP/SP'])):
    x.append(i)
y=digimon['HP/SP']

plt.axhline(y=digimon['HP/SP'].mean(),color='r',linestyle='-',label="Mean")
plt.scatter(x,y)
plt.xlabel('Digimon')
plt.ylabel('HP per SP')
plt.title('Digimon HP per SP ratio Chart')

plt.show()
digimon.sort_values(by='HP/SP',ascending=False).head()
digimon.sort_values(by='HP/SP',ascending=True).head()
moveslist['Attack Type'] = 'None'
moveslist['Accuracy Rate'] = '100%'
moveslist['Attack Count'] = '1'
tem_l = []
for i in range(len(moveslist['Description'])):
    if 'all foe' in moveslist['Description'][i] or 'to all' in moveslist['Description'][i]:
        moveslist.loc[[i], ['Attack Type']] = 'all foe'
    if 'one foe' in moveslist['Description'][i]:
        moveslist.loc[[i], ['Attack Type']] = 'one foe'

    if 'accuracy' in moveslist['Description'][i]:
        w = moveslist['Description'][i]
        for j in range(len(w)):
            if 'a' == w[j] and 'c' == w[j + 1] and 'c' == w[j + 2]:
                l = w[j - 5:j - 1]
                moveslist.loc[[i], ['Accuracy Rate']] = l

    if moveslist['Description'][i][0].isnumeric():
        l = moveslist['Description'][i].split()
        moveslist.loc[[i], ['Attack Count']] = l[0]
    if 'penetrating' in moveslist['Description'][i]:
        tem_l.append(i)
        tem_l.append(moveslist['Description'][i])

moveslist = moveslist.reindex(
    columns=['Move', 'SP Cost', 'Type', 'Power', 'Attack Type', 'Attack Count', 'Accuracy Rate', 'Inheritable',
             'Best ratio', 'Description'])

moveslist.head()
