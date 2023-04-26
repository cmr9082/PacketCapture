def listPackets(filename,list) :
	infile = open(filename, 'r')
	line = infile.readline()
	packet = line
	line = infile.readline()
	while line :
		while (line[0:3] != ('No.')) :
			packet = packet + "\n"+ line
			line = infile.readline()
			print(packet)
		list.append(packet)
		#end of packet
		packet = ""
		line = infile.readline()
	print(list[0])
def getCheck(filename,data) :
	infile = open(filename, 'r')
	line = infile.readline()
	while line:
		line = infile.readline()
		if (line[0:3] == ('No.')) :
			line = infile.readline()
			#get index at beginning of the line
			if(line.find('Echo') >= 0) :
				temp=line.lstrip()
				check = temp[0:temp.index(' ')]
				data.append(check)
	infile.close()
#main
packets = []
checklist = []
#getCheck('Node1.txt', checklist)
listPackets('Node1.txt',packets)

