# MAde By 20CE147 Rohit Thakkar

# PRAC AIM:Lapindrome is defined as a string which when split in the middle, 
# gives two halves having the same characters and same frequency of each character. 
# If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. 
# For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency.
# Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. 
# The two halves contain the same characters but their frequencies do not match. Your task is simple. 
# Given a string, you need to tell if it is a lapindrome. 

#REPO LINK: https://github.com/Rohit-Thakkar/python_assign_sem4/




test_cases = int(input())
a = []
for i in range(test_cases):
    
    trash=input()
    a.append(trash)
for i in range(len(a)):
    s = a[i]
    s1,s2='',''
    if(len(s)%2==0):
        s1=s[:len(s)//2] 
        s2=s[(len(s)//2):]
    else: 
        s1=s[:len(s)//2]
        s2=s[(len(s)//2+1):]
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()
    s1=str(l1)
    s2=str(l2)
    print(s1,s2)
    if(s1==s2):
        print('YES')
    else: 
        print('NO')
