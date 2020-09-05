'''
def stu_avg(lst):
    d = {}
    for i in lst:
        if i[0] not in d:
            d[i[0]] = []
        if i[0] in d:
            d[i[0]].append(i[1])
    for i in d:
        t5 = sorted(d[i],reverse=True)[:5]
        print(i,sum(t5)//5)
    
n = int(input())
x = [[int(x) for x in input().split()]for x in range(n)]
stu_avg(x)

def checkAnagram(s1,s2):
    if (set(s1) == set(s2) )and (len(s1) == len(s2)):
        return True
    else:
        return False
def s_ana(s):
    words = s.split()
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if not checkAnagram(words[i],words[j]):
                temp += 1


    
    
        
s = input()
s_ana(s)       
'''


def rev(s):
    temp = []
    ind = []
    s = list(s)
    for index, i in enumerate(s):
        if i.isalpha():
            temp.append(i)
        else:
            ind.append(i)

    temp = temp[::-1]
    for i in s:
        if i in ind:
            print(i, end="")
        else:
            print(, end="")


s = input()
rev(s)
