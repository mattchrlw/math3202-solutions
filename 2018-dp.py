Payoff = [
    [3,0],
    [5,1]
]

_V = {}

def V(t,s):
    if t == 0:
        return (0, ())
    else: 
        return max((s*Payoff[0][0] + (1-s)*Payoff[0][1] + V(t-1, min(s+0.1,1))[0],(0,) + V(t-1, min(s+0.1,1))[1]),
                   (s*Payoff[1][0] + (1-s)*Payoff[1][1] + V(t-1, max(s-0.2,0))[0],(1,) + V(t-1, min(s+0.1,1))[1]))

print(V(10,0.6))