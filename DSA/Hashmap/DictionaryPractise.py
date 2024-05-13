#Dictionary is a collections which are ordered, changeable, and do not allow duplicates.
#Dictionary elements have key and value pairs
number = 123523
numsCount={};

while number!=0:
    reminder = number%10

    if(numsCount.__contains__(reminder)):
        val = numsCount.get(reminder)
        val=val+1
        numsCount[reminder] = val
    else:
        numsCount[reminder]=1

    number = number//10
    print(f"reminder:{reminder},number:{number}, numcount: {numsCount}")


print(numsCount)

'''

dict ={"car": "tesla",
       "color":['blue','black'],
       "type": "autogear",
       "seater":5,
       "seater":8}
print("Before:")
print(dict) #no duplicates are allowed
dict["seater"]=10
print("After:")
print(dict)

'''




'''
x= dict["type"]
print(x)
dict["type"]="manual" 
print(dict)
dict["glass"]="black" #adding the keys
print(dict)  '''


def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    wordCount1 = {}  # dictionary set for pattern
    for word in pattern:
        if wordCount1.__contains__(word):
            count = wordCount1.get(word)
            count += 1
            wordCount1[word] = count
        else:
            wordCount1[word] = 1
    print(wordCount1)

    wordCount2 = {}  # dictionary set for s
    words = s.split()  # returns each words in a list
    for word in words:
        if wordCount2.__contains__(word):
            count = wordCount2.get(word)
            count += 1
            wordCount2[word] = count
        else:
            wordCount2[word] = 1
    print(wordCount2)


print(wordPattern("aaaa", "dog cat cat dog"))
