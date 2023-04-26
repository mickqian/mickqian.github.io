## Database

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

#### Redis
pro: has persistence & replication


### Cassandra
clustering: automatically scale, easy to set up, young
each node can be read/write, so one-node failure is avoid

用户在读写数据时可以指定要求成功写到多少个节点才算写入成功(设为W)，以及成功从多少个节点读取到了数据才算成功(设为R)





## Message Queue

### RabbitMQ


### kafka
at least one time delivery: apply sequence number to each message to avoid duplicates

### S3

### BloomFilter
If a element exists -> return true
If a element miss -> return true or false

## Cache

### Redis

### Memcache