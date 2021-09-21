import random
import string

def generate_input():
    for line in range(5):
        curline = []
        for i in range(264):
            cur = random.getrandbits(6)
            cur = "{0:06b}".format(cur)
            curline.append(cur)
        print(' '.join(curline), end='\r\n')


output = [879059547225600221, 71793452475485205, 1148698281253257227, 217070812329394967, 1085086090799284516, 4238685779263969, 1085311228075820020, 4486897510174167, 879257471590075933, 233062363111948053, 879310247956329413, 220620237942043428, 864704387274818528, 219564707018453810, 1080930139169943704, 284575531841633519, 1095289279840717921, 219827558966836273, 922164813414728577, 71789326353092547, 922970468266331303, 284624197914774733, 935887582569446640, 233341656386976839, 1095496211378261093, 270431259404009621, 922112088142040996, 271114274360574141, 936480455350027154, 14580558453485969, 1149315982842597017, 273649820165456770, 1134960775807159720, 69285389258153, 868979240123514018, 230541216188255296, 1148645726972267632, 72057336087430075, 1135966209599275106, 220398260916600638, 1152010064483073927, 271272397879702293, 1139343700758887558, 271077784355540943, 1139146754428701768, 4222399461461231, 922326496319573062, 283942073776672713, 1081923578845401015, 274442431825195106, 1097967845536444498, 16944574752682771, 935675805365747915, 67832102939014098, 1081920473329287448, 1073068336005587, 1081721748899955656, 55155024869773009, 918738451380057054, 274652781735887568, 918791227752582714, 270430592862047689, 922960640253902083, 17112864268238567, 878479842607955275, 229951587760733494, 881632416504951469, 1112495565767363, 882638470697435530, 17112815333330190, 1151848652045611600, 54057266045841968, 919582927853977200, 274441624099950113, 881860882925030709, 58476429884768707, 869190591810957703, 220606270746394268, 1138496186912600710, 288226252967132741, 1139407393294925175, 68609593282673765, 1095272117148061322, 68468771777351541, 935689876626275940, 287170512185785987, 1098877480162557621, 220452029779136139, 1138341911719821923, 287966424658087442, 933159088420617518, 57487952572330426, 1084466749241033436, 13735927918412192, 881805026941256233, 216450958350103112, 1135821692603413223, 284838396737815122, 1148422235162410505, 271130552259837474, 922972957682372071, 220675298603830864, 1139406530802367886, 18010259016859042, 879323443101908642, 284839262375919183, 1149490972761796781, 58493138394427981, 922182117624696644, 71780503401582160, 922129603001122379, 13464974967361, 918750881951576401, 57636189074621104, 882438342200737477, 233910087384579782, 882635416186125660, 288018432198980036, 882691507922931320, 229740485016616693, 1081778432842190433, 274504086948213472, 919012484050846377, 273870767986373374, 1098653128292552208, 17789823524785699, 936484823391600233, 288006061884174664, 1135755039810466391, 220610149264392545, 923026816572866165, 220673079782928545, 1084509890119794064, 57698195299630181, 1098597714352143950, 273662949817528928, 1084245170751013532, 233289910418682556, 1152868676445159022, 273861906596622869, 1152062995421196783, 16892006533755522, 878202962169560357, 219551526581911207, 1081712678517132855, 54901075530993324, 1138351810784785110, 287368617589457513, 918959449055625535, 68663387948777742, 864744991438602546, 17789270218755452, 879100224243548756, 18010272116257113, 879323430003683923, 284839275073057464, 935837243715555216, 233127265157825173, 1098822166335471510, 284585233327522172, 1081089049280840078, 66190813938289, 1085311369869266603, 217017417431055728, 1085086103734386376, 4238672944955073, 868969548061077922, 230585125518176963, 1134964279694586486, 58532504927404773, 935903202292740735, 13788713532460788, 1098610032472277687, 273808907837424086, 1098611059250691362, 287170705462591839, 935904280600953359, 54953797377651428, 1081972437337034002, 3431352717032734, 882490899915869684, 217017478683823314, 1080880677300142569, 3395020505739494, 864760452650840824, 68399248252862156, 1152854450759479489, 72056508471328536, 1135967031275879667, 220398260878299005, 923237031130165425, 220461087109169122, 1081778639814733919, 54940658191577131, 1094599850818548609, 271327652553490220, 1080916961136738199, 229961702408703798, 868279998848633946, 54044282154139485, 879258544116612891, 284625063628717240, 879258296069853009, 284798865657302933, 1152867835705298073, 55168202888248452, 1138513488130130342, 287107984222384471, 1085089592271237237, 271274871827451557, 923224455449361838, 67817894327611560, 878469330928386996, 270483416669012830, 879274208876507235, 220675540129136812, 868980306940527370, 230594235130183793, 1094599899900607733, 217282137553960044, 1094652833283493100, 283796252737158241, 878482303020224500, 270496420967206807, 1138513245732277422, 220675350747672793, 1085300646950993669, 14570660180524263, 1149279867130331935, 283727823485587214, 1135765772921798622, 55164714502340078, 919001518395568616, 14422035514995649, 919002553226628642, 270494089596571160, 1081075896199954192, 233909007654326019, 1081765291043638494, 3645104131685402, 881847842601189364, 287158284404650157, 933353496081530906, 288213815831556244, 868082087813444404, 71833031890124679, 882441640700022534, 233962879194169438, 1151852763148127243, 274455678322262261, 869181263355903934, 274442229753314412, 1135751534516958032, 71776131962646638, 932248434541314171, 229697655603511460, 1149491014637175127, 271063908134941100, 936537392976704440, 14636695302442350, 1098824639182863983, 216398129639732071, 1084469432518917257, 216177127761104710]

n = len(output)

seeds, randoms = [], []
for i in range(1, n + 1):
    seeds.append((i * 127) % 500)
    randoms.append((((i * 327) % 681) + 344) % 313)

for i in reversed(range(n - 1)):
    output[i + 1] ^= output[i]

for i in range(n):
    output[i] ^= randoms[i]


def scramble(block, seed):
    raw = ''.join(block)
    n = len(raw)
    ret = [None for i in range(n)]
    for i in range(n):
        idx = (i * seed) % n
        while ret[idx] is not None:
            idx = (idx + 1) % n
        ret[idx] = '11' if raw[i] == '1' else '00'
    return ''.join(ret)


def scramble_idx(seed):
    n = 30
    ret = [None for i in range(n)]
    for i in range(n):
        idx = (i * seed) % n
        while ret[idx] is not None:
            idx = (idx + 1) % n
        ret[idx] = i
    return ret


lines = [[] for i in range(5)]
for i, seed in enumerate(seeds):
    perm = scramble_idx(seed)
    cur = "{0:060b}".format(output[i])
    block = [None for j in range(30)]
    for j in range(0, 60, 2):
        c = cur[j:j + 2]
        assert c in ['11', '00']
        block[perm[j // 2]] = c[0]
    block = ''.join(block)
    for j in range(5):
        lines[j].append(block[6 * j:6 * j + 6])

for line in lines:
    cur = ''
    for w in line:
        c = chr(int(w, 2))
        # assert c in string.printable
        cur += c
    print(cur)

# for i in range(5):
# print(' '.join(lines[i]), end='\r\n')