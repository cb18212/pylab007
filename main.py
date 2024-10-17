import math
from argparse import Action
from pydoc import plain
from enum import Enum

from pyexpat.errors import messages

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
	if letter in alphabet:
		return alphabet.index(letter)
	else:
		return None

def index_to_letter(index, alphabet):
	return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
	return (letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % 26

# def vigenere_letter(key_letter, plaintext_letter, alphabet):
# 	row = letter_to_index(plaintext_letter, alphabet)
# 	col = letter_to_index(key_letter, alphabet)
# 	return int(square[row][col])

def encrypt_vigenere(key, plaintext, alphabet):
	i = 0
	while len(key) < len(plaintext):
		key += key[i]
		i += 1
	#print(key)
	#print(plaintext)
	result = []
	for i in range(len(plaintext)):
		if not plaintext[i] in alphabet:
			result += plaintext[i]
		else:
			result += alphabet[vigenere_index(key[i], plaintext[i], alphabet)]
	return"".join(result)

def decrypt_vigenere(key, ciphertext, alphabet):
	i = 0
	while len(key) < len(ciphertext):
		key += key[i]
		i += 1

	result = []
	for index in range(len(ciphertext)):
		if not ciphertext[index] in alphabet:
			result += ciphertext[index]
		else:
			result += index_to_letter(letter_to_index(ciphertext[index], alphabet) - letter_to_index(key[index], alphabet), alphabet)
	return "".join(result)

key = "messwiththebestdieliketherest"



#vigenere_sq()

class Actions(Enum):
	ENCRYPT = 1
	DECRYPT = 2
	DECRYPTSTASH = 3
	DUMPSTASH = 4
	CLEAR = 5
	QUIT = 6
	ERROR = 7

def check_com(inp):
	if inp.isdigit():
		return int(inp)
	for act in Actions:
		if inp.lower() == act.name.lower():
			return act.value
	return Actions.ERROR

def get_key():
	valid_key = False
	while not valid_key:
		valid_key = True
		key = input("What is the key for the message?: ")
		for i in key:
			if not i in alphabet:
				valid_key = False
				print("Keys can only contain letters")
				break
	return key

store = []

while True:
	action = input("Would you like to encrypt, decrypt, decrypt stash, print stored ciphertexts, clear the stash or quit?? (1/encrypt) (2/decrypt) (3/decryptstash) (4/dumpstash) (5/clear) (6/quit): ").strip()
	action = check_com(action)
	if action != Actions.ERROR:
		print(f"action: {action}")
		match action:
			case Actions.ENCRYPT.value:
				key = get_key()
				res = encrypt_vigenere(key, input("What plaintext would you like to encrypt?: "), alphabet)
				store.append([res, key])
				print(f"\nStored Result: {res}\n")
			case Actions.DECRYPT.value:
				key = get_key()
				res = decrypt_vigenere(key, input("What ciphertext would you like to decrypt?: "), alphabet)
				print(f"\nResult: {res}\n")
			case Actions.DECRYPTSTASH.value:
				print("Decrypting stored messages...")
				for pair in store:
					print(f"\nKey: {pair[1]}\nmessage: {decrypt_vigenere(pair[1], pair[0], alphabet)}")
				print()
			case Actions.DUMPSTASH.value:
				print("\nDisplaying stash...")
				for pair in store:
					print(f"Encrypted message: {pair[0]}")
				print()
			case Actions.CLEAR.value:
				print("Clearing ciphertext stash...\n")
				store = []
			case default:
				print("I have no clue what you did, but something's screwed up.")
	else:
		print("Invlid Input received, please select another option")