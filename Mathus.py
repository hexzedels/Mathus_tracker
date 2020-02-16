import pandas as pd
import numpy as np
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

pd.options.mode.chained_assignment = None
data = pd.read_csv('~/data1.csv')
theme_completer = WordCompleter(np.load('Titles.npy'))
inp = prompt('Enter theme: ', completer=theme_completer)
work_frame = data[data['Title'] == inp]
indx = work_frame.index[0]
print('Total amount of problems: ',data['Total'][indx])
def fix_problems(frame): #Some crazy fix
    app =frame['Solved'][indx][1:-1].split(" ")
    temp = []
    for ap in app:
        temp.append(int(ap))
    return temp
def add(problems):
    problems = problems.split(',')
    problems = [int(x)-1 for x in problems]
    for problem in problems:
        temp[problem] = 1
    data['Solved'][indx] = np.array(temp)
    return temp 
temp = fix_problems(work_frame)
print('Currently solved: ',sum(1 for i in temp if i  == 1))
print(temp)
add(input("Enter problems separated by comma: "))
data.to_csv('data1.csv',index=False)
