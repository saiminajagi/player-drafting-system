import random
t=[12]
for i in range(5):
	from functools import partial
	m=partial(random.sample,range(12),12)
	sample=[m() for i in range(8)]
print(sample)	