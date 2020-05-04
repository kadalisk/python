def f(s):
    print(s)

    # This program will NOT show error
    # if we comment below line.
    s = "Local Variable."

    print(s)


# Global scope
s = "Global Variable"
f(s)
print(s)
