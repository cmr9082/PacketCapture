from filter_packets import *
from packet_parser import *
from compute_metrics import *

f1 =open('Node1_filtered.txt','w')
filtered1 = []
filter('Node1.txt',filtered1)
for instance in filtered1:
    f1.write(instance)
f1.close()

f2 =open('Node2_filtered.txt','w')
filtered2 = []
filter('Node2.txt',filtered2)
for instance in filtered2:
    f2.write(instance)
f2.close()

f3 =open('Node3_filtered.txt','w')
filtered3 = []
filter('Node3.txt',filtered3)
for instance in filtered3:
    f3.write(instance)
f3.close()

f4 =open('Node4_filtered.txt','w')
filtered4 = []
filter('Node4.txt',filtered4)
for instance in filtered4:
    f4.write(instance)
f4.close()

results1 = parse('Node1_filtered.txt')

Node1Ip = "192.168.100.1"
Node2Ip = "192.168.100.2"
Node3Ip = "192.168.200.1"
Node4Ip = "192.168.200.2"

resultsies1 = compute(results1, Node1Ip)

# results2 = parse('Node2_filtered.txt')
# results3 = parse('Node3_filtered.txt')
# results4 = parse('Node4_filtered.txt')

