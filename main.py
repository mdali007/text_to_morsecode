morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '0': '-----', '1': '.----', '2': '..---',
                   '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', ' ': '/'
                   }


def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char  # Keep non-alphanumeric characters as is
    return morse_code.strip()


# Example usage:
input_text = input("Enter text to convert to Morse code: ")
result = text_to_morse(input_text)
print("Morse Code:", result)
