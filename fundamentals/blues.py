# Python numeric types (int, float, complex)

# int
intNumber = int(10);                    # 10
intNumber = int('10');                  # 10
intNumber = int('           10\n    ')  # 10
intNumber = int('A', 11);               # 10

# float
floatNumber = float(10.320);
floatNumber = float("+1.809");          # 1.809
floatNumber = float("-1.809");          # -1.809
floatNumber = float("+.809");           # 0.809
floatNumber = float(.809);              # 0.809
floatNumber = float(0.0);               # 0.0
floatNumber = float(.00000);            # 0.0
floatNumber = float('inf');             # inf
floatNumber = float('-Infinity');       # -inf
floatNumber = float("-InFINITY");       # -inf
floatNumber = float("7e-15");           # 0.000000000000007

# complex
complexNumber = complex("+1.25");                   # (1.25+0j)
complexNumber = complex("-4.5j");                   # (-4.5j)
complexNumber = complex("-12.50+4.85j");            # (-12.5+4.85j)
complexNumber = complex("\t( +90-84.10J )\n");      # (90-84.1j)
complexNumber = complex("4.5j");                    # 4.5j

# round
money = "100.58";
soles = money.split(".")[0];
cents = money.split(".")[1];