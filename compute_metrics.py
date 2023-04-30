def compute(packets) :
	echo_req_sent = []
	echo_req_revd = []
	echo_replies_sent = []
	echo_replies_revd = []

	for packet in packets:
		if packet[1] == 'ICMP':
			if 'Echo (ping) request' in packet[3]:
				if packet[2] == 'request':
					echo_req_sent.append(packet)
				elif packet[2] == 'reply':
					echo_req_revd.append(packet)
			if 'Echo (ping) reply' in packet[3]:
				if packet[2] == 'request':
					echo_replies_sent.append(packet)
				elif packet[2] == 'reply':
					echo_replies_revd.append(packet)

	#data size metrics

	#number of echo requests sent
	#len(echo_req_revd)

	#number of echo replies sent
	#len(echo_replies_sent)

	#number of echo replies receieved
	#len(echo_replies_revd)

	#total echo request bytes sent
	#echo_req_sent length sum

	#total echo request bytes received
	#echo_req_revd length sum

	#total echo request data sent
	#(echo_req_sent length sum) - (len of echo_req_sent *42)

	#total echo request data received
	#(echo_req_revd length sum) - (len of echo_req_revd *42)

	#time based metrics

	#average ping round trip time (RTT)
	#echo_req_sent time - echo_req_revd time / len(echo_req_sent)

	#echo request throughput
	#echo_req_sent length sum / (echo_req_sent time - echo_req_revd time / len(echo_req_sent))

	#echo request goodput
	#(echo_req_revd length sum) - (len of echo_req_revd *42)) / (echo_req_sent time - echo_req_revd time / len(echo_req_sent))

	#average reply delay
	#(echo_req_revd time - echo_repies_sent) / len(echo_req_revd)

	#distance metric

	#average number hops per echo request
	#echo_req_revd - echo_repies_sent /len(echo_req_sent)