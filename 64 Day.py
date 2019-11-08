# _________________ 64 Day _______________ #

#Python Try Except

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
    

#Python Try Except with else

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

    

#Python Try Except with finally

try:
    print(x)
except:
    print("Somthing went wrong")
finally:
    print("The 'try except' is finished")

    
