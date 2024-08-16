# add your code here
#Write a Python program that encrypts text given by the user. The program should 
#ask the user for a plain text sentence and print the encrypted text. The text 
#should be encrypted using a caesar cipher with a right shift of 5.

#Here is an example execution of the program:


#Please enter a senctence: python is fun!
#The encrypted sentence is: udymts nx kzs!

#initialize alphabet list to check against
upperalphachr = []
loweralphachr = []

#initialize encoded alphabet list to output
encsentlist = []

#populate alphabetlists
for i in range(65,91):
    upperalphachr.append(chr(i))
for i in range(97,123):
    loweralphachr.append(chr(i))

#input
sentence = input("Please enter a sentence:")
for char in sentence:
    if char in upperalphachr:
                char_index = upperalphachr.index(char)
                encpos = (char_index + 5) % 26
                encletter = upperalphachr[encpos]
                encsentlist.append(encletter)
    elif char in loweralphachr:
                char_index = loweralphachr.index(char)
                encpos = (char_index + 5) % 26
                encletter = loweralphachr[encpos]
                encsentlist.append(encletter)
                print(sentence)
                print(''.join(encsentlist))
    else:
                encsentlist.append(char)


print(sentence)
print(''.join(encsentlist))





