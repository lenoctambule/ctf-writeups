chall.pyc (Python 3.10)
[Code]
    File Name: /tmp/chall.py
    Object Name: <module>
    Arg Count: 0
    Pos Only Arg Count: 0
    KW Only Arg Count: 0
    Locals: 0
    Stack Size: 3
    Flags: 0x00000040 (CO_NOFREE)
    [Names]
        'input'
        'userInput'
        'key'
        'code'
        'print'
    [Var Names]
    [Free Vars]
    [Cell Vars]
    [Constants]
        [Code]
            File Name: /tmp/chall.py
            Object Name: <listcomp>
            Arg Count: 1
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Locals: 2
            Stack Size: 4
            Flags: 0x00000043 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)
            [Names]
                'ord'
            [Var Names]
                '.0'
                'e'
            [Free Vars]
            [Cell Vars]
            [Constants]
            [Disassembly]
                0       BUILD_LIST              0
                2       LOAD_FAST               0: .0
                4       FOR_ITER                6 (to 18)
                6       STORE_FAST              1: e
                8       LOAD_GLOBAL             0: ord
                10      LOAD_FAST               1: e
                12      CALL_FUNCTION           1
                14      LIST_APPEND             2
                16      JUMP_ABSOLUTE           2
                18      RETURN_VALUE            
        '<listcomp>'
        'Password:'
        'd1j#H(&Ja1_2 61fG&'
        [Code]
            File Name: /tmp/chall.py
            Object Name: code
            Arg Count: 1
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Locals: 3
            Stack Size: 6
            Flags: 0x00000043 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)
            [Names]
                'ord'
                'key'
                'len'
                'code'
            [Var Names]
                'l'
                'el'
                'rest'
            [Free Vars]
            [Cell Vars]
            [Constants]
                None
                1
                5
                0
            [Disassembly]
                0       LOAD_FAST               0: l
                2       DUP_TOP                 
                4       MATCH_SEQUENCE          
                6       POP_JUMP_IF_FALSE       33 (to 66)
                8       GET_LEN                 
                10      LOAD_CONST              1: 1
                12      COMPARE_OP              5 (>=)
                14      POP_JUMP_IF_FALSE       33 (to 66)
                16      UNPACK_EX               1
                18      STORE_FAST              1: el
                20      STORE_FAST              2: rest
                22      POP_TOP                 
                24      LOAD_CONST              2: 5
                26      LOAD_FAST               1: el
                28      BINARY_MULTIPLY         
                30      LOAD_GLOBAL             0: ord
                32      LOAD_GLOBAL             1: key
                34      LOAD_GLOBAL             2: len
                36      LOAD_FAST               2: rest
                38      CALL_FUNCTION           1
                40      LOAD_GLOBAL             2: len
                42      LOAD_GLOBAL             1: key
                44      CALL_FUNCTION           1
                46      BINARY_MODULO           
                48      BINARY_SUBSCR           
                50      CALL_FUNCTION           1
                52      BINARY_XOR              
                54      BUILD_LIST              1
                56      LOAD_GLOBAL             3: code
                58      LOAD_FAST               2: rest
                60      CALL_FUNCTION           1
                62      BINARY_ADD              
                64      RETURN_VALUE            
                66      POP_TOP                 
                68      MATCH_SEQUENCE          
                70      POP_JUMP_IF_FALSE       43 (to 86)
                72      GET_LEN                 
                74      LOAD_CONST              3: 0
                76      COMPARE_OP              2 (==)
                78      POP_JUMP_IF_FALSE       43 (to 86)
                80      POP_TOP                 
                82      BUILD_LIST              0
                84      RETURN_VALUE            
                86      POP_TOP                 
                88      LOAD_CONST              0: None
                90      RETURN_VALUE            
        'code'
        (
            292
            194
            347
            382
            453
            276
            577
            434
            183
            295
            318
            196
            482
            325
            412
            502
            396
            402
            328
            194
            473
            490
            299
            503
            386
            215
            263
            211
            318
            206
            533
        )
        'Bravo!'
        'Dommage...'
        None
    [Disassembly]
        0       LOAD_CONST              0: <CODE> <listcomp>
        2       LOAD_CONST              1: '<listcomp>'
        4       MAKE_FUNCTION           0
        6       LOAD_NAME               0: input
        8       LOAD_CONST              2: 'Password:'
        10      CALL_FUNCTION           1
        12      GET_ITER                
        14      CALL_FUNCTION           1
        16      STORE_NAME              1: userInput
        18      LOAD_CONST              3: 'd1j#H(&Ja1_2 61fG&'
        20      STORE_NAME              2: key
        22      LOAD_CONST              4: <CODE> code
        24      LOAD_CONST              5: 'code'
        26      MAKE_FUNCTION           0
        28      STORE_NAME              3: code
        30      LOAD_NAME               3: code
        32      LOAD_NAME               1: userInput
        34      CALL_FUNCTION           1
        36      BUILD_LIST              0
        38      LOAD_CONST              6: (292, 194, 347, 382, 453, 276, 577, 434, 183, 295, 318, 196, 482, 325, 412, 502, 396, 402, 328, 194, 473, 490, 299, 503, 386, 215, 263, 211, 318, 206, 533)
        40      LIST_EXTEND             1
        42      COMPARE_OP              2 (==)
        44      POP_JUMP_IF_FALSE       29 (to 58)
        46      LOAD_NAME               4: print
        48      LOAD_CONST              7: 'Bravo!'
        50      CALL_FUNCTION           1
        52      POP_TOP                 
        54      LOAD_CONST              9: None
        56      RETURN_VALUE            
        58      LOAD_NAME               4: print
        60      LOAD_CONST              8: 'Dommage...'
        62      CALL_FUNCTION           1
        64      POP_TOP                 
        66      LOAD_CONST              9: None
        68      RETURN_VALUE            
