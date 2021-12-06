from collections import defaultdict

def nxt(n, v1, v2):
    val = n + 2460 * v1 + 205 * v2
    return val

root = 0x403EB6
nodes = [0x4015DF, 0x4016AC, 0x401779, 0x401846, 0x401913, 0x4019E0, 0x401AAD, 0x401B7A, 0x401F7B, 0x402048, 0x402115, 0x4021E2, 0x4022AF, 0x40237C, 0x402449, 0x402516, 0x402917, 0x4029E4, 0x402AB1, 0x402B7E, 0x402C4B, 0x402D18, 0x402DE5, 0x402EB2, 0x4032B3, 0x403380, 0x40344D, 0x40351A, 0x4035E7, 0x4036B4, 0x403781, 0x40384E, 0x403C4F, 0x403D1C, 0x403DE9, 0x403EB6, 0x403F83, 0x404050, 0x40411D, 0x4041EA, 0x4045EB, 0x4046B8, 0x404785, 0x404852, 0x40491F, 0x4049EC, 0x404AB9, 0x404B86, 0x404F87, 0x405054, 0x405121, 0x4051EE, 0x4052BB, 0x405388, 0x405455, 0x405522, 0x405923, 0x4059F0, 0x405ABD, 0x405B8A, 0x405C57, 0x405D24, 0x405DF1, 0x405EBE]
node_set = set(nodes)

v12 = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
v12 = {i + 1:v for i, v in enumerate(v12)}

vis = defaultdict(lambda: False)
path = []

def recover(path):
    ans = []
    for i in range(1, len(path)):
        u, v = path[i - 1:i + 1]
        found = 0
        for k, (v1, v2) in v12.items():
            if nxt(u, v1, v2) == v:
                ans.append(k)
                found += 1
        assert found == 1
    ans.append(-1)
    print(ans)
    return ans


def get_path(path):
    if len(path) == len(nodes):
        print(path)
        return
    
    valid = node_set - set(path)
    v = path[-1]

    for v1, v2 in v12.values():
        u = nxt(v, v1, v2)
        if u in valid:
            get_path(path + [u])


get_path([root])
