# Problem Statement : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/
import itertools
#https://www.youtube.com/watch?v=Qu3dThVy6KQ
string = input()
string=string.split(' ')
k=int(string[1])
strr = string[0]

char_list = []
for i in strr:
    char_list.append(i)
char_list.sort()

ans = list(itertools.combinations_with_replacement(char_list,k))
for tuplee in ans:
    temp=''
    for idx in range(k):
        temp += tuplee[idx]
    print(temp)
