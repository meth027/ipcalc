r_input = "192.168.1.1/20"
IP = r_input
IP = IP.split("/")


def ip_split(ipaddr):
  ip = ipaddr.split(".")
  ipl = []
  for i in ip:
    if int(i) < 256:
      ipl.append(int(i))
    else:
      return ("You entered wrong ip address. Check your input and try again")
  return ipl

source_ip = ip_split(IP[0])

def ip2bin(ipaddr):
  binIp = []
  for i in ipaddr:
    integ = int(i)
    binary = bin(integ)
    binIp.append(binary.replace("0b",""))
  binIpNew = [str(binIp[0]).rjust(8,"0"),str(binIp[1]).rjust(8,"0"),str(binIp[2]).rjust(8,"0"),str(binIp[3]).rjust(8,"0")]
  return binIpNew

binIpAddr = ip2bin(source_ip)

def mask_validator(mask):
  m = int(mask)
  if m < 33:
    return m
  else:
    return ("You entered wrong subnet mask. Check your input and try again")

mask = mask_validator(IP[1])

def mask2bin(mask):
  bin_mask = int(mask)*"1"
  bitmask = bin_mask.ljust(32,"0")
  bitmask = [bitmask[0:8],bitmask[8:16],bitmask[16:24],bitmask[24:32]]
  return bitmask

binMask = mask2bin(mask)

def mask255(binaryMask):
  a = binaryMask
  mask = [int(a[0],2),int(a[1],2),int(a[2],2),int(a[3],2)]
  return mask

def wildcard_maker(binaryMask):
  a = binaryMask
  mask = [255 - int(a[0],2),255 - int(a[1],2),255 - int(a[2],2),255 - int(a[3],2)]
  return mask

decMask = mask255(binMask)
wildMask = wildcard_maker(binMask)
wildMaskBin = ip2bin(wildMask)


def networkCalc(binaryIP,binaryMask):
  a = binaryIP
  b = binaryMask
  network = [int(a[0],2) & int(b[0],2),int(a[1],2) & int(b[1],2),int(a[2],2) & int(b[2],2),int(a[3],2) & int(b[3],2)]
  return network

ntCalc = networkCalc(binIpAddr,binMask)

def broadcast_counter(ntCalc,wildMask):
  a = ntCalc
  b = wildMask
  counter = [a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3]]
  return counter

broadcast = broadcast_counter(ntCalc,wildMask)

def maxhost_counter(broadcast):
  a = broadcast
  max_host = [a[0],a[1],a[2],(a[3]-1)]
  return max_host

max_host = maxhost_counter(broadcast)

def minhost_counter(network):
  a = network
  min_host = [a[0],a[1],a[2],(a[3]+1)]
  return min_host

min_host = minhost_counter(ntCalc)

def total_hosts(mask):
  a = mask
  total = 2 ** (32-a)
  return total

hosts = total_hosts(mask)

print (source_ip)
print (binIpAddr)
print (mask)
print (binMask)
print (ntCalc)
print (decMask)
print (wildMask)
print (wildMaskBin)
print (broadcast)
print (max_host)
print (min_host)
print (hosts)
