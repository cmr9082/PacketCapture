import sys

def parse():
    metrics = []
    with open(sys.argv[1], 'r') as doc:
        for line in doc:
                newline = doc.readline().strip()
                parts = newline.split()
                if len(parts) >= 8 and parts[4] == "ICMP":
                    time = parts[1]
                    protocol = parts[4]
                    length = parts[5]
                    info = ' '.join(parts[7:])
                    metrics.append((time, protocol, length, info))
    return metrics

results = parse()
print(results)

for metrics in results:
    print('Time:', metrics[0])
    print('Protocol:', metrics[1])
    print('Length:', metrics[2])
    print('Info:', metrics[3])
    print()