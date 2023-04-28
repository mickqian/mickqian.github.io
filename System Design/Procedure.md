1. Clarify the system's constraints and to identify what use cases the system needs to satisfy
	question can be made on:
	* the number of users
	* the amount of data the sytem should work with
	* the traffic the system should handle, request/month
2. Draw a diagram on abstract design
	application **service** layer
	data **storage** layer
3. Scalabilities
	Think about bottlenecks:
	* huge (user) request: load balancer
	* huge data: distribution
	* latency: caching
	* single point failure ?
	* fault tolerance
	Address by Scale:
	 
	It's all about trade-off