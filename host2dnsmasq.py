f = open('oriversionofblacklist.txt', 'r')
w = open('dnsmasqversionofblacklist.txt','w')
lines = f.readlines()
for line in lines:
    if(line[0] == '0'):
        tmp = line.split(' ')
        w.write('address=\"/'+ tmp[1].replace('\n', '/') + tmp[0] + '\"\n')
f.close
w.close
