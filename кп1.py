import math

β2 = 1.7
m = 1
α1 = math.sin(math.pi / 2)
α2 = math.log10(0.05) + pow (math.e, α1)
β1 = pow (math.e, α1)

A = ((α1*β1)-(α2*β2))/((m*α1)- pow (α2, 2))
print(A)