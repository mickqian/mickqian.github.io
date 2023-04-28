## Tiny url
The basic process can be:  

**Insert:**  

1.  Hash an input long url into a single integer;
2.  Locate a server on the ring and store the key--longUrl on the server;
3.  Compute the shorten url using base conversion (from 10-base to 62-base) and return it to the user.

**Retrieve:**  

1.  Convert the shorten url back to the key using base conversion (from 62-base to 10-base);
2.  Locate the server containing that key and return the longUrl.

## Load balancer

## Distributed lock

## TopK
top-k frequent items in a data stream

#### Naive solution
hashmap: store frequency of elements
heap: (cnt, elements) of top k

#### Improved of huge data
shard the data with hash, calculate top-k seperately

#### Lossy Counting
Like a Boyer-Moore, with hashmap

## Rate limiter


## News Feed

Read much more than write

Discussed in different conditions:

#### Pull: read only when needed
high fan out: many followers
k-way merge, to get top-100
Cons: If a user subscribed many (N), N read can be rather slow
solution? add cache

#### Push: write
low fan out: few followers
“Disk is cheap”，不要怕浪费数据库存储，为了加速查询，多存一些东西是没关系的。

Cons: if a user has many subscribers, can be slow


Pull method is populer