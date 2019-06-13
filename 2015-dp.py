Operators = [155, 120, 140, 100, 155]

_V = {}
max_operators = 155

def V(t,s):
    actions = []
    if t == 0:
        return (0,())
    if (t,s) not in _V:
        _V[t,s] = min((2000*(s-Operators[5-t]) + 200*(abs(a)**2) + V(t-1, s+a)[0], (a,)+V(t-1, s+a)[1]) 
        for a in range(-max_operators, max_operators+1) if (s+a) >= Operators[5-t] if (s+a) <= max_operators)
    
    return _V[t,s]

print(V(5,155))