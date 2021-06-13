import pyomo.environ as pyo
import os
os.environ['NEOS_EMAIL'] = 'cvelas31@gmail.com'

model = pyo.ConcreteModel()
model.x = pyo.Var([1, 2], domain=pyo.NonNegativeReals)
model.OBJ = pyo.Objective(expr=2*model.x[1] + 3*model.x[2])
model.Constraint1 = pyo.Constraint(expr=3*model.x[1] + 4*model.x[2] >= 1)

# Execute with
# pyomo solve --solver=cplex --solver-manager=neos simple_model.py