__author__ = 'jc437345'


vowel=['a', 'e', 'i', 'o', 'u']
vowel_count = 0
name=input('enter the name')

for i in name:

    if i.lower() in vowel:
        vowel_count += 1
#print (vowel_count)
print ('out of {} letters, {} has {} vowels'.format(len(name), name, vowel_count))
