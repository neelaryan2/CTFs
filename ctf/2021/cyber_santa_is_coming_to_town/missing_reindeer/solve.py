from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64


def invpow(x, n):
    high = 1
    while high**n < x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1


n = 0xe623972884b1f4d722bdd5ee5beb84cb84760c2ed0ffafd93cd6030fb20d7930903bd1731dc74c954a23075303dfd71b885cd66e985bf759ed17a985f7e7d837c857bd31a147d74da261492858fa5fcfb89230878ef4fffcff92fc292989326454afb51bb7ab253fefd5b357bf83a639f153204afc5628f3e02022c6949dc23cb19d2fd639b6d5987ac332a01dd23b437a6777bb967f80e522e941e5f972160aed556db7393919806422ae1a7dc9b19996fdb7b29141472d6803dff42a713db57ac078fca48d1a6861423de3a12ed9cfafb831e5d69b92d71963d023228c2612ea334a652c46121f505d1b5a551224c69fc8239cfe1093de68095f7153159667
e = 3

c = 'Ci95oTkIL85VWrJLVhns1O2vyBeCd0weKp9o3dSY7hQl7CyiIB/D3HaXQ619k0+4FxkVEksPL6j3wLp8HMJAPxeA321RZexR9qwswQv2S6xQ3QFJi6sgvxkN0YnXtLKRYHQ3te1Nzo53gDnbvuR6zWV8fdlOcBoHtKXlVlsqODku2GvkTQ/06x8zOAWgQCKj78V2mkPiSSXf2/qfDp+FEalbOJlILsZMe3NdgjvohpJHN3O5hLfBPdod2v6iSeNxl7eVcpNtwjkhjzUx35SScJDzKuvAv+6DupMrVSLUfcWyvYUyd/l4v01w+8wvPH9l'
c = base64.b64decode(c)
c = bytes_to_long(c)

flag = long_to_bytes(invpow(c, e))
print(flag.decode())
