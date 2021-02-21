# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 08:05:47 2020

@author: Shivadhar SIngh
"""

import matplotlib.pyplot as plt
import numpy as np

import csv
with open("daily-min-temp-CBR.csv") as csvfile:
    reader = csv.reader(csvfile)
    min_table = [ [int(row[2]), int(row[3]), int(row[4]),\
                   row[5], row[7]] for row in reader if ((row[3]) == '06' or\
                     (row[3]) == '07' or (row[3]) == '08')]
    csvfile.close()
with open("daily-max-temp-CBR.csv") as newfile:
    readin = csv.reader(newfile)
    max_table = [[int(row[2]), int(row[3]), int(row[4]),\
                   row[5], row[7]] for row in readin if ((row[3]) == '06' or\
                     (row[3]) == '07' or (row[3]) == '08')]
    newfile.close()
#temp = [float(row[3]) for row in min_table if row[3] != ""]     
#print(min_table)
#print(max_table)

def count_subzero_nights(year):
    count = 0
    for row in min_table:
        if row[3] != "" and row[0] == year:
            if float(row[3]) < 0:
                count += 1
    return count

def avg_min_temp(month, year):
    sum_temp = 0
    for row in min_table:
        if row[3] != "" and row[1] == month and row[0] == year:
            sum_temp += float(row[3])
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8\
        or month == 10 or month == 12:
            days = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
        elif row[0] % 4 == 0:
            days = 29
        else: days = 28
    avg = sum_temp/days
    return avg

xs = [i for i in range(2008,2020)]
ys = []
for i in range(2008, 2020):
    ys.append(count_subzero_nights(i))
plt.plot(xs, ys, linestyle="solid")
plt.show()

N = 12
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = []
zvals = []
kvals = []
for year in range(2008, 2020):
    yvals.append(avg_min_temp(6, year))
    zvals.append(avg_min_temp(7, year))
    kvals.append(avg_min_temp(8, year))

rects1 = ax.bar(ind, yvals, width, color='r')

rects2 = ax.bar(ind+width, zvals, width, color='g')

rects3 = ax.bar(ind+width*2, kvals, width, color='b')

ax.set_ylabel('Avg. Temperatue')
ax.set_xlabel('Years')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('2008', '2009', '2010', '2011', '2012', '2013', '2014',\
                     '2015', '2016', '2017', '2018', '2019') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('June', 'July', 'August') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        if h < 0:
            space = 1.1*h
        else:
            space = 1.05*h
        ax.text(rect.get_x()+rect.get_width()/2., space, '%.1f'%float(h),
                ha='center', va='bottom').set_rotation(90)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()



