x=10 # global variable 
def modify_global():
    global x   # Using the global x varibale inside the function 
    x=1        # x is a local variable 
    print(x)    
modify_global() 
