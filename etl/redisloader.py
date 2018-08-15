# -*- coding:utf-8 -*-
import csv
import glob
import multiprocessing
import sys

import datetime
from rediscluster import StrictRedisCluster

REDIS_CONFIG = {
    'jy_cluster': {
        'host': 'localhost',
        'port': 6379
    }
}


def load(cluster, datapaths):
    print datapaths, "process start"
    rc = StrictRedisCluster(startup_nodes=[REDIS_CONFIG.get(cluster)], decode_responses=True)
    with open(datapaths, 'rb') as csv_file:
        data_reader = csv.reader(csv_file, delimiter="\t")
        for row in data_reader:
            rc.hmset(row[0],
                     {
                         'a': row[1],
                         'c': row[2],
                         'd': row[3]
                     })
    print datapaths, "process end"


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    data_file_pattern = sys.argv[1]
    cluster = sys.argv[2]
    if cluster != 'jy_cluster':
        print "error : cluster must be jy_cluster"
        sys.exit()

    data_file_paths = glob.glob(data_file_pattern)
    processes = []
    for path in data_file_paths:
        p = multiprocessing.Process(target=load, args=(cluster, path))
        processes.append(p)
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print('all done')
    endtime = datetime.datetime.now()
    times = (endtime - starttime).seconds
    print "运行时间为", times, "秒"
