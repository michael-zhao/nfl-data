import random

names = ['nikal', 'andy', 'jason', 'matt', 'dean', 'travis', 'dad', 'mason']
distinctRandNums = random.sample(range(1, len(names)+1), len(names))

zipped = zip(names, distinctRandNums)
res = dict(zipped)

print(list(zip(names, distinctRandNums)))

print(res)

