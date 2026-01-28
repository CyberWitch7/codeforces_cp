n = int(input().strip())
s = input().strip().lower()

letters = set(s)
if len(letters) == 26:
    print("YES")    
else:
    print("NO")