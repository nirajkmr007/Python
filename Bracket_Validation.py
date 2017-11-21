'''
Created on Oct 24, 2017

@author: Niraj.Kumar
'''

if __name__ == '__main__':
    pass

get_match = {']':'[','}':'{',')':'('}
flag = True

inputs = '{[}]}'

stack = []

for i in inputs:
    if(i in ['[','{','(']):
        stack.append(i)
    else:
        if(len(stack) and get_match[i] == stack[-1]):
            stack.pop()
        else:
            flag = False
            break;
        
if(flag and len(stack)== 0):
    print("ok")
else:
    print("not ok")
    