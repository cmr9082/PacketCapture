def listPackets(filename,list) :
	infile = open(filename, 'r')
	line = infile.readline()
	packet = ""
	while line :
		if((line[0:3] != ('No.'))) :
			packet = packet + "\n"+ line
			line = infile.readline()
		elif((line[0:3] == ('No.'))):
			list.append(packet)
			packet = ""
			packet = packet + "\n"+ line
			line = infile.readline()
	return list

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
getCheck('Node1.txt', checklist)
listPackets('Node1.txt',packets)

print(packets[1])