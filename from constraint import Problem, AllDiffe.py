from constraint import Problem, AllDifferentConstraint

def maze():
    problem = Problem()
    queen = range(8)
    problem.addVariables(queen, range(8))
    problem.addConstraint(AllDifferentConstraint(), queen)

    for i in queen:
        for j in queen:
            if i < j:
                problem.addConstraint(lambda x, y, i=i, j=j: abs(x - y) != abs(i - j), (i, j))

    solution = problem.getSolutions()
    for idx, soln in enumerate(solution[:2], start=1):
        for row in range(8):
            line = ""
            for cols in range(8):
                if soln[cols] == row:
                    line += 'Q'
                else:
                    line += '.'
            print(line)
        print()

if __name__ == "__main__":
    maze()
