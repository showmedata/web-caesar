import string

def alphabet_position(letter):
    alphabet = string.ascii_lowercase
    let = letter.lower()
    idx = 0
    for pos in range(len(alphabet)):
        if let == alphabet[pos]:
            idx = pos
    return idx

def rotate_character(char, rot):
    if char.isalpha() != True:
        return char
    case = ''
    if char in string.ascii_lowercase:
        case = 'lower'
    else:
        case = 'upper'
    idx = alphabet_position(char)
    new_idx = 0
    new_idx = (idx + (rot % 26)) % 26
    alphabet = string.ascii_lowercase
    new_char = alphabet[new_idx]
    if case == 'lower':
        return new_char
    else:
        new_char = new_char.upper()
    return new_char

def encrypt(text, rot):
    new_text = ''
    for char in text:
        new_text = new_text + rotate_character(char, rot)
    return new_text
