
## Consistent Hashing
保证当机器增加或者减少时，节点之间的数据迁移只限于两个节点之间，不会造成全局的网络问题
环形hash


### Linear Consistency 线性一致性
aka atomic consistency/strong consistency/immediate consistency/external consistency
#### Basic idea
让一个系统看起来好像只有**一个**数据副本，且所有操作均为原子性


### Eventual Consistency

常用实现手段：
* 读修复： 消除副本数据不一致问题
* 写修复: primary 的写操作直到 follower 的写成功后才完成
* async repair：running data consistency checks


### Leaderless 无主
peer-to-peer
dynamo, riak, cassandra, voldemort
easy to write

#### Quorum 法定人数
w + r > n， 才能保证至少有一个副本是最新的


### Idempotency


### Sharding
#### vs replication
solve the problem of cost(CPU, network bandwidth, disk IO, etc)

#### problems
* **Rebalancing**:  if a particular data blows the storage capacity for the shard
* Reports require running same query on all shards


### Denormalize
techniques used to accelerate some specific querys/performance, including:
1. insert redundent key, according to specific query
2. insert derived key, as precalcualation or cache result
3. re-organize tables: if the result of merging two tables is required
4. split tables: Massive table or cold columns, to accelerate or decrese table size


### Not Only SQL
types:
* kv
* column
* document-based
* graph


#### features
partitions based on hash

#### pros
* scale easily 
* write fast



#### cons
* query only on primary key
* consistency



* Not tabular relations
* More flexible
* Compromise consitency, in favor of availability and speed

### Graph Database
SQL Server
highly-related
pro:
1. fast relation-query operation


### Cache
write-through: strong consistency
