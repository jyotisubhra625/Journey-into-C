#Write a python pogram to translate a message into a secret code language.
#Use the rules below to translate normal English into secrete code language.

# Coding: 

# if the word contains atleast 3 characters,remove the first letter and append it at the end.
# now append three random characters at the starting and the end.
# else: 
# simply reverse the string

# Decoding

#if the word contains less than 3 characters ,reverse it. 
# else : 
# remove 3 random character from start and end and low remove the last letter and append it to the beginning

'''                                                  ***POGRAM***                                              '''
import random

def encoding(string):
    words = string.split()      #here words is a list
    encoded_words = []
    for word in words:
        if len(word) > 2:
            new_word = word[1:] + word[0]
            # first 3 random characters
            f1 = ""
            f2 = ""
            for _ in range(3):
                alphabet = random.choice("abcdefghijklmnopqrstuvwxyz")
                f1 = f1 + alphabet
            # last 3 random characters
                f2 = f2 + alphabet
            new_word = f1 + new_word + f2
        else:
            new_word = word[::-1]
        encoded_words.append(new_word)
    encoded_string = ""
    for word in encoded_words:
        encoded_string = encoded_string + word + " "
    return encoded_string



def decoding(string):
    words=string.split()
    decoded_words=[]
    for word in words :
        if len(word)>2:
            new_word=word[3:-3]
            new_word=new_word[-1]+new_word[:-1]
        elif len(word)<3 :
            new_word=word[::-1]
        decoded_words.append(new_word)
        decoded_string=""
        for word in decoded_words:
            decoded_string=decoded_string + word + " "
    return decoded_string
    
while True:
 c=input("The code word is : ")
 if(c=="quit"):
     break
 string = input("Enter a string: ")
 if(c=="code"):
    encoded_string = encoding(string)
    print("Encoded string:", encoded_string)
 elif(c=="decode"):
    decoded_string = decoding(string)
    print("Decoded string:", decoded_string)
 else:
    print("Invalid code word ! Try Again ")
    