alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
'''
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
'''

def encrypt(original_text, shift_amount):
    encoded_text = ''
    for char in original_text:
        encoded_index_value = alphabet.index(char) + shift_amount
        encoded_index_value %= len(alphabet)
        encoded_text += alphabet[encoded_index_value]

    print(f"Here is the encoded result: {encoded_text}")

''' numeric_text_values = []
    encoded_text = ''
    for char in original_text:
        numeric_text_values.append((ord(char) + shift_amount))
    for value in numeric_text_values:
        encoded_text += (chr(value))

'''
encrypt("hello", 2)
