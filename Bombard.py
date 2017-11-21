'''
Created on Oct 24, 2017

@author: Niraj.Kumar
'''
class Bomb(object):
    def bombard(self,lst):
        start = 0
        end  = 0
        i = 0
        flag = True;
        while flag:
            flag = False
            print("{}".format(lst))
            try:
                if( lst[i]==lst[i+1]):
                    end +=1
                    flag = True
            except IndexError:
                if start != end:
                    for j in range(start,end+1):
                        lst.pop(start)
                break
            if(lst[i]!= lst[i+1]):
                if start != end:
                    for j in range(start,end+1):
                        lst.pop(start)
                    i-=end
                    start = i
                    end = i
                    i-=1
                    flag = True
                else:
                    start += 1
                    end += 1
                    flag = True
            i += 1
        return lst
        
if __name__ == '__main__':
    pass
str = 'aaaaaaaaba'
lst = []
for i in str:
    lst.append(i)

print(Bomb().bombard(lst))
