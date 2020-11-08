#温度转换
TempStr = input()
if TempStr[-1] in ["C","c"]:
    F = eval(TempStr[0:-1]) * 1.8 + 32
    print("{:.2f}F".format(F))
elif  TempStr[-1] in ["F","f"]:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("{:.2f}C".format(C))
else:
    print("输入格式错误")