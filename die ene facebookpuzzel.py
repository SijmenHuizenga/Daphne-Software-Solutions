
def solve(problem, operations, base=""):
	"""
	Een functie om Daphne's breinbrekende facebookpuzzel op te lossen.
	
	Het doel van deze puzzel is om een som op te lossen door operatoren in te vullen in de som.
	
	Pas op als je computer bijzonder aardappel is, omdat er wel 4^4=256 opties getest worden!
	"""
	if len(problem) == 1:
		base = base + str(problem[0])
		if eval(base):
			print("Solution: " + base)
		return

	if problem[0] == "==" or problem[1] == "==":
		solve(problem=problem[1:], operations=operations, base=base+str(problem[0]))
		return

	for n in range(0, len(operations)):
		solve(problem=problem[1:], operations=operations, base=base + str(problem[0]) + str(operations[n]))


solve(problem=[8, 4, 6, "==", 6, 7, 4], operations=["+", "-", "*", "/"])