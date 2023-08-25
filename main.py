print("""For this test, we will use two variables called 'p' and 'q'.
Both values will be set to 'True'
""")
print("p = True")
p = True
print("q = True")
q = True

print("""
Below are De Morgan's Laws. Both of these comparisons should return as True,
however the second one returns as False.
""")
print("not (p and q) == (not p) or (not q)")
print(not (p and q) == (not p) or (not q))
print("not (p or q) == (not p) and (not q)")
print(not (p or q) == (not p) and (not q))

print("""
Breaking out the left and right segments and running the code on their own
shows that they are, in fact, both returning as False.
""")
print("not (p or q)")
print(not (p or q))
print("(not p) and (not q)")
print((not p) and (not q))

print("""
And we can confirm that False == False returns as True.
""")
print("False == False")
print(False == False)

print("""
So why does the comparison of these two segments return as False, not True?
""")
print("not (p or q) == (not p) and (not q)")
print(not (p or q) == (not p) and (not q))

print("""
To help make sense of this, I want to see what happens when the two segments
are assigned to variables then compared to one another.
""")
print("left = not (p or q)")
left = not (p or q)
print("right = (not p) and (not q)")
right = (not p) and (not q)
print("print(left)")
print(left)
print("print(right)")
print(right)
print("print(left == right)")
print(left == right)

print("""
As you can see, when each segment is assigned to a variable, the proper result
of the comparison is returned. The question now is what is taking place when
the two segments are compared to one another in their raw form that is causing
the logic to not behave as it should? Is this a bug in the Python code?
""")
