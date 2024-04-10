## MARK: - Includes

# Include the functions
from parkerFuncsProject350 import *

# Note: Functions not under testing are in another file (included above).

## MARK: - Variables

# Create nodes and edges
nodes = CreateNodes()
edges = CreateEdges(nodes)

# Create the formula
boolFormula = GetFormulaFromEdges(edges)

# Define even and prime nodes
evenNodes = GetEvenNodesFrom(nodes)
primeNodes = GetPrimeNodesFrom(nodes)

# Create the bdd
bdd = expr2bdd(boolFormula)

# Create the closure RoR, RR2, and RR2*
closureRR = GetClosure(boolFormula, nodes)
closureRR2 = GetClosure(closureRR, nodes)
closureRR2Star = closureRR2.smoothing()

# Get Reachable Evens
reachableEvens = GetReachable(boolFormula, nodes, evenNodes)

# Get Reachable Primes
reachablePrimes = GetReachable(boolFormula, nodes, primeNodes)

# Define Statement A:
statementA = reachablePrimes & Or(reachableEvens, closureRR2Star).smoothing()


### MARK: - Tests
print("See tests below. ASNI colors used...")
print("----------Begin tests----------")
## MARK: RR Tests:
SetRedOutput()
assert closureRR.restrict({nodes[27]: 1, nodes[3]: 1}), "Failure: RR(27, 3) is false. Expected true!"
SetGreenOutput()
print("Success: RR(27, 3) is true!")

SetRedOutput()
assert (not closureRR.restrict({nodes[16]: 1, nodes[20]: 1})) == False, "Failure: RR(16, 20) is true. Expected false!"
SetGreenOutput()
print("Success: RR(16, 20) is false!")


## MARK: EVEN Tests:
SetRedOutput()
assert reachableEvens.restrict({nodes[14]: 1}), "Failure: EVEN(14) is false. Expected true!"
SetGreenOutput()
print("Success: EVEN(14) is true!")

SetRedOutput()
assert (not reachableEvens.restrict({nodes[13]: 1})) == False, "Failure: EVEN(13) is true. Expected false!"
SetGreenOutput()
print("Success: EVEN(13) is false!")


## MARK: PRIME Tests:
SetRedOutput()
assert reachablePrimes.restrict({nodes[7]: 1}), "Failure: PRIME(7) is false. Expected true!"
SetGreenOutput()
print("Success: PRIME(7) is true!")

SetRedOutput()
assert (not reachablePrimes.restrict({nodes[2]: 1})) == False, "Failure: PRIME(2) is true. Expected false!"
SetGreenOutput()
print("Success: PRIME(2) is false!")


## MARK: RR2 Tests:
SetRedOutput()
assert closureRR2.restrict({nodes[27]: 1, nodes[6]: 1}), "Failure: RR2(27, 6) is false. Expected true!"
SetGreenOutput()
print("Success: RR2(27, 6) is true!")

SetRedOutput()
assert (not closureRR2.restrict({nodes[27]: 1, nodes[9]: 1})) == False, "Failure: RR2(27, 9) is true. Expected false!"
SetGreenOutput()
print("Success: RR2(27, 6) is false!")

## MARK: Statement A:
SetRedOutput()
assert statementA, "Failure: StatementA is false. Expected true!"
SetGreenOutput()
print("Success: StatementA is true!")

ResetOutputColor()

print("----------End tests----------")
