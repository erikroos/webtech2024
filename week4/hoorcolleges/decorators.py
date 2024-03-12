# Decoration m.b.v. een annotation (@)

def wrapper_func(f):
    def wrapper():
        print("Some preprocessing")
        f()
        print("Some postprocessing\n")
    return wrapper

@wrapper_func
def wrapped_func():
    print("Output from original function")

wrapped_func()

# Wat dit eigenlijk doet:

def wrapper_func2(f):
    def wrapper():
        print("Some preprocessing")
        f()
        print("Some postprocessing\n")
    return wrapper

def wrapped_func2():
    print("Output from original function")

wrapped_func2 = wrapper_func2(wrapped_func2) # dit is wat die annotatie doet

wrapped_func2()