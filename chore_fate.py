import random
from pprint import pprint
import pandas as pd

with open('chore_list.txt') as f:
    chores = f.read().split('------')

    daily, weekly, monthly, annually = chores[2].strip().split('\n'), \
                                       chores[4].strip().split('\n'), \
                                       chores[6].strip().split('\n'), \
                                       chores[8].strip().split('\n')
                                       
    len_daily, len_weekly, len_monthly, len_annually = len(daily), len(weekly), len(monthly), len(annually)

    # daily
    Alan = []
    Jessica = []
    # print(daily)

    for i in range(len_daily//2):
        Alan.append(daily[random.randint(0, len_daily-1)])
    
    for i in daily:
        if i not in Alan:
            Jessica.append(i)


    print('Alan Daily:', Alan)
    print('Jessica daily:', Jessica) 