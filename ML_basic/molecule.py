def isNumber(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def molecule(letters):
    upper=[ord('A')<=ord(x) and ord(x) <=ord('Z') for x in letters]
    lower=[ord('a')<=ord(x) and ord(x) <=ord('b') for x in letters]
    number=[isNumber(x) for x in letters]

    #for i in upper:

    #print(result)
molecule('CO12')

def molecule2(letters):
    string = letters
    ans = string[0]
    numlist = []
    for idx, char in enumerate(string[1:]):
        print(idx,char)
        print(string[idx],char)
        if string[idx].islower() and char.isupper():
            ans += '-'
        elif string[idx].isupper() and char.isupper():
            ans += '-'
        elif string[idx].isupper() and char.isnumeric():
            ans += '-'
        elif char.isnumeric():
            numlist.append(char)
        ans += char
    print(ans)
    anslst = ans.split('-')[:-1]
    numlist = [i for i in ans.split('-')[-1]]
    print(anslst)
    print(numlist)
    if len(anslst) != len(numlist):
        print('error')
    else:
        lst = list(zip(anslst, numlist))
        lst2 = []
        for i in lst:
            lst2.append(i[0] + i[1])
        sum = ''
        for i in lst2:
            sum += i
        sum = sum.replace('1', '')
        print(sum)

molecule2('COACl1234')