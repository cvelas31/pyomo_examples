"""
Install ipopt and glpk using conda
"""

from pyomo.environ import (
    ConcreteModel,
    Var,
    Binary,
    Constraint,
    minimize,
    log,
    Objective,
    SolverFactory,
)

## Create a simple model
model = ConcreteModel()

model.x = Var(bounds=(1.0, 10.0), initialize=5.0)
model.y = Var(within=Binary)

model.c1 = Constraint(expr=(model.x - 4.0) ** 2 - model.x <= 50.0 * (1 - model.y))
model.c2 = Constraint(expr=model.x * log(model.x) + 5.0 <= 50.0 * (model.y))

model.objective = Objective(expr=model.x, sense=minimize)

## Solve the model using MindtPy
SolverFactory("mindtpy").solve(model, mip_solver="glpk", nlp_solver="ipopt")

model.objective.display()
model.display()
model.pprint()