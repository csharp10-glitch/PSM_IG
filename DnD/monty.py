from DnD import Dice

expect = []
expectp = []

for i in range(8,21):
    attack = Dice.dStar(20,10000000)
    damage = Dice.dStar(6,10000000)
    attackp = Dice.dStarMod(20,10000000)
    damagep = Dice.dStarMod(6,10000000)
    for j in range(200):
        # print(i)
        # print(attack[j])
        # print(attack[j]>i)
        if attack[j]>=i:
            expect.append(damagep[j])
        else:
            expect.append(0)
        if attackp[j]>=i:
            expectp.append(damage[j])
        else:
            expectp.append(0)

for i in range(13):
    print(i+8)
    print(Dice.dAverage(expect[(0+200*i):(200+200*i)]))
    print(Dice.dAverage(expectp[(0+200*i):(200+200*i)]))

