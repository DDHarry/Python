#
# switching 2 or more variables
va =1
vb = 2; vc = 3; # We can write many more ones
print("va : ",va)
print("vc : ",vc)

va, vb, vc = vc, va, vb
print("And now, ve have switched the variables")
print("va is now : ",va)
print("vc is now : ",vc)
