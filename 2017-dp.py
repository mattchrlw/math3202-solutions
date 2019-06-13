_V = {}

def V(t, s: tuple, c):
    if t == 0:
        return (10*s[0] + s[1]) * (10*s[2] + s[3])
    if (t,s,c) not in _V:
        possibilities = []
        for i in range(4):
            if s[i] == -1:
                cards = list(s)
                cards[i] = c
                expectation = sum(
                    V(t-1, tuple(cards),j) for j in range(10) if j not in cards
                ) / (10-(4-t)-1)
                possibilities.append(expectation)
        _V[t,s,c] = min(possibilities)
    return _V[t,s,c]

print([V(4,(-1,-1,-1,-1), c) for c in range(10)])

            # newlist = list(s)
            # possibilities.append(V(t+1, tuple(newlist), left)*1/(10-(4-t)))

    # if [t,s,c] not in _V:
    #     for i in []
    #     for i in range(4):
    #         current_cards = list(s)
    #         current_cards[i] = c
    #         if s[i] != -1:



        # _V[t,s,c] = min(
        #     current_cards = list(s)
        #     current_cards[i] = c
        #     sum(1/(10-(4-t))*V(t+1,)
        #     for a in range(10) if a not in s
        # )


    # return _V[t,s,c]