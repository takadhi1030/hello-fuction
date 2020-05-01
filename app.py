def hello():
    print("Hello World")
# 引数もなくて返り値もない

hello()


def say_hello(name):
    print(f"Hi {name} ")



say_hello("Bob")
# 引数はあって、返り値はない

def double(number):
    return 2 * number


result_1 = double(3)
print(result_1)
# 引数も返り値もある

# 1分課題
def str_combine(str1, str2):
    return str1 + str2


result = str_combine("Kazuma", "Takahashi")
print(result)
pass

str_combine("Kazuma", "Takahashi")  # "Kazuma Tkahashi"を返す
