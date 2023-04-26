## Database

#### pros
* topic: distribute to different workers
#### cons

### Dynamo
leaderless, de-centralization
always writeable
#### Variant consistent hashing
instead of mapping a node to a single point in the circle, each node gets assigned to multiple points in the ring. Reduces uniform-data-distribution
#### Preference list
The list of nodes that is responsible for storing a particular key is called the preference list
#### Hinted handoff
temporarily stores the key in other nodes. When node recovered, deliver the data back the delete the temporary replica

#### Anti entropy(replica synchronization)
Merkle Tree: parent node stores the hash of children
Each node contains merkle tree of key range it stores
To do this, we need to quickly compare two copies of a range of data residing on different replicas and figure out exactly which parts are different.


![[Pasted image 20230426192152.png]]



#### MySQL
pro: software support

### Redis
#### pros
has persistence & replication


### Cassandra
clustering: automatically scale, easy to set up, young
each node can be read/write, so one-node failure is avoid
tunable consistency: 用户在读写数据时可以指定要求成功写到多少个节点才算写入成功(设为W)，以及成功从多少个节点读取到了数据才算成功(设为R)





## Message Queue

### RabbitMQ


### Kafka
at least one time delivery: apply sequence number to each message to avoid duplicates
pub/sub
NIO allows for fast transfer of data in and out of the system
zero-copy: nio

#### Brokers
* receive messages from producers, deliver messages to consumer
* **persist** messages for some time
* **lightweight**

Log-based queue: append-only, producers and consumer
#### Topic
queues, logical collections of partitions
topics are replicated
broker is the **leader** of a partition
writes are written to N replicas
![[Pasted image 20230426214037.png]]
producers balance load to brokers
#### Cons
* not designed for large payloads
* rebalancing problem:  if you're doing any aggregation in the consumer by the partition ke
* number of partitions cannot be easily changed
* lots of topics can hurt IO

### BloomFilter
If a element exists -> return true
If a element miss -> return true or false

## Cache

### Redis
in-mem key/value 
various types
eventually persistent
pub/sub
async
master-slave
atomic operations
### Memcached
key/value
