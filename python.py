#!/usr/bin/python3.6

import sys

fname = sys.argv[1]
f = open(fname, 'r')
s = f.read()
lines = s.split("\n")
#print(lines)
ips = set()
for line in lines :
         elems = line.split(' ')
         ip = elems[0]
#         print(ip)
         ips.add(ip)

ips = sorted(list(ips))
for ip in ips :
       print(ip)



#print(sorted(list(ips)))
httpCodes = [ 200, 404 ]
code200 = 0
code404 = 0
for line in lines :
        if len(line) != 0 :
           elems = line.split(' ')
           try :
               code = int(elems[8])
               if code == 200 :
                      code200 = code200 + 1
               if code == 404 :
                      code404 = code404 + 1
           except :
                  pass
print('all:', len(lines), '200:', code200, '404:', code404)

log = open('stat.log', 'a')
codeReport = [

nLine = 0
for line in lines :
        nLine = nLine + 1
        if len(line) != 0 :
        elems = line.split(' ')
        try :
               code = int(elems[8])
               ip = elems[0]
               p = False
               for i in codeReport :
               if i.get(ip, False) == False :
                                p = True
               if p == False :
                                codeReport.append( { ip : {"200" : 0, "404" : 0} )
                      for i in codeReport :
                      
                             if i.get(ip, False) != False  :
                                     if code == 200 :
                                            i[ip]["200"] = i[i]["200"] + 1
                                     if code == "404" :
                                            i[ip]["404"] = i[ip]["200"] + 1
        except :
s = 'Line:', + str(nLine) + ' incorrect status code', "\n"
log = open('./stat.log', 'a')
codReport = []
for i in codeReport :
         print(i)
