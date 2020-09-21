from z3 import *

if __name__ == '__main__':
    # x = z3.Int("x")
    # y = z3.Int("y")
    # z = z3.Int("z")
    # exp = z3.And(3 * x - y + z == 185, 2 * x + 3 * y - z == 321, x + y + z == 173)
    # solver = z3.Solver()
    # solver.add(exp)
    # solver.check()
    # print(solver.model())
    x = z3.Int("x")
    exp = z3.And(x * x + x - 7943722218936282 == 0)
    solver = z3.Solver()
    solver.add(exp)
    solver.check()
    print(solver.model())

