

def football(players):
    player = players[0]
    count = 1
    for i in range(1, len(players)): # i = 1,2,3,4,5,6,7,8
        if player == players[i]:        #1,1,1,0,0,0,1,1
            count += 1
            if count == 7:
                return "YES"
        else:
            count = 1
            player = players[i]

    return "NO"


a = input()

print(football(a))
