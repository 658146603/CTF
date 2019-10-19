from z3 import *

if __name__ == '__main__':
    x = Int('x')
    y = Int('y')
    solver: Solver = Solver()
    solver.add(x-y == 3)
    solver.add(3*x - 8*y == 4)
    print(solver.check())
    print(solver.model())
