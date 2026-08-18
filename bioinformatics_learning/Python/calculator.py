num1 = float(input("请输入第一个数字："))
op = input("请输入运算符：")
num2 = float(input("请输入第二个数字："))
if op == "+":
    res = num1 + num2
elif op == "-":
    res = num1 - num2
elif op == "*":
    res = num1 * num2
elif op == "/":
    if num2 != 0 :
     res = num1 / num2
    else:
        res = "不能除以0"
else :
    res = "未知运算符"
print(f"结果：{num1}{op}{num2} = {res}")
