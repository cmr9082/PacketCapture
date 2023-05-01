def compute(packets) :

	echo_req_sent = []
	echo_req_revd = []
	echo_replies_sent = []
	echo_replies_revd = []

	for packet in packets:
		if packet[1] == 'ICMP':
			if '(ping) request' in packet[3]:
				if 'reply in' in packet[3]:
					echo_req_sent.append(packet)
				if 'request in' in packet[3]:
					echo_req_revd.append(packet)
			if '(ping) reply' in packet[3]:
				if 'reply in' in packet[3]:
					echo_replies_sent.append(packet)
				if 'request in' in packet[3]:
					echo_replies_revd.append(packet)

	#print(echo_req_sent)
	# print(echo_req_revd)
	# print(echo_replies_sent)
	#print(echo_replies_revd)

	#data size metrics
	num_echo_req_sent = len(echo_req_sent)
	num_echo_req_revd = len(echo_req_revd)
	num_echo_replies_sent = len(echo_replies_sent)
	num_echo_replies_revd = len(echo_replies_revd)

	total_echo_req_sent_bytes = sum(int(packet[5]) for packet in echo_req_sent)
	total_echo_req_revd_bytes = sum(int(packet[5]) for packet in echo_req_revd)

	total_echo_req_sent_data = total_echo_req_sent_bytes - (num_echo_req_sent * 42)
	total_echo_req_revd_data = total_echo_req_revd_bytes - (num_echo_req_revd * 42)

	#time based metrics
	avg_rtt = sum(int(echo_req_revd[i][1]) - int(echo_req_sent[i][1]) for i in range(len(echo_req_sent))) / len(echo_req_sent)

	echo_req_throughput = total_echo_req_sent_bytes / ((int(echo_req_sent[0][1]))-(int(echo_req_sent[-1][1])))

	echo_req_goodput = total_echo_req_revd_data / ((int(echo_req_sent[0][1]))-(int(echo_req_sent[-1][1])))

	avg_reply_delay = sum(int(echo_replies_revd[i][1]) - int(echo_req_revd[i][1]) for i in range(len(echo_req_revd))) / len(echo_req_revd)

	#distance metric
	avg_num_hops = sum(128 - int(packet[8]) for packet in echo_req_revd) / len(echo_req_revd)

	metrics = {
		"Echo Requents Sent": num_echo_req_sent,
		"Echo Requents Received": num_echo_req_revd,
		"Echo Replies Sent": num_echo_replies_sent,
		"Echo Replies Received": num_echo_replies_revd,
		"Echo Request Bytes Sent (bytes)": total_echo_req_sent_bytes,
		"Echo Request Data Sent (bytes)": total_echo_req_sent_data,
		"Echo Request Bytes Received (bytes)": total_echo_req_revd_bytes,
		"Echo Request Data Received (bytes)": total_echo_req_revd_data,
		"Average Ping Round Trip Time (RTT)": avg_rtt,
		"Echo Request Throughput (kB/sec)": echo_req_throughput,
		"Echo Request Goodput (kB/sec)": echo_req_goodput,
		"Average Reply Delay (microseconds)": avg_reply_delay,
		"Average Echo Request Hop Count": avg_num_hops
	}
	
	return metrics