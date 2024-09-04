def local_example():
    """
    This function demonstrates the usage of local variables.
    """
    a = [20,10,30]  # This is a local variable
    print("Local variable a =", a)

def global_example(a):
    # global a  # This is a global variable
    print("Global variable a =", a)


a = [20,10]
local_example()
local_example()
global_example(a)