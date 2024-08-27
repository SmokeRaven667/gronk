from typing import List
# Write any import statements here
import functools
from collections import Counter
def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  # total_cells = sum([len(x) for x in G])

  # option 1
  # print(functools.reduce(lambda acc, x: acc + len(x), G, 0))

  # option 2
  # sucks to iterate structure twice
  counts = Counter([item for sublist in G for item in sublist])
  hits = Counter([item for sublist in G for item in sublist if item == 1])
  
  return sum(hits.values())/sum(counts.values())


print(getHitProbability(2, 3, [[0, 0, 1], [1, 0, 1]])) # Expected output: 0.5  
print(getHitProbability(2, 2, [[0, 0], [0, 0]])) # Expected output: 0.0