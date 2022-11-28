# n=int(input())
# x=list(map(int,input().split()))
# l=[]
# i=0
# while(i<len(x)):
#     b=(i+1)*-1
#     l.append(x[b])
#     i+=1
# j=0
# while(j<len(l)):
#     print(l[j],end=" ")
#     j+=1


n=int(input())
if n%5==0 and n%11==0:
    print('BOTH')
elif n%5==0 or n%11==0:
    print('ONE')
else:
    print('None')