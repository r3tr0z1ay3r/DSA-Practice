def sockMerchant(n, ar):
    hashMap = {}
    pairs = 0
    pair = []
    for i in ar:
        print(pair)
        if i in pair:
            pairs += 1
            pair.append(i)
            pair.remove(i)
            pair.remove(i)
        else:
            pair.append(i)
    print(pairs)
    return pairs

n,ar = 9,[10, 20, 20, 10, 10, 30, 50, 10, 20]
sockMerchant(n,ar)