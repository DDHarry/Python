#
# switching 2 or more variables
va =1
vb = 2; vc = 3; # Not very Python ;-)

va, vb, vc = 4,5,6 # We can write many more ones
print("va = ",va, " vb = ", vb)
print("vc = ",vc)

va, vb, vc = vc, vb, va
print("And now, ve have switched the variables")
print("va is now : ",va)
print("vc is now : ",vc)
