#
print("\n")
print("Let us assign & switch")
# Not very Python assignment;-)
va =1
vb = 2; vc = 3;
print("va is : ",va); print("vc is now : ",vc,"\n")

# Assignment in idiomatic Python
va, vb, vc = 4,5,6
print("va = ",va,"; vb = ", vb, "; vc = ",vc,".")

# switching 2 or more variables: the Python's way
va, vb, vc = vc, vb, va
print("And now, ve have switched the variables")
print("va is now : ",va,"; vb is now : ",vb, "; vc is now : ",vc,"\n")

