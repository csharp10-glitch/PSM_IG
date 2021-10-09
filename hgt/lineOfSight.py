import math as m

def losLoss(d, freq):
    loss = 92.45 + 20 * m.log10(freq) + 20 * m.log10(d)