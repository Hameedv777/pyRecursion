# It is used for iteration
def tr_recursion(k):
    if (k>0):
        result=k+tr_recursion(k-1)
        print(result)
    else:
        result=0;
    return result

print("Recursion Result")                
tr_recursion(7)