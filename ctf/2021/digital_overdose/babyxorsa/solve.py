N = 0
hint = 0
enc = 0

known = 999
candidates = [(0, 0)]

for i in range(known):
	mod = 1 << (i + 1)
	prod = N & (mod - 1)
	xor = hint & (mod - 1)

	next_candidates = []

	for p_, q_ in candidates:
		for bp in range(2):
			for bq in range(2):
				p1 = p_ ^ (bp << i)
				q1 = q_ ^ (bq << i)

				prod_ = (p1 * q1) & (mod - 1)
				xor_ = p1 ^ q1

				if prod_ == prod and xor_ == xor:
					next_candidates.append((p1, q1))

	del candidates
	candidates = next_candidates


# sanity check
for p_, q_ in candidates:
	mod = 1 << known
	prod = (p_ * q_) & (mod - 1)
	xor = p_ ^ q_

	assert prod == (N & (mod - 1))
	assert xor == hint

print(len(candidates))
