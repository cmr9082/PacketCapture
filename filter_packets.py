def filter(filename,list,filtered) :
	infile = open(filename, 'r')
	line = infile.readline()
	isEcho = False
	packet = ""
	while line :
		if((line[0:3] != ('No.'))) :
			packet = packet + "\n"+ line
			if(line.find('Echo') >= 0) :
				isEcho = True
			line = infile.readline()
		elif((line[0:3] == ('No.'))):
			list.append(packet)
			if(isEcho) :
				filtered.append(packet)
			packet = ""
			packet = packet + "\n"+ line
			line = infile.readline()
#main
packets = []
filtered = []
filter('Node1.txt',packets,filtered)
print(packets[1])
print(filtered[2])