def climbingLeaderboard(ranked, player):
    l,r = len(ranked)-1,0
    merged = []
    while l >= 0 or r == len(player):
        if ranked[l] < player[r]:
            merged.append(ranked[l])
            l -= 1
        else:
            merged.append(player[r])
            r += 1
    if player[r]:
        merged.append(player[r])
    ranking,rank = {},1
    for i in range(len(merged)-1,0,-1):
        if merged[i] not in ranking.keys():
            ranking[merged[i]] = rank
            rank += 1
    return_arr = []
    for i in player:
        return_arr.append(ranking[i])
    print(ranking)
    print(return_arr)
ranked1 = [100 ,100 ,50 ,40 ,40 ,20 ,10]
player1 = [5 ,25 ,50 ,120]
climbingLeaderboard(ranked1,player1)