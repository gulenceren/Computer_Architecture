print("""
    -----------------------------------------------------------------------------
    x  y  |  F0  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12  F13  F14  F15
    -----------------------------------------------------------------------------
    0  0  |  0   0   0   0   0   0   0   0   1   1    1    1    1    1    1    1
    0  1  |  0   0   0   0   1   1   1   1   0   0    0    0    1    1    1    1
    1  0  |  0   0   1   1   0   0   1   1   0   0    1    1    0    0    1    1
    1  1  |  0   1   0   1   0   1   0   1   0   1    0    1    0    1    0    1
""")
girdi=input("Which Boolean Function Will You Operate?")
if girdi == "f0"  or girdi=="F0":
    print("The result is 0 for all x y values.")
elif girdi == "f1"  or girdi=="F1":
    x=0;y=0
    ve=x*y
    print("x={} y={} result for values={}".format(x,y,ve))
    x = 0;y = 1
    ve = x * y
    print("x={} y={} result for values={}".format(x, y, ve))
    x = 1;y = 0
    ve = x * y
    print("x={} y={} result for values={}".format(x, y, ve))
    x = 1;y = 1
    ve = x * y
    print("x={} y={} result for values={}".format(x, y, ve))
elif girdi == "f2"  or girdi=="F2":
    x = 0; y = 0 ;b=y
    if b==0:
        b=1
    ve = x * b
    o=ve
    print("x={} y={} result for values={}".format(x, y, ve))
    x = 0;y = 1;b=y
    if b == 1:
        b = 0
    ve = x * b
    p=ve
    print("x={} y={} result for values={}".format(x, y, ve))
    x = 1;y = 0;b=y
    if b==0:
        b=1
    ve = x * b
    r=ve
    print("x={} y={} result for values={}".format(x, y, ve))
    x = 1;y = 1;b=y
    if b == 1:
        b = 0
    ve = x * b
    s=ve
    print("x={} y={} result for values={}".format(x, y, ve))
elif girdi=="f3" or girdi=="F3":
    x = 0;y = 0
    print("x={} y={} result for values={}".format(x, y, x))
    x = 0;y = 1
    print("x={} y={} result for values={}".format(x, y, x))
    x = 1;y = 0
    print("x={} y={} result for values={}".format(x, y, x))
    x = 1;y = 1
    print("x={} y={} result for values={}".format(x, y, x))
elif girdi == "f4"  or girdi=="F4":
    x = 0;b = x;y = 0
    if b == 0:
        b = 1
    ve = b * y
    print("x={} y={} result for values={}".format(x, y, ve))
    x = 0;b = x;y = 1
    if b == 0:
        b = 1
    ve = b * y
    print("x={} y={} result for values={}".format(x, y, ve))
    x = 1;b = x;y = 0
    if b == 1:
        b = 0
    ve = b * y
    print("x={} y={} result for values={}".format(x, y, ve))
    x = 1;b = x;y = 1
    if b == 1:
        b = 0
    ve = b * y
    print("x={} y={} result for values={}".format(x, y, ve))
elif girdi=="f5" or girdi=="F5":
    x = 0;y = 0
    print("x={} y={} result for values={}".format(x, y, y))
    x = 0;y = 1
    print("x={} y={} result for values={}".format(x, y, y))
    x = 1;y = 0
    print("x={} y={} result for values={}".format(x, y, y))
    x = 1;y = 1
    print("x={} y={} result for values={}".format(x, y, y))
elif girdi=="f6" or girdi=="F6":
    x = 0;b = x;y = 0 ;c=y
    if b == 0:
        b = 1
    ve = b * y
    if c== 0:
        c = 1
    ve1 = x * c
    print("x={} y={} result for values={}".format(x, y, ve + ve1))
    x = 0;b = x;y = 1;c = y
    if b == 0:
        b = 1
    ve = b * y
    if c == 1:
        c = 0
    ve1 = x * c
    print("x={} y={} result for values={}".format(x, y, ve + ve1))
    x = 1;b = x;y = 0;c=y
    if b == 1:
        b = 0
    ve = b * y
    if c == 0:
        c = 1
    ve1 = x * c
    print("x={} y={} result for values={}".format(x, y, ve + ve1))
    x = 1;b = x;y = 1;c=y
    if b == 1:
        b = 0
    ve = b * y
    if c == 1:
        c = 0
    ve1 = x * c
    print("x={} y={} result for values={}".format(x, y, ve+ ve1))
elif girdi == "f7"  or girdi=="F7":
    x=0;y=0
    veya=x + y
    print("x={} y={} result for values={}".format(x,y,veya))
    x = 0;y = 1
    veya = x + y
    print("x={} y={} result for values={}".format(x, y, veya))
    x = 1;y = 0
    veya = x + y
    print("x={} y={} result for values={}".format(x, y, veya))
    x = 1;y = 1
    veya = x + y
    if veya == 2:
        veya=1
    print("x={} y={} result for values={}".format(x, y, veya))
