'''
Created on Nov 25, 2017

@author: Niraj.Kumar
'''
'replace space to %20 in given string'

st = "this is url"

import time
start_time = time.time()


#st[0]='k'
res = ""
for i in st:
    if i == ' ':
        res += "%20"
    else :
        res += i

print(res)

print("--- %s seconds ---" % (time.time() - start_time))