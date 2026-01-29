n,k = map(int,input().split())

time_left = 240 - k
count = 0

for i in range(1,n+1):
    if time_left >= i*5:
        time_left -= i*5
        count += 1
    else:
        break
print(count)