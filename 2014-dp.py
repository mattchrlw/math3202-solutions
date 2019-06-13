Demand = [10,20,30,30,20,20]

_V = {}

def V(t,s):
    if t == 6:
        return (0,())
    if (t,s) not in _V:
        _V[t,s] = min((20*min(a,1) + 2*a + 0.1*min(s+a-Demand[t-1], 40) + V(t+1, min(s+a-Demand[t], 40))[0], 
        (a,)+V(t+1, min(s+a-Demand[t], 40))[1]) for a in [0,10,20,30,40,50,60] if (s+a) >= Demand[t])
    
    return _V[t,s]

print(V(0, 0))