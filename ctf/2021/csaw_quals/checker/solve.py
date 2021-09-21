def up(x):
    x = [f"{ord(x[i]) << 1:08b}" for i in range(len(x))]
    return ''.join(x)


def up_inv(x):
    assert len(x) % 8 == 0
    ret = ''
    for i in range(0, len(x), 8):
        c = int(x[i:i + 8], 2) >> 1
        ret += chr(c)
    return ret


def down(x):
    x = ''.join(['1' if x[i] == '0' else '0' for i in range(len(x))])
    return x


def right(x, d):
    x = x[d:] + x[0:d]
    return x


def left(x, d):
    x = right(x, len(x) - d)
    return x[::-1]


def encode(plain):
    d = 24
    x = up(plain)
    x = right(x, d)
    x = down(x)
    x = left(x, d)
    return x


def decode(encoded):
    d = 24
    x = right(encoded, d)
    x = down(x)
    x = left(x, d)
    x = up_inv(x)
    return x


def main():
    print("What does this mean?")
    encoded = "1010000011111000101010101000001010100100110110001111111010001000100000101000111011000100101111011001100011011000101011001100100010011001110110001001000010001100101111001110010011001100"
    flag = decode(encoded)
    print(flag)


if __name__ == "__main__":
    main()
