import csv
from collections import defaultdict

data = open('mozilla.csv')
data_reader = csv.reader(data)

labels = next(data_reader)

data_viz1_excitment = defaultdict(list)
data_viz1_fear = defaultdict(list)

for row in data_reader:
    data_viz1_excitment[row[7]].append(row[20])
    data_viz1_fear[row[7]].append(row[19])


viz1_fear_counts = {}
for key, vals in data_viz1_fear.items():
    temp = defaultdict(int)
    for val in vals:
        temp[val] += 1
    viz1_fear_counts[key] = temp

viz1_excitment_counts = {}
for key, vals in data_viz1_excitment.items():
    temp = defaultdict(int)
    for val in vals:
        temp[val] += 1
        viz1_excitment_counts[key] = temp


headers = ['Ultra Nerd:  I build my own computers, run my own servers, code my own apps. I‰Ûªm basically Mr. Robot.','Technically Savvy:   I know my way around a computer pretty well. When anyone in my family needs technical help, I‰Ûªm the one they call.','Average User:   I know enough to get by.', 'Luddite:  Technology scares me! I only use it when I have to.']

file = open('viz1_excitment.csv', 'w')
file.write('Skill Level, None of the above, It will be fun, It will bring the world together, It will make life easier, We will be smarter and better educated, Other (please specify)\n')

for key in headers:
    updated_key= key.split(':')[0]  #grab only the words before the colon
    line = viz1_excitment_counts[key]
    row = updated_key+', '  #setting up the csv row to print
    row += str(line['None of the above'])+', '
    row += str(line['How much fun it will be'])+', '
    row += str(line['How it will bring the world together'])+', '
    row += str(line['How easy it will make life'])+', '
    row += str(line['How it will make us all smarter and better educated'])+', '
    row += str(line['Other (please specify)'])+'\n'
    file.write(row)
file.close()

file = open('viz1_fear.csv', 'w')
file.write('Skill Level, Scared as hell, Cautiously optimistic, A little wary, On the fence, Super excited \n')
for key in headers:
    updated_key= key.split(':')[0]  #grab only the words before the colon
    line = viz1_fear_counts[key]
    row = updated_key+', '  #setting up the csv row to print
    row += str(line['Scared as hell. The future where everything is connected has me scared senseless. We‰Ûªre all doomed!'])+', '
    row += str(line['Cautiously optimistic. I‰Ûªm hopeful we‰Ûªre building a better world by becoming more connected in everything we do.'])+', '
    row += str(line['A little wary. All this being connected to the internet in every part of our lives makes me a little nervous. What‰Ûªs going to happen to our privacy?'])+', '
    row += str(line['On the fence.  I‰Ûªm not sure about all this. I think I‰Ûªll wait and see.'])+', '
    row += str(line['Super excited! I can‰Ûªt wait for everything to be connected. My life will be so much better.'])+'\n'
    file.write(row)
file.close()





