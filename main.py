# Global variables
possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
initialPosition = 0
shiftedPosition = 0
shiftedMessage = ""

# Define the function called encryptOrDecrypt

# Define the function called wraparound

# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: " + possibleCharacters + "\n\nLet's get started!|n")

# Receive user input
initialMessage = input("What is your message? ")
key = int(input("What is the key? Choose a number from 0 to 93. "))
mode = input("Do you want to encrypt or decrypt? ")

# Encrypt or decrypt the message
for character in initialMessage:
    if character in possibleCharacters:
        initialPosition = possibleCharacters.find(character)

        if mode.lower() == "encrypt":