n = int(input("얼마를 거슬러 주어야 하나요?: "))
count = 0

list = [500, 100, 50 ,10]

for coin in list:
    count += n // coin
    n %= coin

print(count)
