import numpy as np
import pandas as pd

# Load data
dat = pd.read_csv("mozilla.csv", low_memory=False)

d = dat['Language']
null_idx = d.isnull()
val_idx = np.invert(null_idx.as_matrix())
dat = dat.iloc[val_idx]

countryList = dat['Country'].unique()
languageList = dat['Language'].unique()

explain_list = ['Explain: IoT', 'Explain: Connected Devices', 'Explain: Botnet', 'Explain: Blockchain',
                'Explain: RFID', 'Explain: DDOS', 'Explain: Zero Day', 'Explain: VPN', 
                'Explain: TOR', 'Explain: None']

'''
for language in languageList:
	ind_language = (dat['Language'] == language)

	print language + ': ' + str(sum(ind_language))

'''

fid = open('viz3.csv', 'w')
fid.write('Language,Total,')
for header in explain_list:
	fid.write(header)

	if header == explain_list[-1]:
		fid.write('\n')
	else:
		fid.write(',')

for language in languageList:
	fid.write(language + ',')
	ind_language = (dat['Language'] == language)

	fid.write(str(sum(ind_language)) + ',')

	for item in explain_list:
		dat2 = dat[item][ind_language]

		count = sum(dat2.isnull())

		fid.write(str(count))

		if item == explain_list[-1]:
			fid.write('\n')
		else:
			fid.write(',')

fid.close()