import nmap
from colored import fg, bg, attr

color = fg('green')
reset = attr('reset')

try:
	file1 = open('scanme-header.txt', 'r')
	print(' ')
	print (color + file1.read() + reset)
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
	print("Please Wait !\n")
	scanner.scan(target, '1-1000', '-v -sS')
	hostname = scanner[target].hostname()
	if (hostname == ""):
		print("Hostname:\tUnknown")
	else:
		print("Hostname:\t", hostname)
	print("State:\t ", scanner[target].state())
	print("Scan Info:\t ", scanner.scaninfo())
	print("Protocol(s):\t ", scanner[target].all_protocols())
	#print("Discovered Port(s):\t ", scanner[target]['tcp'].keys())
	for proto in scanner[target].all_protocols():
		lport = scanner[target][proto].keys()
		for port in lport:
			print('Port:\t ', port)
			print('State:\t ', scanner[target][proto][port]['state'])
		print("\n")



elif (response=='2'):
	print("NMAP Version:\t ", scanner.nmap_version())
	print("Scanning:\t ", target)
	print("Please Wait !\n")
	scanner.scan(target, '1-1000', '-v -sU')
	hostname = scanner[target].hostname()
	if (hostname == ""):
		print("Hostname:\tUnknown")
	else:
		print("Hostname:\t", hostname)
	print("State:\t ", scanner[target].state())
	print("Scan Info:\t ", scanner.scaninfo())
	print("Protocol(s):\t ", scanner[target].all_protocols())
	print("Discovered Port(s):\t ", scanner[target]['udp'].keys())
	for proto in scanner[target].all_protocols():
		lport = scanner[target][proto].keys()
		for port in lport:
			print('Port:\t ', port)
			print('State:\t ', scanner[target][proto][port]['state'])
		print("\n")



elif (response=='3'):
	print("NMAP Version:\t ", scanner.nmap_version())
	print("Scanning:\t ", target)
	print("Please Wait !\n")
	scanner.scan(target, '1-1000', '-T4 -A -v')
	hostname = scanner[target].hostname()
	if (hostname == ""):
		print("Hostname:\tUnknown")
	else:
		print("Hostname:\t", hostname)
	print("State:\t ", scanner[target].state())
	print("Scan Info:\t ", scanner.scaninfo())
	print("Protocol(s):\t ", scanner[target].all_protocols())
	#print("Discovered Port(s):\t ", scanner[target]['tcp'].keys())
	for proto in scanner[target].all_protocols():
		lport = scanner[target][proto].keys()
		for port in lport:
			print('Port:\t ', port)
			print('State:\t ', scanner[target][proto][port]['state'])
		print("\n")



else:
	print("Wrong Option!")
	exit(0)
