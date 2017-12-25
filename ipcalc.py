r_input = "192.168.1.1/24"
IP = r_input
IP = IP.split("/")


def ip_split(ipaddr):
  ip = ipaddr.split(".")
  ipl = []
  for i in ip:
    if int(i) < 256:
      ipl.append(int(i))
    else:
      return ("You entered wrong subnet mask. Check your input and try again")
  return ipl

source_ip = ip_split(IP[0])

def ip2bin(ipaddr):
  binIp = []
  for i in ipaddr:
    integ = int(i)
    binary = bin(integ)
    binIp.append(binary)
  return binIp

def mask_validator(mask):
  m = int(mask)
  if m < 33:
    return m
  else:
    return ("You entered wrong subnet mask. Check your input and try again")

mask = mask_validator(IP[1])

def mask2bin(mask):
  mask = int(mask)
  bin_mask = bin(mask)
  return bin_mask

def networkCalc(ipaddr):
  #not finished yet
  birIp = 1


print (source_ip)
print (ip2bin(source_ip))
print (mask)
print (mask2bin(mask))
