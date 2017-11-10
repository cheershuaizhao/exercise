'''
Created by Shuai 20171102
'''
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import timeit

def read_data(dirc):
    '''
    :param dirc: directory of the data
    :return: 
    '''
    mydata = []
    with open(dirc) as f:
        for line in f:
            line_list = line.strip().split(',')
            key = line_list[0].split()[0]
            mydata.append([key] + line_list[1:])
    return mydata


def return_maxplant(mydata, state = 'ca'):
    plantdict = defaultdict(lambda : 0)
    for i in range(len(mydata)):
        line = mydata[i]
        if state in line:
            plantdict[line[0]] += 1
    plantlst = sorted(plantdict.items(), key=lambda d: d[1])
    maxkey, maxvalue = plantlst[-1][0], plantlst[-1][1]
    return maxkey, maxvalue


def support_items(mydata, species = 'acalypha'):
    subdata = []
    for i in range(len(mydata)):
        if mydata[i][0] == species:
            subdata.append(mydata[i])
    return subdata

def find_init_fs(mydata, species = 'acalypha'):
    data = support_items(mydata, species= species)
    min_s = len(data) / 5
    freq_sets = set()
    for record in data:
        for item in record[1:]:
            freq_sets.add(item)
    dt = defaultdict(lambda : 0)
    for value in freq_sets:
        for record in data:
            if value in record:
                dt[value] += 1
    freq_sets = []
    for k, v in dt.items():
        if v > min_s:
            freq_sets.append(set([k]))
    dt_fs = {}
    for k,v in dt.items():
        if v > min_s:
            dt_fs[frozenset({k})] = v
    return freq_sets, data, dt_fs


def create_new_fs(old_fs, data, dt_fs, ar):
    dt_from = {}
    new_fs = []
    min_s = len(data) / 5
    dt = defaultdict(lambda: 0)
    k = len(old_fs[0])
    start = timeit.default_timer()
    for i in range(len(old_fs) - 1):
        for j in range(i + 1, len(old_fs)):
            new_item = deepcopy(old_fs[i])
            new_item.update(old_fs[j])
            if len(new_item) == k + 1 and new_item not in new_fs:
                new_fs.append(new_item)
                dt_from[frozenset(new_item)] = [frozenset(old_fs[i]), frozenset(old_fs[j])]

    for record in data:
        for value in new_fs:
            if value.issubset(set(record)):
                dt[frozenset(value)] += 1
    new_fs = []
    for k, v in dt.items():
        if v > min_s:
            new_fs.append(set(k))
            dt_fs[k] = dt[k]
    for k, v in dt.items():
        if v > min_s:
            for value in dt_from[k]:
                if dt_fs[k] / dt_fs[value] > 0.2:
                    ar.append([value, k, dt_fs[k], dt_fs[value], dt_fs[k] / dt_fs[value]])
    stop = timeit.default_timer()
    print(stop - start)

    return new_fs, dt_fs, ar


def find_max_pattern_and_ar(old_fs, data):
    old_fs, data, dt_fs = find_init_fs(data, species = 'acalypha')
    max_pattern = []
    ar = []
    while old_fs:
        new_fs, dt_fs, ar = create_new_fs(old_fs, data, dt_fs, ar)
        for value in new_fs:
            if len(value) > len(max_pattern):
                max_pattern = [value]
            if len(value) == len(max_pattern):
                max_pattern.append(value)
        old_fs = deepcopy(new_fs)
        print(new_fs)
    return max_pattern, ar




def find_ar(old_fs, data):
    new_fs = []
    min_s = len(data) / 5
    dt = defaultdict(lambda: 0)

if __name__ == "__main__":
  dirc = "C:\\Users\Shuai\\Downloads\\plants.data"
  data = read_data(dirc)
  maxkey, maxvalue = return_maxplant(data, 'ca')
  old_fs, data, dt_fs= find_init_fs(data, species= 'acalypha')
  new_fs, dt_fs, ar = create_new_fs(new_fs, data, dt_fs, [])

  max_pattern, ar = find_max_pattern_and_ar(old_fs, data)
