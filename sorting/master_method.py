# Page 135

# T (n) = a T(n / b) + f(n)
# 1. if f(n) = O(n ^ log_b(a - e))      e > 0 : T (n) = Theta(n ^ log_b(a))
# 2. if f(n) = Theta(n ^ log_b(a))            : T (n) = Theta(n ^ log_b(a) * lg(n))
# 3. if f(n) = Omega(n ^ log_b(a + e))  e > 0 : T (n) = Theta(f(n))

# EXERCISES
# T(n) = 9T(n/3) + n
# f(n) = n;
# a = 9
# b = 3
# f(n) = O(n)  e = 1 -> T(n) = Theta(n ^ 2)

# T(n) = T(2/3n) + 1
# f(n) = 1
# a = 1
# b = 3/2
# f(n) = Theta(n ^ 0) -> T(n) = Theta(lg(n))

# T(n) = 3T(n / 4) + n*lg(n)
# f(n) = n*lg(n)
# a = 3
# b = 4
# n ^ log_b(a) = n ^ log_4(3) = Omega(n ^ 0.8) < f(n)
# T(n) = Theta(n * lg(n))

# T(n) = 2 T(n / 2) + n * lg(n)
# f(n) = n * lg(n)
# a = 2
# b = 2
# f(n) = Theta(n)
# T(n) = n * lg(n)

# T(n) = 8 T(n / 2) + Theta(n ^ 2)
# f(n) = Theta(n ^ 2)
# a = 8
# b = 2
# n ^ log_b(a) = n ^ 3
# T(n) = Theta(n ^ 3)

# T(n) = 7 T(n / 2) + Theta(n ^ 2)
# f(n) = Theta(n ^ 2)
# a = 7
# b = 2
# n ^ log_b(a) = n ^ 2.80
# T(n) = Theta(n ^ lg(7))