# Source Generated with Decompyle++
# File: dc_9111.pyc (Python 3.9)

    # [Disassembly]
    #     0       LOAD_CONST              0: '############################'
    #     2       STORE_NAME              0: flag
    #     4       LOAD_NAME               0: flag
    #     6       LOAD_CONST              1: None
    #     8       LOAD_CONST              1: None
    #     10      LOAD_CONST              2: -1
    #     12      BUILD_SLICE             3
    #     14      BINARY_SUBSCR
    #     16      STORE_NAME              1: a
    #     18      LOAD_CONST              3: '#######'
    #     20      STORE_NAME              2: key
    #     22      LOAD_NAME               3: len
    #     24      LOAD_NAME               2: key
    #     26      CALL_FUNCTION           1
    #     28      STORE_NAME              4: b
    #     30      LOAD_CONST              4: <CODE> <listcomp>
    #     32      LOAD_CONST              5: '<listcomp>'
    #     34      MAKE_FUNCTION           0
    #     36      LOAD_NAME               5: range
    #     38      LOAD_CONST              6: 0
    #     40      LOAD_NAME               3: len
    #     42      LOAD_NAME               1: a
    #     44      CALL_FUNCTION           1
    #     46      LOAD_NAME               4: b
    #     48      CALL_FUNCTION           3
    #     50      GET_ITER
    #     52      CALL_FUNCTION           1
    #     54      STORE_NAME              6: c
    #     56      LOAD_NAME               6: c
    #     58      GET_ITER
    #     60      FOR_ITER                46 (to 108)
    #     62      STORE_NAME              7: i
    #     64      LOAD_CONST              7: <CODE> <listcomp>
    #     66      LOAD_CONST              5: '<listcomp>'
    #     68      MAKE_FUNCTION           0
    #     70      LOAD_NAME               8: zip
    #     72      LOAD_NAME               2: key
    #     74      LOAD_NAME               7: i
    #     76      CALL_FUNCTION           2
    #     78      GET_ITER
    #     80      CALL_FUNCTION           1
    #     82      STORE_NAME              9: d
    #     84      LOAD_NAME               9: d
    #     86      GET_ITER
    #     88      FOR_ITER                16 (to 106)
    #     90      STORE_NAME              7: i
    #     92      LOAD_NAME               10: print
    #     94      LOAD_NAME               7: i
    #     96      LOAD_CONST              8: 10
    #     98      BINARY_ADD
    #     100     CALL_FUNCTION           1
    #     102     POP_TOP
    #     104     JUMP_ABSOLUTE           88
    #     106     JUMP_ABSOLUTE           60
    #     108     LOAD_CONST              1: None
    #     110     RETURN_VALUE

from dis import dis

def func():
	flag = '############################'
	a = flag[::-1]
	key = '#######'
	b = len(key)
	c = range(0, len(a), b)
	return

print(dis(func))

# flag = '############################'
# a = flag[::-1]
# key = '#######'
# b = len(key)
# c = (lambda .0: [ a[i:i + b] for i in .0 ])(range(0, len(a), b))