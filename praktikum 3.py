file = open("d:/datal.txt", "r")
try:
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)
except ValueError:
        print('Input tidak valid')