elif girdi == "f8"  or girdi=="F8":
    x=0;y=0
    veya=x + y
    if veya == 0:
        veya=1
    print("x={} y={} result for values={}".format(x,y,veya))
    x = 0;y = 1
    veya = x + y
    if veya == 1:
        veya=0
    print("x={} y={} result for values={}".format(x, y, veya))
    x = 1;y = 0
    veya = x + y
    if veya == 1:
        veya = 0
    print("x={} y={} result for values={}".format(x, y, veya))
    x = 1;y = 1
    veya = x + y
    if veya == 2:
        veya=1
    if veya == 1:
        veya = 0
    print("x={} y={} result for values={}".format(x, y, veya))
elif girdi=="f9" or girdi=="F9":
    x = 0;b = x;y = 0;c = y
    if b == 0:
        b = 1
    ve = b * y
    if c == 0:
        c = 1
    ve1 = x * c;m=ve+ve1
    if m == 0:
        m = 1
    print("x={} y={} result for values={}".format(x, y, m))
    x = 0;b = x;y = 1;c = y
    if b == 0:
        b = 1
    ve = b * y
    if c == 1:
        c = 0
    ve1 = x * c ;m=ve+ve1
    if m==1:
        m=0
    print("x={} y={} result for values={}".format(x, y, m))
    x = 1; b = x;y = 0;c = y
    if b == 1:
        b = 0
    ve = b * y
    if c == 0:
        c = 1
    ve1 = x * c;m=ve+ve1
    if m == 1:
        m = 0
    print("x={} y={} result for values={}".format(x, y, m))
    x = 1;b = x; y = 1; c = y
    if b == 1:
        b = 0
    ve = b * y
    if c == 1:
        c = 0
    ve1 = x * c;m=ve+ve1
    if m == 0:
        m = 1
    print("x={} y={} result for values={}".format(x, y, m))
elif girdi=="f10" or girdi=="F10":
    x = 0;y = 0;b=y
    if b==0:
        b=1
    print("x={} y={} result for values={}".format(x, y, b))
    x = 0;y = 1;b=y
    if b==1:
        b=0
    print("x={} y={} result for values={}".format(x, y, b))
    x = 1;y = 0;b=y
    if b==0:
        b=1
    print("x={} y={} result for values={}".format(x, y, b))
    x = 1;y = 1;b=y
    if b==1:
        b=0
    print("x={} y={} result for values={}".format(x, y, b))
elif girdi == "f11"  or girdi=="F11":
    x = 0; y = 0 ;b=y
    if b==0:
        b=1
    veya = x + b
    print("x={} y={} result for values={}".format(x, y, veya))
    x = 0;y = 1;b=y
    if b == 1:
        b = 0
    veya = x + b
    print("x={} y={} result for values={}".format(x, y, veya))
    x = 1;y = 0;b=y
    if b==0:
        b=1
    veya = x + b
    if veya==2:
        veya=1
    print("x={} y={} result for values={}".format(x, y, veya))
    x = 1;y = 1;b=y
    if b == 1:
        b = 0
    veya = x + b
    print("x={} y={} result for values={}".format(x, y, veya))
elif girdi=="f12" or girdi=="F12":
    x = 0;y = 0;b=x
    if b==0:
        b=1
    print("x={} y={} result for values={}".format(x, y, b))
    x = 0;y = 1;b=x
    if b==0:
        b=1
    print("x={} y={} result for values={}".format(x, y, b))
    x = 1;y = 0;b=x
    if b==1:
        b=0
    print("x={} y={} result for values={}".format(x, y, b))
    x = 1;y = 1;b=x
    if b==1:
        b=0
    print("x={} y={} result for values={}".format(x, y, b))
elif girdi == "f13"  or girdi=="F13":
    x = 0; y = 0 ;b=x
    if b==0:
        b=1
    veya = b + y
    print("x={} y={} result for values={}".format(x, y, veya))
    x = 0;y = 1;b=x
    if b == 0:
        b = 1
    veya = b + y
    if veya==2:
        veya=1
    print("x={} y={} result for values={}".format(x, y, veya))
    x = 1;y = 0;b=x
    if b==1:
        b=0
    veya = b + y
    print("x={} y={} result for values={}".format(x, y, veya))
    x = 1;y = 1;b=x
    if b == 1:
        b = 0
    veya = b + y
    print("x={} y={} result for values={}".format(x, y, veya))
elif girdi == "f14"  or girdi=="F14":
    x=0;y=0
    ve = x * y
    if ve == 0 :
        ve = 1
    print("x={} y={} result for values={}".format(x,y,ve))
    x = 0;y = 1
    ve = x * y
    if ve == 0 :
        ve = 1
    print("x={} y={} result for values={}".format(x, y, ve))
    x = 1;y = 0
    ve = x * y
    if ve == 0 :
        ve = 1
    print("x={} y={} result for values={}".format(x, y, ve))
    x = 1;y = 1
    ve = x * y
    if ve == 1 :
        ve = 0
    print("x={} y={} result for values={}".format(x, y, ve))
elif girdi=="f15" or girdi=="F15":
    print("Results for All x and y Values ​​are 1")
else:
    print("Please Enter the Correct Function Number!!!!")