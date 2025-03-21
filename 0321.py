a = [1, 2, 3]
b = a
c = a
b[1] = 6 # 僅改變 b 的 list 第 2 個元素
print(a, b, c)