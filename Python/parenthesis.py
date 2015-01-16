def check(s):
    stack = []
    for char in s:
        if(char == "("):
            stack.append(char)
        elif(char == ")"):
            if(stack == []):
                return False
            else:
                stack.pop()

    return True if stack == [] else False


a = "(234234) + (123(sivan))"
b = "( (a)(b) ) (s) )"
                 #  ^ odd one out
c = "assert(elem_equal_fn(ht_lookup(buster, ted)->board, ted));"

print check(a) # True
print check(b) # False
print check(a[:3]) # False
print check(c)