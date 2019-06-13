from gurobipy import *

Packages = [70,90,100,110,120,130,150,180,210,220,250,280,340,350,400]
Sections = ['A','B','C','D']

# Sets
S = range(len(Sections))
P = range(len(Packages))

m = Model("Balancing")

# Data

# Variables
X = {(p,s): m.addVar(vtype=GRB.BINARY) for p in P for s in S}

# Constraints
m.addConstrs(quicksum(X[p,s] for p in P) >= 3 for s in S)
m.addConstrs(quicksum(X[p,s]*Packages[p] for p in P) <= 1000 for s in S)
m.addConstr(quicksum(X[p,0]*Packages[p] for p in P) == quicksum(X[p,3]*Packages[p] for p in P))
m.addConstr(quicksum(X[p,1]*Packages[p] for p in P) == quicksum(X[p,2]*Packages[p] for p in P))
m.addConstrs(quicksum(X[p,s] for s in S) == 1 for p in P)

m.optimize()

for s in S:
    print(s, [p for p in P if (X[p,s].x > 0.9)])