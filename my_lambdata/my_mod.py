
# my_lambdata/my_mod.py

def enlarge(n):
    return n * 100

# print("JUNK")
# print("GLOBAL SCOPE")
#
# y = float(input("PLEASE INPUT A NUMBER TO ENLARGE: "))
# print(enlarge(y))

if __name__ == "__main__":
    # only if run from the command line, invoke the following code:
    # otherwise, don't

    print("JUNK")
    print("GLOBAL SCOPE")

    y = float(input("PLEASE INPUT A NUMBER TO ENLARGE: "))
    print(enlarge(y))
