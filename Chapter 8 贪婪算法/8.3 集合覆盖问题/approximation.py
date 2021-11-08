states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()  #存储最终选择的广播台



while states_needed:
    best_station = None #存储覆盖最多未覆盖州的广播台
    states_covered = set()  #包含广播台覆盖的所有未覆盖的州 #set()创建一个无序不重复的元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station # 计算交集用 &， 并集 |，差集 -
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)