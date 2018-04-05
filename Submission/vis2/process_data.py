import numpy as np
import pandas as pd

# Clearing out the apostrophe and other non understandable symbols
mozilla = pd.read_csv('data/20171013111831-SurveyExport.csv',encoding='ISO-8859-1',low_memory=False)

mozilla = mozilla.replace({'Ûª': '\''}, regex=True)
mozilla = mozilla.replace({'åÊ': '\''}, regex=True)

mozilla.columns = mozilla.columns.str.replace('Ûª', '\'')
mozilla.columns = mozilla.columns.str.replace('åÊ', '')

mozilla.columns = mozilla.columns.str.replace(':You\'re planning on buying your next cool new tech toy. Maybe it\'s a smart TV or a new smartphone. Take a look at the items below and arrange them in order of importance as you make that purchase.', '')

retain_cols = ['Country','Price','Features','Safety','Security','Privacy','Reliability','User Reviews','Expert Recommendation','Friend or Family Recommendation','Convenience']

mozilla = mozilla[retain_cols]

# Dropping those rows which don't have anything specified
# Keep only those rows which have everything specified 
mozilla = mozilla.dropna()

mozilla['Price'] = mozilla['Price'].astype(int).astype(str)
mozilla['Features'] = mozilla['Features'].astype(int).astype(str)
mozilla['Safety'] = mozilla['Safety'].astype(int).astype(str)
mozilla['Security'] = mozilla['Security'].astype(int).astype(str)
mozilla['Privacy'] = mozilla['Privacy'].astype(int).astype(str)
mozilla['Reliability'] = mozilla['Reliability'].astype(int).astype(str)
mozilla['User Reviews'] = mozilla['User Reviews'].astype(int).astype(str)
mozilla['Expert Recommendation'] = mozilla['Expert Recommendation'].astype(int).astype(str)
mozilla['Friend or Family Recommendation'] = mozilla['Friend or Family Recommendation'].astype(int).astype(str)
mozilla['Convenience'] = mozilla['Convenience'].astype(int).astype(str)

totalrecordsbycountry = mozilla.groupby('Country').count()['Price'].values
countries = mozilla['Country'].unique()
countries.sort()
countries = countries.tolist()

count1s = []
countpercountry1 = []
for i in range(0, len(countries)):
    for k in range(0,10):
        countpercountry1.append(int(0))
    count1s.append(countpercountry1)
    countpercountry1 = []         

count10s = []
countpercountry10 = []
for i in range(0, len(countries)):
    for k in range(0,10):
        countpercountry10.append(int(0))
    count10s.append(countpercountry10)
    countpercountry10 = []         

for index,row in mozilla.iterrows():
    if row['Price'] == '1':
        count1s[countries.index(row['Country'])][0] += 1
    elif row['Features'] == '1':
        count1s[countries.index(row['Country'])][1] += 1
    elif row['Safety'] == '1':
        count1s[countries.index(row['Country'])][2] += 1
    elif row['Security'] == '1':
        count1s[countries.index(row['Country'])][3] += 1
    elif row['Privacy'] == '1':
        count1s[countries.index(row['Country'])][4] += 1
    elif row['Reliability'] == '1':
        count1s[countries.index(row['Country'])][5] += 1
    elif row['User Reviews'] == '1':
        count1s[countries.index(row['Country'])][6] += 1
    elif row['Expert Recommendation'] == '1':
        count1s[countries.index(row['Country'])][7] += 1
    elif row['Friend or Family Recommendation'] == '1':
        count1s[countries.index(row['Country'])][8] += 1
    elif row['Convenience'] == '1':
        count1s[countries.index(row['Country'])][9] += 1

