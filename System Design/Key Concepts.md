
## Consistent Hashing
保证当机器增加或者减少时，节点之间的数据迁移只限于两个节点之间，不会造成全局的网络问题
环形hash


### Consistency 一致性

强度从高到低：
1. strong consistency
2. linear consistency/read-after-write    write-write consistency
3. 单调读一致性 前缀一致性 
4. Casual consistency
5. eventual consistency

#### Linear Consistency
aka atomic consistency/strong consistency/immediate consistency/external consistency
#### Basic idea
让一个系统看起来好像只有**一个**数据副本，且所有操作均为原子性


#### Eventual Consistency

常用实现手段：
* 读修复：从replicas中读，将缺失变更发送给相应replica, 消除副本数据不一致问题
* 写修复:  primary 的写操作直到 follower 的写成功后才完成
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
* document-based: json, Dynamo
* graph: Neo4j, complex relations

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
#### Write/read-through
update cache & database
由缓存作为数据库的代理，和数据库进行交互
**strong consistency**
##### Read through
check cache
* hit: return
* miss: load from database, return
##### Write through
check cache
* hit: update cached value, sync update database
* miss: update database

##### Write invalidate
update database, invalidate cache

#### Write back/Write behind
update cache only, **async** update database
used in write-heavy scenarios


### Transaction
group read/writes into a logical unit, to avoid worrying about partial failure

multi-object transactions: difficult to implement. object here means table, file, mq, etc. Put data of a transaction into a single partition to speedup.

foreign key: avoid

dirty read/write, solved by :
1. locking before read/write/commit, not work well when there's a long-running write transaction
2. or 

#### Snapshot Isolation/read skew
transactions are allowed in repeatable reads(which can be combined as a single transaction)
solution: reads from a *consistent snpashot* of the database


isolation
read-committed: 

concurrency control
isolation-level

multi-version concurrency control：无锁实现，时间早的优先，只能读比当前🍜早的 transaction，

visibility rule: object not visible/deleted until finally commited


#### Read modify write/Lost Update
cause: two writes depends on the same old read data, and write accordingly
Solution: 
	1. atomic write， `update cnt set v = v + 1`
	2. Automatically detect lost updates, abort and retry
	3. CAS: compare(old value and latest value) and swap
	4. CRDT: writes in a replicated context, especially if thery are commulative/swappable

LWW could cause lost update