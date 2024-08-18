import math

def DPchange(money, Coins):
    MinNumCoins = {}
    MinNumCoins[0] = 0
    infinity = math.inf
    for m in range(1,money+1):
        MinNumCoins[m] = infinity
        for coin in Coins:
            if m >= coin:
                if MinNumCoins[m - coin] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - coin] + 1
    return MinNumCoins[money]






text = open('dataset_243_10.txt').read().split('\n')
money = int(text[0])
Coins = text[1].split()
Coins = [int(x) for x in Coins]
print(DPchange(money, Coins))
