quotient, remainder = divmod(1782, 15);     # 118, 12

myPow = pow(2, 5);                          # 32
noPow = 2 ** 5;                             # 32

def myDivMod(x, y):
    return x // y, x % y;

def pythagoras (cathet_1, cathet_2):
    c = cathet_1 * cathet_1 + cathet_2 * cathet_2;
    return float(c ** (1 / 2));