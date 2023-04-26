import sys

def parse() :
	print('called parse function in packet_parser.py')
	metricz = []
	with open(sys.argv[1], 'r') as doc:
		for line in doc:
			if not line.strip():	
				newline = doc.readline().strip()
				newline.split(" ")
				if newline[4] == "ICMP":
					print(newline[4])
				else:
					continue

parse()