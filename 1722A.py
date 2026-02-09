t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    if n != 5:
        print("NO")
        continue
    
    if sorted(s) == sorted("Timur"):
        print("YES")
    else:
        print("NO")
