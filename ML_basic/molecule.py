def isNumber(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def make_sign(a,b):
    sign_dict={}

    #print(lower_index)
    #for i in range(0,len(a)):

def molecule(letters):
    upper=[ord('A')<=ord(x) and ord(x) <=ord('Z') for x in letters]
    lower=[ord('a')<=ord(x) and ord(x) <=ord('b') for x in letters]
    number=[isNumber(x) for x in letters]

    print(upper)
    print(lower)
    print(number)
    result=make_sign(upper,lower)
    print(result)
molecule('C2O')