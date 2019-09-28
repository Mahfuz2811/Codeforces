
word = input() #WUB  WE  WUB  ARE  WUB  WUB  THE  WUB  CHAMPIONS  WUB  MY  WUB  FRIEND  WUB
songs = ''
k = 0

while word:
    if word[0:3] == 'WUB':
        word = word[3:]
    else:
        j = 0
        ch = ''
        while word[j:3+j] != 'WUB':
            ch += word[j]
            j += 1
            if len(word) == j:
                break

        songs += ch + ' '
        word = word[len(ch):]

print(songs.strip())