for index,row in mozilla.iterrows():
    if row['Price'] == '10':
        count10s[countries.index(row['Country'])][0] += 1
    elif row['Features'] == '10':
        count10s[countries.index(row['Country'])][1] += 1
    elif row['Safety'] == '10':
        count10s[countries.index(row['Country'])][2] += 1
    elif row['Security'] == '10':
        count10s[countries.index(row['Country'])][3] += 1
    elif row['Privacy'] == '10':
        count10s[countries.index(row['Country'])][4] += 1
    elif row['Reliability'] == '10':
        count10s[countries.index(row['Country'])][5] += 1
    elif row['User Reviews'] == '10':
        count10s[countries.index(row['Country'])][6] += 1
    elif row['Expert Recommendation'] == '10':
        count10s[countries.index(row['Country'])][7] += 1
    elif row['Friend or Family Recommendation'] == '10':
        count10s[countries.index(row['Country'])][8] += 1
    elif row['Convenience'] == '10':
        count10s[countries.index(row['Country'])][9] += 1
        
factors = ['Price','Features','Safety','Security','Privacy','Reliability','User Reviews','Expert Recommendation','Friend or Family Recommendation','Convenience']

highestprior = []
for i in range(0,len(count1s)):
    maxval = max(count1s[i])
    highestprior.append(factors[count1s[i].index(maxval)])

lowestprior = []
for i in range(0,len(count10s)):
    maxval = max(count10s[i])
    lowestprior.append(factors[count10s[i].index(maxval)])

count1s = np.asarray(count1s)
count10s = np.asarray(count10s)

countries1 = []
countries1.append(countries)
countries = countries1
countries = np.asarray(countries)

highestprior1 = []
highestprior1.append(highestprior)
highestprior = highestprior1
highestprior = np.asarray(highestprior)

lowestprior1 = []
lowestprior1.append(lowestprior)
lowestprior = lowestprior1
lowestprior = np.asarray(lowestprior)

tmp = np.concatenate((countries.T,count1s),axis=1)
allhighestpriorityvalues = np.concatenate((tmp,highestprior.T),axis=1)

tmp2 = np.concatenate((countries.T,count10s),axis=1)
alllowestpriorityvalues = np.concatenate((tmp2,lowestprior.T),axis=1)

countrynameid = pd.read_csv('data/world-country-names.tsv',sep='\t')

mapids = []
for i in range(0,len(countries[0])):
    mapids.append('1000')
for i in range(0,len(countries[0])):
    for index,row in countrynameid.iterrows():
        if (str(countries[0][i]) in row['name']):
            mapids[i] = int(row['id'])

mapids1 = []
mapids1.append(mapids)
mapids = mapids1
mapids = np.asarray(mapids)

allhighestpriorityvalues = np.concatenate((allhighestpriorityvalues,mapids.T),axis=1)

alllowestpriorityvalues = np.concatenate((alllowestpriorityvalues,mapids.T),axis=1)

column_names_high = ['Country','Price','Features','Safety','Security','Privacy','Reliability','User Reviews','Expert Recommendation','Friend or Family Recommendation','Convenience','Priority','mapID']

column_names_low = ['Country','Price','Features','Safety','Security','Privacy','Reliability','User Reviews','Expert Recommendation','Friend or Family Recommendation','Convenience','Priority','mapID']

column_names1_high = []
column_names1_high.append(column_names_high)
column_names_high = column_names1_high
column_names_high = np.asarray(column_names_high)

column_names1_low = []
column_names1_low.append(column_names_low)
column_names_low = column_names1_low
column_names_low = np.asarray(column_names_low)

total_highest = np.concatenate((column_names_high,allhighestpriorityvalues),axis=0)
total_lowest = np.concatenate((column_names_low,alllowestpriorityvalues),axis=0)

df_high = pd.DataFrame(total_highest)
df_high.to_csv("data/highest_priority.csv",index=False,header=False)

df_high = pd.read_csv('data/highest_priority.csv')
df_high = df_high[df_high['mapID'] != 1000]
df_high.to_csv("data/highest_priority.csv",index=False)

df_low = pd.DataFrame(total_lowest)
df_low.to_csv("data/lowest_priority.csv",index=False,header=False)

df_low = pd.read_csv('data/lowest_priority.csv')
df_low = df_low[df_low['mapID'] != 1000]
df_low.to_csv("data/lowest_priority.csv",index=False)
