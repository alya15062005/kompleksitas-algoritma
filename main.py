coint = [2, 3, 5, 10, 15]

amount = int(input("Masukan jumlah yang dicapai:"))

count = 0 

for coin in coint:
    while amount >= coin:
        amount -= coin
        coin += 1 

print("jumlah koin yang diperlukan:", count)