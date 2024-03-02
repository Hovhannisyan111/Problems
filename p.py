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

#15. Գրել ֆունկցիա, որը որպես արգումենտ կստանա թիվ և կստուգի պոլինդրոմ է այն, թե ոչ։
#def polindrome(n):
##    return str(n) == str(n)[::-1]
#    tmp = n
#    x = 0
#    while n > 0:
#        num = n%10
#        x = x*10 + num
#        n = n//10
#    if tmp == x:
#        return "Palindrome"
#    else:
#        return "It's not"
#print(polindrome(12121))
#print(polindrome(123))

#16․ Գրել ֆունկցիա, որը որպես արգումենտ կստանա թիվ և կվերադարձնի իրենամենամոտ պոլինդրոմ թիվը։




#17.Գրել ֆունկցիա որը, որպես արգումենտ կստանա թիվ և կվերադարձնի իր առաջին և վերջին թվանշանների արտադրյալը։
#def my(number):
#    last = number %10
#
#    while number > 10: 
#        number = number //10
#    first = number
#    return first * last
#print(my(743))

#18. Գրել ֆունկցիա որը որպես արգումենտ կստանաիստ և կվերադարձնի լիստում եղած տողերի քանակությունը
#def my_len(ml):
#    return len(ml)
#ml = [1,2,3,4,5,6,7]
#print(my_len(ml))

#19.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա թվերից առավելագույնը։
#def my_max(ml):
#    return max(ml)
#ml = [2,5,8,1,3]
#print(my_max(ml))

#20. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա երկնիշ զույգ թվերը։
#def even(ml):
#    ms = []
#    for i in ml:
#        if 10 <= i < 100 and i%2 == 0:
#            ms.append(i)
#    return(ms)
#ml = [5,12,56,65,77,1234,22,]
#print(even(ml))

#21. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա թվերի միջին թվաբանականը։
#def average(ml):
#    return sum(ml) // len(ml)
#ml = [1,2,6,89,34,345]
#print(average(ml))

#22.Գրել ֆունկցիա որը որպես առգումենտ կստանա տողերի լիստ և կվերադարձնի այդ տողերի երկարությունները պարունակող լիստ    
#def list_len(ml):
#    ms = []
#    for i in ml:
#        ms.append(len(i))
#    return ms
#ml = ["Apple","hello","good","end"]
#print(list_len(ml))

#23. ,Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա թվերը դասավորված նվազման կարգով։
#def my(ml):
#    ms = []
#    for i in ml:
#        if str(i).isdigit():
#            ms.append(i)
#    ms.sort()
#    ms.reverse()
#    return ms
#
#ml = ["Apple", 77, 11, 87, 12, "good"]
#print(my(ml))

#24. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնիլիստում առկա տողերը դասավորված երկարությունների նվազման կարգով։
#def my_len(ml):
#    ms = []
#    for i in ml:
#        if str(i).isalpha():
#            ms.append(len(i))
#    ms.sort()
#    ms.reverse()
#    return(ms)
#ml = ["Apple", 55, "my", "four", 90, "Python"]
#print(my_len(ml))

#25.Գրել ֆունկցիա որը որպես արգումենտ կընդունի կընդունի տողերի լիստ,ևկվերադարձնի այն բառը որը կպարունակի ամենաշատ ձայնավորները։
#def my(ml):
#    def my_vowels(n):
#        vowels = "aeuioy"
#        return sum(1 for i in n if i.lower() in vowels)
#    max_vowels = ""
#    max_count = 0
#    for i in ml:
#        vowels_count = my_vowels(i)
#        if vowels_count > max_count:
#            max_vowels = i
#            max_count = vowels_count
#    return max_vowels
#    
#ml = ["Hello","good","world","Python","banana"]
#print(my(ml))

#26. ,Գրել ֆունկցիա որը որպես արգումենտ կընդունի նախադասությունների ,լիստ և կվերադարձնի այն նախադասությունը որը կպարունակի ամենաշատ բառեր։
#def max_word(ml):
#    max_sentence = ""
#    max_count = 0
#
#    for sentence in ml:
#        words = sentence.split()
#        word_count = len(words)
#        if word_count > max_count:
#            max_sentence = sentence
#            max_count = word_count
#
#    return max_sentence
#ml = [
#        "a set of words that is complete in itself",
#        "typically containing a subject and predicate",
#        "conveying a statement",
#        "question, exclamation, or command",
#        "(This has the most) and sometimes one or more subordinate."
#    ]
#print(max_word(ml))

#27․ Գրել ֆունկցիա որը որպես արգումենտ կստանա տող /իրականում նախադասություն/ և կվերադարձնի այդ նախադասությունում առկա ամենամեծ թիվը /ոչ թե թվանշանը/ ։
#def max_num(mstr):
##   return max(int(i) for i in mstr.split() if i.isdigit())
#    ms = mstr.split()
#    num = 0
#    for i in ms:
#        if str(i).isdigit() and int(i) > num:
#            num = int(i) 
#    return num
#print(max_num(input("Enter: ")))

#28․ Գրել ֆունկցիա, որը որպես արգումենտ կստանա բառարանների լիստ՝ մարդկանց նկարագրող, և կվերադարձնի այն բառարանը, որում մարդու տարիքն ամենամեծն է։
#def age(ml):
#    max_age = 0
#    oldest = ""
#    for i in ml:
#        age = i.get("age",0)
#        if age > max_age:
#            max_age = age
#            oldest = i
#    return oldest
#    
#ml = [
#        {'name': 'Bob',
#         'job': 'Unemployed',
#         'age': 55
#            },
#        {'name': 'Joe',
#         'job': 'President',
#         'age': 77
#            },
#        {'name': 'Jack',
#         'job': 'Engineer',
#         'age': 45
#            }
#        ]
#print(age(ml))

#29. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ ուսանողների նկարագրող և կվերադարձնի այդ ուսանողների լիստը դասավորված աճման կարգով՝ ըստ միասվորների։
#def sort(ml):
#    return sorted(ml, key=lambda x: x["xp"])
#
#ml = [
#        {"name": "Bob",
#         "xp": 75
#         },
#         {"name": "Ann",
#         "xp": 95
#         },
#
#          {"name": "Jack",
#         "xp": 60
#         }
#
#        ]
#print(sort(ml))
        
#30. Գրել ֆունկցիա, որը որպես արգումենտ կստանա բառարանների լիստ՝ համալսարանների նկարագրող և կվերադարձնի այն համալսարանը, որի անվանումն ամենաերկարն է
#def longest(ml):
#    max_length = 0
#    long_name = ""
#    for i in ml:
#        name = i.get("name","")
#        if len(name) > max_length:
#            max_length = len(name)
#            long_name = name 
#    return long_name
#universities = [
#        {"name": "Cambrigde"},
#        {"name": "Oxford"},
#        {"name": "National Polytechnic University of Armenia"},
#        {"name": "Harvard"}
#]
#print(longest(universities))
            

































