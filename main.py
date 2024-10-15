import math
from pydoc import plain

alphabet = "abcdefghijklmnopqrstuvwxyz"
square = []
for i in range(26):
	square.append([])
	for i2 in range(26):
		square[i].append(int(math.fmod(i2+i, 26)))

def vigenere_sq():
	for x in range(len(alphabet)):
		for y in range(len(alphabet)):
			character = " "*4
			if x != 0 and y != 0:
				character = f"{alphabet[square[x - 1][y - 1]]}"
			elif y == 0:
				character = (" "+alphabet)[x] + " "
			elif x == 0:
				character = (" "+alphabet)[y] + " "
			print(f"| {character} ", end="")
		print()

def letter_to_index(letter, alphabet):
	return alphabet.index(letter)

def index_to_letter(index, alphabet):
	return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
	return (letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % 26

def vigenere_letter(key_letter, plaintext_letter, alphabet):
	row = letter_to_index(plaintext_letter, alphabet)
	col = letter_to_index(key_letter, alphabet)
	return int(square[row][col])

def encrypt_vigenere(key, plaintext, alphabet):
	i = 0
	while len(key) < len(plaintext):
		key += key[i]
		i += 1
	#print(key)
	#print(plaintext)
	result = ""
	for i in range(len(plaintext)):
		if plaintext[i] == " ":
			result += " "
		else:
			result += alphabet[vigenere_index(key[i], plaintext[i], alphabet)]
	return result

def decrypt_vigenere(key, ciphertext, alphabet):
	i = 0
	while len(key) < len(ciphertext):
		key += key[i]
		i += 1

	result = ""
	for index in range(len(ciphertext)):
		if ciphertext[index] == " ":
			result += " "
		else:
			result += index_to_letter(letter_to_index(ciphertext[index], alphabet) - letter_to_index(key[index], alphabet), alphabet)
	return result

key = "messwiththebestdieliketherest"



#vigenere_sq()

while True:
	action = input("Would you like to encrypt, decrypt, or quit?? (1/encrypt) (2/decrypt) (3/quit): ").strip()
	if action == "encrypt":
		action = 1
	elif action == "decrypt":
		action = 2
	elif action in ["quit", "3"]:
		break
	elif action in ["1","2"]:
		action = int(action)
	else:
		action = 4 #Incorrect input
		print("Invalid selection! Please try again")

	if action != 4:
		key = input("What is the key for the message?: ")
		if action == 1:
			res = encrypt_vigenere(key, input("What plaintext would you like to encrypt?: "), alphabet)
		elif action == 2:
			res = decrypt_vigenere(key, input("What ciphertext would you like to decrypt?: "), alphabet)
		else:
			print("I have no clue what you did, but something's screwed up.")
		print(f"\nResult: {res}\n")