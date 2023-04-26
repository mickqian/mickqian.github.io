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

## Rate limiter