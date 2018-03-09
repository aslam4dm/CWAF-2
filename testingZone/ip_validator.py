import string

"""
12.12.12.12
12.122.12.12
12.12.122.12
12.12.12.122
122.12.12.12
122.122.12.12
122.122.122.12
122.122.122.122
"""

def invalid_ip():
	print("[!] invalid Addr")

def IPv4_validator():
	setter = False
	while setter != True:
		usr_inpt = input("@set-IPv4: ")
		is_greater = False
		# check to ensure all octets are less than length of 4
		for octet in usr_inpt.split("."):
			if len(octet) > 3:
				is_greater = True
				break
		if is_greater == True:
			invalid_ip()
			continue
		if usr_inpt[0] in string.digits:
			if not "." in usr_inpt:
				invalid_ip()
			elif ".." in usr_inpt or "..." in usr_inpt:
				invalid_ip()
			else:
				if usr_inpt.count(".") != 3:
					invalid_ip()
					continue
				if usr_inpt[0] == "." or usr_inpt[1] == ".":
					invalid_ip()
				elif usr_inpt[2] == ".":	# at this stage can only go upto 10
					if usr_inpt[4] == "." or usr_inpt[5] == "." or usr_inpt[6] == ".":
						if usr_inpt[6] == "." or usr_inpt[7] == "." or usr_inpt[8] == "." or usr_inpt[9] == "." or usr_inpt[10] == ".":
							setter = True
							return(usr_inpt)
						else: print("invalid point (octet 3)")
					else: print("invalid point (octet 2)")
				elif usr_inpt[3] == ".":
					if usr_inpt[5] == "." or usr_inpt[6] == "." or usr_inpt[7] == ".":
						if usr_inpt[7] == "." or usr_inpt[8] == "." or  usr_inpt[9] == "." or usr_inpt[10] or usr_inpt[11] == ".":
							setter = True
							return(usr_inpt)
						else: invalid_ip()
					else: invalid_ip()
				else:
					invalid()
		else:
			invalid()

def invalid_url(*args):
	if args:
		print("[!] invalid URL: {}".format(args[0]))
	else:
		print("[!] invalid URL")

def read_domains():
	valid_list = []
	with open("domainList.txt", "r") as f:
		for ex in f.readlines():
			valid_list.append(ex.lower().strip("\n"))
	return valid_list

def URL_validator():
	# set valid_extensions
	valid_extensions = read_domains()
	setter = False
	while setter != True:
		usr_inpt = input("@set-URL: ")
		if "." not in usr_inpt:
			invalid_url()
			continue
		if ", " in usr_inpt:
			targets = usr_inpt.split(", ")
			print(targets)
			for t in targets:
				if "." not in t:
					invalid_url(t)
					continue
				if t.split(".")[2] not in valid_extensions:
					invalid_url(t)
					continue
				else:
					print(t.split(".")[2])
URL_validator()

