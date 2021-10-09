from DnD import Dice

stats = []

for i in range(6):
    stats.append(Dice.dStar(6,4))
    stats[-1].remove(min(stats[-1]))
    stats[-1]=sum(stats[-1])

print(stats)