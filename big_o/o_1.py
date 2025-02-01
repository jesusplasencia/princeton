## family of algos than run in O(1) complexity
def dist(p, q):
    dx = (p[0] - q[0]) ** 2  # 1 instruction
    dy = (p[1] - q[1]) ** 2  # 1 instruction
    return (dx + dy) ** 0.5  # 1 instruction
