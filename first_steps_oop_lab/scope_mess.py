x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x  # changes x = "local" in outer()
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x  # changes x = "global" outside any func
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
