from pulp import *

# create an Lp instance
prob = LpProblem("simplex problem 1", LpMaximize)

# initialize the variables
x = LpVariable("x", 0)
y = LpVariable("y", 0)
z = LpVariable("z", 0)

# add the objective function
prob += 4*x + 3*y + 2*z, "objective function"

# enter the constraits
prob += x + z <= 2, "first constrait"
prob += -x - y + z <= 1, "second constrait"
prob += x + y + z <= 3, "third constrait"

#solve the LP
prob.solve()

# print out whether or not this is (in)feasible, optimal, (un)bounded
print("Status:", LpStatus[prob.status])

# print out the variables' optimal values
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimized objective function value is printed to the screen
print("The optimal solution 'z' is: ", value(prob.objective))