import math

from PA3.countInv import count_inversions

RND_SIZE = 100

result = list(reversed(range(1, RND_SIZE + 1)))

print(count_inversions(result))
print(result)
print("n logn = " + str({RND_SIZE * math.log2(RND_SIZE)}))