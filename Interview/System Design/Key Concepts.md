
### Consistent Hashing
保证当机器增加或者减少时，节点之间的数据迁移只限于两个节点之间，不会造成全局的网络问题
环形hash

### Partition
failover:
	1. detect
	2. elect new leader:consensus algo
	3. reconfigure

*split brain*

logical log: decoupled from the storage engine internals
write-ahead log:

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
* column-based: column data stored in separated files, when reading few columns, reading all columns from transactional-database can be too much. Column files can be compressed as bitmap, or run-length if it's sparse
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
* Eventual but not linear consistency

#### Pros
* speed, availabilities


#### Cons
* lack of consistency
* lack of ACID transactions
* lack of standard Structued Query Language interface

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

Atomic is for abort

multi-object transactions: difficult to implement. object here means table, file, mq, etc. Put data of a transaction into a single partition to speedup.

foreign key: avoid

dirty read/write, solved by :
1. locking before read/write/commit, not work well when there's a long-running write transaction
2. or 

#### Snapshot Isolation/read skew
transactions are allowed in repeatable reads(which can be combined as a single transaction)
solution: reads from a *consistent snpashot* of the database


isolation-levels
* read uncommitted: 
* read committed(default): 1.  读数据库时，只会读到已提交的数据。(无脏读), 写数据库时，只会覆盖已经提交的数据。(无脏写)
* repeatable read: 只能读到该事务启动时已经提交的其他事务修改的数据
	* con: phantom read: 由于只锁住旧数据，同一查询语句可能返回新数据
* serializability:
* snapshot isolation: 使用 mvcc 的无锁特性来提高性能，因为对一个 key 能够保存多个版本的数据，SI 能够做到读不阻塞写，甚至写也不阻塞写。
	* con: write skew

**multi-version concurrency control**：clock-based, 无锁实现，时间早的优先，只能读比当前🍜早的 transaction，

visibility rule: object not visible/deleted until finally commited

#### Read modify write/Lost Update
cause: two writes depends on the same old read data, and write accordingly
Solution: 
	1. atomic write, `update cnt set v = v + 1`
	2. locking, starvation
	3. Automatically detect lost updates, abort and retry
	4. CAS: compare(old value and latest value) and swap
		* not working for snapshots
	5. Conflict resolving: 
		* CRDT: writes in a replicated context, especially if thery are commulative/swappable

LWW could cause lost update

#### Write skew
read-update-write 

* optimistic locking: instead of blocking, transactions continues anyway, and database check when committing
	* contention low
* pessmisitic locking: wait until the situation is safe(no race condition)
	* contention high


* 2-phase locking/read-write lock: provides serializebility
all reads - all writes
* predicate lock: not perform well
* index range lock: allows database to lock access to all rows matching some query
