def fun1():
    print("fun1 start")
    fun2()
    print("fun1 end")

def fun2():
    print("fun2 start")
    fun3()
    print("fun2 end")

def fun3():
    print("fun3")

fun1()
