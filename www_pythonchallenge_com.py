'''
Created on Oct 25, 2017

@author: Niraj.Kumar
'''

#4






#3
'''p=[]
for l in open('challenge3.txt'):
    for i in l:
        p.append(i)

#create a dictionary
dic = {}
for i in set(p):
    dic.update({i:0})

for i in p:
    n= dic.get(i)
    dic.update({i:n+1})
print(dic)'''

#itqluaye aeilqtuy equality
 

'''from pyspark.context import SparkContext

#initializing spark session
sc = SparkContext.getOrCreate()
text_file = sc.textFile("challenge3.txt")
counts = text_file.flatMap(lambda line: line.split()) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
print(counts)'''





#1 274877906944
'print(2**38)'

#2
'''str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
str ='map'
print(str.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")))


list =[]
for i in str:
    if(i in [' ','.','(',')']):
        list.append(i)
    else:
        list.append(chr(ord(i)+2))
    
for i in list:
    print(i, end='')
    '''