# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from ortools.sat.python import cp_model
from ortools.linear_solver import pywraplp
# Define data for machine and task    
machines=[
{"cp":100,"mem":100,"stgIO":100,"netIO":100,"type":"1","cost":170},
{"cp":200,"mem":60,"stgIO":200,"netIO":100,"type":"2","cost":150},
{"cp":50,"mem":60,"stgIO":200,"netIO":100,"type":"2","cost":60}
]
task={"cp":80,"mem":60,"stgIO":60,"netIO":60}

num_machines=len(machines)
print(task)

# ## Machine type assignment - with CP-Sat solver 02
# %%
# =============Create the solver
model = cp_model.CpModel()
# =======create decision variabl
k=model.NewIntVar(0, num_machines,'m')

# ========define constraints
#for i in range(num_machines):
model.Add(machines[k.Index()]['cp']>=task['cp'])
model.Add(machines[k.Index()]['mem']>=task['mem'])
model.Add(machines[k.Index()]['stgIO']>=task['stgIO'])
model.Add(machines[k.Index()]['netIO']>=task['netIO'])

model.Minimize(machines[k.Index()]['cost'])
solver_cp=cp_model.CpSolver()
status=solver_cp.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print('Total cost = ', solver_cp.ObjectiveValue())
    print(k.Index())
    

# %% [markdown]
# ## Machine type assignment - with CP-Sat solver
# =============Create the solver
model = cp_model.CpModel()
#===========create decision varibles, x[i] indicate if it fit to the task  >1>  or not <0>
x=[]
for i in range(num_machines):
    x.append(model.NewBoolVar(f'x[{i}]'))

#===============define constraints
#only one machine will be assigned
model.Add(sum(x[i] for i in range(num_machines))==1)

#cpu constraint
model.Add(sum(machines[i]['cp']*x[i] for i in range(num_machines))>=task['cp'] )
#mem constraint
model.Add(sum(machines[i]['mem']*x[i] for i in range(num_machines))>=task['mem'] )
#stgIO constraint
model.Add(sum(machines[i]['stgIO']*x[i] for i in range(num_machines))>=task['stgIO'] )
#netIO constraint
model.Add(sum(machines[i]['netIO']*x[i] for i in range(num_machines))>=task['netIO'] )

#===============deinf objective
model.Minimize(sum(x[i]*machines[i]['cost'] for i in range(num_machines)))
solver_cp=cp_model.CpSolver()
status=solver_cp.Solve(model)


# Print solution.
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print('Total cost = ', solver_cp.ObjectiveValue())
    for i in range(len(x)):
        print(solver_cp.BooleanValue(x[i]))

else:
    print("No Optimal or Feasible solution")






# %% [markdown]
# ## Machine type assignment - with LP solver 

# =============Create the mip solver with the SCIP backend.
solver = pywraplp.Solver.CreateSolver('SCIP')

#===========create decision varibles, x[i] indicate if it fit to the task  >1>  or not <0>
x={}
for i in range(num_machines):
    x[i]=solver.IntVar(0,1,'')

#===============define constraints
#only one machine will be assigned
solver.Add(solver.Sum(x[i] for i in range(num_machines))==1)

#cpu constraint
solver.Add(solver.Sum(machines[i]['cp']*x[i] for i in range(num_machines))>=task['cp'] )
#mem constraint
solver.Add(solver.Sum(machines[i]['mem']*x[i] for i in range(num_machines))>=task['mem'] )
#stgIO constraint
solver.Add(solver.Sum(machines[i]['stgIO']*x[i] for i in range(num_machines))>=task['stgIO'] )
#netIO constraint
solver.Add(solver.Sum(machines[i]['netIO']*x[i] for i in range(num_machines))>=task['netIO'] )


#===============deinf objective

solver.Minimize(solver.Sum(x[i]*machines[i]['cost'] for i in range(num_machines)))
status=solver.Solve()

# Print solution.
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('Total cost = ', solver.Objective().Value())
    for i in range(len(x)):
        print(x[i].solution_value())
else:
    print("No Optimal or Feasible solution")

# %% [markdown]
# ## Example from Google - Assignment 01

# %%
from ortools.linear_solver import pywraplp
# =============Create the mip solver with the SCIP backend.
solver = pywraplp.Solver.CreateSolver('SCIP')

#===========create decision varibles, x[i] indicate if it fit to the task  >1>  or not <0>
x={}
for i in range(num_machines):
    x[i]=solver.IntVar(0,1,'')


#===============define constraints
#only one machine will be assigned
solver.Add(solver.Sum(x[i] for i in range(num_machines))==1)

#cpu constraint
solver.Add(solver.Sum(machines[i]['cp']*x[i] for i in range(num_machines))>=task['cp'] )
#mem constraint
solver.Add(solver.Sum(machines[i]['mem']*x[i] for i in range(num_machines))>=task['mem'] )
#stgIO constraint
solver.Add(solver.Sum(machines[i]['stgIO']*x[i] for i in range(num_machines))>=task['stgIO'] )
#netIO constraint
solver.Add(solver.Sum(machines[i]['netIO']*x[i] for i in range(num_machines))>=task['netIO'] )

#===============deinf objective
solver.Minimize(solver.Sum(x[i]*machines[i]['cost'] for i in range(num_machines)))
status=solver.Solve()

# Print solution.
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('Total cost = ', solver.Objective().Value())
    for i in range(len(x)):
        print(x[i].solution_value())
else:
    print("No Optimal or Feasible solution")



# %%
# Example of assignment from or-tools
from ortools.linear_solver import pywraplp

def main():
    # Data
    costs = [
        [90, 80, 75, 70],
        [35, 85, 55, 65],
        [125, 95, 90, 95],
        [45, 110, 95, 115],
        [50, 100, 90, 100],
    ]
    num_workers = len(costs)
    num_tasks = len(costs[0])

    # Solver
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')


    # Variables
    # x[i, j] is an array of 0-1 variables, which will be 1
    # if worker i is assigned to task j.
    x = {}
    for i in range(num_workers):
        for j in range(num_tasks):
            x[i, j] = solver.IntVar(0, 1, '')

    # Constraints
    # Each worker is assigned to at most 1 task.
    for i in range(num_workers):
        solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) <= 1)

    # Each task is assigned to exactly one worker.
    for j in range(num_tasks):
        solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 1)

    # Objective
    objective_terms = []
    for i in range(num_workers):
        for j in range(num_tasks):
            objective_terms.append(costs[i][j] * x[i, j])
    solver.Minimize(solver.Sum(objective_terms))

    # Solve
    status = solver.Solve()

    # Print solution.
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print('Total cost = ', solver.Objective().Value(), '\n')
        for i in range(num_workers):
            for j in range(num_tasks):
                # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
                if x[i, j].solution_value() > 0.5:
                    print('Worker %d assigned to task %d.  Cost = %d' %
                          (i, j, costs[i][j]))


if __name__ == '__main__':
    main()



# %%
