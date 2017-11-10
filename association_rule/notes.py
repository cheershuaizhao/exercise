Learned Set proprities from implement Apriori

1. Convert set into frozenset for being dict keys. Do not conver set into tuple for being dict keys. Tuple has sequences.
{'ar', 'pa'} in dt_fs.keys() #correct
{'pa', 'ar'} in dt_fs.keys() #wrong

2. set operations
https://docs.python.org/2/library/sets.html

3. deep copy set
from copy import deepcopy
deepcopy(set_a)
