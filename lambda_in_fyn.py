# 1
# def demo():
#     x=lambda a:a*5
#     print(x(2))
# demo()

def fun(n):
    return lambda a:a*n
mydemo=fun(3)
print(mydemo (4))