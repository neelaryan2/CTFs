def triple(eat):
    return str(int(eat) * 3)


def interleave(arg1, arg2):
    print(arg1, arg2)
    idx1 = 0
    idx2 = 0
    pointer = 0
    ret = ""
    while idx1 < len(arg1) and idx2 < len(arg2):
        if pointer % 3 == 0:
            ret += arg2[idx2]
            idx2 += 1
        else:
            ret += arg1[idx1]
            idx1 += 1
        pointer += 1
    return ret


def reverse(arg):
    return arg[::-1]


def eaT(eat):
    return triple(eat[:3]) + reverse(eat)


def Ate(eat):
    return "Eat9" + eat[:3]


def main(inp):
    if len(inp) == 9:
        if str.isdigit(inp[:3]) and str.isdigit(inp[7:]):
            check = interleave(eaT(inp), Ate(reverse(inp)))
            if check == "E10a23t9090t9ae0140":
                flag = "eaten_" + eat
                print("absolutely EATEN!!! IITB{" + flag + "}")
            else:
                print("thats not the answer. you formatted it fine tho, here's what you got\n>>", check)
        else:
            print("thats not the answer. bad format :(\
            \n(hint: 123abc456 is an example of good format)")
    else:
        print("thats not the answer. bad 3 :(")


print("what's the answer")
inp = input()
main(inp)
