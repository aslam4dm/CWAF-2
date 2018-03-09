import re
import string
from col import Colours as c

#GLOBAL
is_set = False
TARGET = []

# two options. uniform resource locator (URL) otherwise IPv4 address of a given site
# URL conditions: must contain a valid hostname, followed by period and web-extenstion
	# e.g. google.com or YAHOO.COM or bbc.co.uk
# IPv4: must contain 4 octets, after each one, there must be a period, except the last
	# e.g. 192.168.122.224
# if the first value is a letter, we assume it's a web hostname likewise if it begins with
# a digit we assume it's an ipv4 address
def read_domains():
	with open("domainList.txt", "r") as f:
		return f.readlines()

# current issue is that the input needs to be looped in case of incorrect user input

def set_target(**kwargs):
	# takes potential args: "file=" and "option=" 
	global TARGET
	global is_set
	is_set = False
	try:
		try:
			# reset previous options/targets otherwise just append to targets
			if kwargs["option"] == "new targets":
				TARGET = []
		except: pass
		if kwargs["file"]:
			motherLoad(kwargs["file"])
	except: pass
	while is_set == False:
		target = input("@set-target: ")
		if target == "":
			print("[!] Invalid input.")	
		elif "." not in target:
			print("[!] Problem with URL: {}".format(target))
		elif target[0] in string.ascii_letters:
			if ", " in target:	# the Syntax for applying multiple targets is: abc.com, xyz.org, ..., ...,
				set_mult_targets(target.lower())
			else:
				setting_hostname(target.lower())
	return TARGET

# issue [!] some input don't adhere to any kind of loop

def setting_hostname(ipt):
	# Works for a single target
	global TARGET
	global is_set # modification of is_set should stop the loop
	valid_list = []
	domain_lst = read_domains()
	for ex in domain_lst:
		valid_list.append(ex.lower().strip("\n"))
	#setting the extention list ^
	if "." not in ipt:
		print("[!] Problem with URL: {}".format(ipt))
	elif len(ipt.split(".")) == 2:
		if ipt.split(".")[1] in valid_list:
			TARGET.append(ipt) # satisfies criteria
			is_set = True
		else:
			print("[!] Problem with URL: {}".format(ipt))
	elif len(ipt.split(".")) == 3:
		if str(ipt.split(".")[1])+"."+ipt.split(".")[2] in valid_list:
			TARGET.append(ipt) # satisfies criteria
			is_set = True
		else:
			print("[!] Problem with URL: {}".format(ipt))
	elif len(ipt.split(".")) > 3:
		print("[!] Problem with URL: {}".format(ipt))
	else:
		print("[!] Problem with URL: {}".format(ipt))

def set_mult_targets(ipt):
	# Works for multiple targets provided they meet the Syntax criteria
	targets = ipt.split(", ")
	ult_list = []
	for t in targets:
		if setting_hostname(t) == None:
			pass
		else: 
			ult_list.append(setting_hostname(t))
	#TARGET = ult_list
	#return(TARGET)

def motherLoad(*args):
	ult_list = []
	for item in args[0].readlines():
		setting_hostname(item.strip("\n"))


# TESTS
"""
t= set_target()
print(t)

f = open("spider.txt", "r")
nt = set_target(file=f)
print(nt)

tv = set_target()
print(tv)

ntry = set_target(option="new targets")
print(ntry)

"""