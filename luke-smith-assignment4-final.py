# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 22:22:08 2023

@author: lasmi
"""

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift
    
    def encrypt(self, message):
        cipher = [] #This will store the encrypted characters as they're created
        for letter in message:
            if letter.isalpha(): #Checks to make sure the letter is actually a letter 
                #Here we convert the letter to uppercase and add in the specified shift. 65 is added to get the value of the encrypted letter
                cipher.append(chr((ord(letter.upper()) + self.shift - 65) % 26 + 65))
            else: #If it's not a letter, add it to the cipher list anyway
                cipher.append(letter)
        return ''.join(cipher) #This joins the list into a single string and returns its value
    
    def decrypt(self, message):
        text = [] #Another empty list to store the now decryped letters
        for letter in message:
            if letter.isalpha(): #Checking again to see if the letter is actually a letter
                text.append(chr((ord(letter.upper()) - self.shift - 65) % 26 + 65)) #Same as above, but subtracting the specified shirt
            else:
                text.append(letter) #Again, if it's not a letter, add it over to the lsit
        return ''.join(text) #Joins the list into a single string and returns the now decrypted message

cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
coded = cipher.encrypt(message)
print("Secret: ", coded)
answer = cipher.decrypt(coded)
print("Message: ", answer)
