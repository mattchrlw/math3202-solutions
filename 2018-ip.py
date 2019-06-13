from gurobipy import *

# Data

Ports = ['Manly', 'Cleveland', 'Dunwich']
Cap = [8,8,6]

Travel = [
	[29, 27, 21], [39, 18, 30], [40, 20, 31], [33, 19, 27], [35, 29, 36], [21, 23, 20],
	[30, 41, 32], [37, 27, 36], [20, 25, 34], [36, 28, 20], [24, 23, 25], [38, 22, 40], 
	[39, 19, 27], [30, 18, 28], [40, 20, 32], [21, 32, 40], [23, 18, 20], [31, 18, 20]
]

P = range(len(Ports))
B = range(18)

# Model

m = Model('Boats')

# Sets

# Variables

X = {(b,p): m.addVar(vtype=GRB.BINARY) for b in B for p in P}
Z = m.addVar()

# Objective

# m.setObjective(quicksum(Travel[b][p] * X[b,p] for b in B for p in P), GRB.MINIMIZE)
m.setObjective(Z)

# Constraints

m.addConstrs(quicksum(X[b,p] for p in P) == 1 for b in B)
m.addConstrs(quicksum(X[b,p] for b in B) <= Cap[p] for p in P)
m.addConstrs(Z >= quicksum(Travel[b][p] * X[b,p] for p in P) for b in B)

m.optimize()

for p in P:
    print(Ports[p], [b for b in B if X[b,p].x > 0.9])