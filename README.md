## Episode数据同步
Episode数据同步包括三种方式，首先都需要导出全量数据
Detail on [Wiki Design](http://wiki.qiyi.domain/pages/viewpage.action?pageId=27034214)

### 全量导出
- 对Qipu Hbase的两张表进行全表扫描，导出全量数据到Redis
  sh qipu_episode_sync.sh sh|jy init

- Redis是Cluster模式使用redisloader.py，第一个参数为路径，支持模糊匹配

  第二个参数为集群简称 jy_cluster

### 导入Redis
- 一次性行为
  sh qipu_episode_sync.sh sh|jy update

### 增量更新
- 记录导出数据时间，并将读取导出的数据，更新redis中的数据

### 爬虫
- spider中两种方法
