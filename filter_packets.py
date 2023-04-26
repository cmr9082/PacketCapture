def listPackets(filename,list) :
	infile = open(filename, 'r')
	line = infile.readline()
	while line:
		#find a way to identify one packet
		packet = 'needs to be assigned'
		#Store packet in List
		list.append(packet)
	infile.close()
def getCheck(filename) :
	infile = open(filename, 'r')
	line = infile.readline()
	while line:
		line = infile.readline()
		if (line[0] == ('N')) :
			line = infile.readline()
			print(line)
			#get index at beginning of the line


	infile.close()
#main
packets = []
getCheck('Node1.txt')
listPackets('Node1.txt',packets)

