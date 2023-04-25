
### RabbitMQ

### Cassandra
clustering: automatically scale, easy to set up, young
each node can be read/write, so one-node failure is avoid

用户在读写数据时可以指定要求成功写到多少个节点才算写入成功(设为W)，以及成功从多少个节点读取到了数据才算成功(设为R)

### kafka
at least one time delivery: apply sequence number to each message to avoid duplicates

### Dynamo
leaderless
### Database
#### MySQL
pro: software support

#### Redis
pro: has persistence & replication

### S3

### BloomFilter
If a element exists -> return true
If a element miss -> return true or false