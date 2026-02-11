x = list(map(int, input().split()))
x.sort()

meeting_point = x[1] #median

total_distance = abs(x[0] - meeting_point) + abs(x[1] - meeting_point) + abs(x[2] - meeting_point)

print(total_distance)