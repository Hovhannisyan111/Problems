#1 Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից թվերի գումարը։
#def my_sum(*args):
#    return sum(args)
#print(my_sum(4,6,7))
#print(my_sum(12,5,57,567,8,90))
#2. Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից տողերի քանակը։
#def my_len(x):
#    return len(x)
#print(my_len(input("Enter: ")))
#3. Գրել ֆունկցիա որը կվերադարձնի ստասած արգումենտների միջին թվաբանականը։
#def my_average(*args):
#    return sum(args) // len(args)
#print(my_average(5,5,7,7))
#4. Գրել ֆունկցիա որը կստանա արգումենտ և կվերադարձնի այդ արգումենտերի հետ կատարած մաթեմատիկական գործողությունների արդյունքները։
#def my_math(x,y,operation):
#    oper = {
#        "gumarum": lambda x,y: x+y,
#        "hanum": lambda x,y: x-y,
#        "bazmapatkum": lambda x,y: x*y,
#        "bajanum": lambda x,y: x//y
#    } 
#
#    results = {}
#    for i in operation:
#        if i in oper:
#           results[i] = oper[i](x,y)
#    return results
#print(my_math(15,5,operation=['gumarum', 'hanum', 'bazmapatkum', 'bajanum']))
#5. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի (upperայն դարձված ամբողջությամբ մեծատառ ֆունկցիան օգտագործել չի )կարելի 
#def my_upper(ms):
#    mstr = ""
#    for i in ms:
#        if 'a' <= i <= 'z':
#            mstr += chr(ord(i) - 32)
#        else:
#            mstr += i
#    return mstr
#        
#print(my_upper(input("Enter: ")))
#6. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի (lowerայն դարձված ամբողջությամբ փոքրատառ ֆունկցիան օգտագործել չի կարելի):
#def my_lower(mstr):
#    ms = ""
#    for i in mstr:
#        if 'A' <= i <= "Z":
#            ms += chr(ord(i) + 32)
#        else:
#            ms += i 
#    return ms 
#print(my_lower(input("Enter: ")))
#
#7.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված բոլոր բառերի առաջին տառերը մեծատառ (tittle ֆունկցիան օգտագործել չի կարելի )։
#def my_title(mstr):
#    ms = mstr.split()
#    new = [i[0].upper() + i[1:] for i in ms]
#    return " ".join(new)
#print(my_title(input("Enter: ")))   
#8. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված հակառակ։
#def reverse(mstr):
#    return mstr[::-1]
#print(reverse(input("Enter: ")))
#9.Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և 2 թիվ։ Այն պետք է վերադարձնի տրված 2 թվերի արանքում եղած ենթատողը։
#def my(mstr,x,y):
#    return mstr[x:y]
#print(my(input("Enter: "),int(input("Enter a number")),int(input("Enter a number:"))))
#10. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառը։
#def  my_max(mstr):
#    ms = mstr.split()
#    maxword = ""
#    for i in ms:
#        if len(i) > len(maxword):
#            maxword = i
#    return maxword
#print(my_max(input("Enter: ")))
#11. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաշատ օգտագործված տառը։
#def letter(mstr):
#    ms = "".join(i for i in mstr.lower() if i.isalpha())
#    count = 0
#    tar = ""
#    for i in ms:
#        if ms.count(i) > count:
#            count = ms.count(i)
#            tar = i 
#    return tar
#print(letter(input("Enter: "))) 
#12. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառում ամենաշատ օգտագործված տառը։
#def my_max(mstr):
#    ms = mstr.split()
#    mword = ""
#    for i  in ms:
#        if len(i) > len(mword):
#            mword = i
#   print(mword)
#    count = 0
#    tar = ""
#    for i in mword:
#        if mword.count(i) > count:
#            count = mword.count(i)
#            tar = i 
#    return tar 
#print(my_max(input("Enter: ")))
#13. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։ Կվերադարձնի այդ թվին համապատասխն ինդեքսում եղած էլէմենտները՝ սկզբից և վերջից։
#def my(mstr,n):
#    start = mstr[n] 
#    end = mstr[-n -1]
#    return start,end
#print(my(input("Enter: "),int(input("Enter a nuumber: "))))







