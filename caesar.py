def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(letter.lower())

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        idx = (alphabet_position(char) + rot) % 26

        if char.islower():
            return alphabet[idx]
        else:
            return alphabet[idx].upper()
    else:
        return char

def rotate_string(text, rot):
    encrypt_text = ""
    for character in text:
        encrypt_text += rotate_character(character, rot)
    return encrypt_text