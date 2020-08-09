import nmap

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

try:
	file1 = open('scanme.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('\nBanner File not found!')


scanner = nmap.PortScanner()

target = input("Enter IP Address to scan: ")
type(target)

response = input("\nEnter the type of scan you want to run: \n\n1)TCP Scan \n2)UDP Scan \n3)Intense Scan \n\n")
print("\n")

if (response=='1'):
	print("NMAP Version:\t ", scanner.nmap_version())
	print("Scanning:\t ",target)
	scanner.scan(target, '1-1000', '-v -sS')
	print("Hostname:\t ", scanner[target].hostname())
	print("State:\t ", scanner[target].state())
	print("Scan Info:\t ", scanner.scaninfo())
	print("Protocol(s):\t ", scanner[target].all_protocols())
	#print("Discovered Port(s):\t ", scanner[target]['tcp'].keys())
	for proto in scanner[target].all_protocols():
		lport = scanner[target][proto].keys()
		for port in lport:
			print('Port:\t ', port)
			print('State:\t ', scanner[target][proto][port]['state'])


elif (response=='2'):
	print("NMAP Version:\t ", scanner.nmap_version())
	print("Scanning:\t ", target)
	scanner.scan(target, '1-1000', '-v -sU')
	print("Hostname:\t ", scanner[target].hostname())
	print("State:\t ", scanner[target].state())
	print("Scan Info:\t ", scanner.scaninfo())
	print("Protocol(s):\t ", scanner[target].all_protocols())
	print("Discovered Port(s):\t ", scanner[target]['udp'].keys())
	for proto in scanner[target].all_protocols():
		lport = scanner[target][proto].keys()
		for port in lport:
			print('Port:\t ', port)
			print('State:\t ', scanner[target][proto][port]['state'])



elif (response=='3'):
	print("NMAP Version:\t ", scanner.nmap_version())
	print("Scanning:\t ", target)
	scanner.scan(target, '1-1000', '-T4 -A -v')
	print("Hostname:\t ", scanner[target].hostname())
	print("State:\t ", scanner[target].state())
	print("Scan Info:\t ", scanner.scaninfo())
	print("Protocol(s):\t ", scanner[target].all_protocols())
	#print("Discovered Port(s):\t ", scanner[target]['tcp'].keys())
	for proto in scanner[target].all_protocols():
		lport = scanner[target][proto].keys()
		for port in lport:
			print('Port:\t ', port)
			print('State:\t ', scanner[target][proto][port]['state'])



else:
	print("Wrong Option!")
	exit(0)
