#(답지봄) 만들 수 있는 금액부터 추려 나가는 방법
'''import sys

N=int(sys.stdin.readline())
coin=list(map(int,sys.stdin.readline().split()))
coin.sort() #오름차순 정렬

target=1 #1부터 만들 수 있는지 확인
for num in coin:
    if target<num: #만들 수 없는 금액 발생
        break
    target+=num #target-1만큼은 만들 수 있다.

print(target)
'''

n=int(input())
coins=sorted(list(map(int,input().split())))
data=[coins[0]]
for i in range(1,n):
    tmp=[]
    for j in data:
        new=coins[i]+j
        if new not in data:
            tmp.append(new)
        
    if coins[i] not in data:
        tmp.append(coins[i])            
    
    data+=tmp

for i in range(max(data)):
    if i not in data:
        answer=i
        break

print(answer)