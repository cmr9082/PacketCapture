def compute() :
	print('called compute function in compute_metrics.py')

	#node1

	#data size metrics

	#number of echo requests sent
	#count number of echo requests sent by node

	#number of echo requests received
	#count number of echo requests received by node

	#number of echo replies sent
	#count number of echo replies sent by node

	#number of echo replies receieved
	#count number of echo replies receieved by node	

	#total echo request bytes sent
	#sum the size of all echo requests sent by node in bytes

	#total echo request bytes received
	#sum the size of all echo requests received by node in bytes

	#total echo request data sent
	#sum the size of the payload of all echo requests sent by node in bytes

	#total echo request data received
	#sum the size of the payload of all echo requests received by node in bytes

	#time based metrics

	#average ping round trip time (RTT)
	#calculate time difference between sending echo request and the receiving, average for all for the node

	#echo request throughput
	#calculate the sum of the frame sizes of all echo requests sent by node, divide by sum of all ping RTT, convert to kB/sec

	#echo request goodput
	#calculate the sum of payload for all echo requests sent by node, divide by sum by ping RTT, convert to kB/sec

	#avgerage reply delay
	#calculate the time difference echo request and sending reply, average reply delay times, convert to microseconds


	#distance metric

	#average number hops per echo request
	#subtract TTL in echo request from TTL in echo reply to get number of hops, average with all echo requests sent by node