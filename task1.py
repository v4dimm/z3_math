from z3 import *

def taskSolve(n):
	X = [Int("x{0}".format(x)) for x in range(n)]
	Y = [Int("y{0}".format(y)) for y in range(n)]

	s = Solver()

	s.add(Distinct(*X), Distinct(*Y))

	for i in range(n-1):
		for j in range(i+1,n):
			s.add(X[i]-X[j] != Y[i] - Y[j])

	for i in range(n):
		s.add(X[i]>=0, X[i]<n)
		s.add(Y[i]>=0, Y[i]<n)

	if s.check() == sat:
		print(s.model())

taskSolve(4)