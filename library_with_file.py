"""For this file I assume that I have created a file in the current folder containing the entries of the census.
Following I need to check them , so I can crete a file containing the missing ones"""



d = []
with open('data', 'r', encoding = 'utf-8') as f:
    for line in f:
        d.append(int(line.strip()))

        
to_file =''
for i in range(1,max(d)):
    if i not in d:
        to_file+=str(i) +'\n'

with open('results.txt', 'w', encoding = 'utf-8') as f:
    f.write(to_file)
