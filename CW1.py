alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']

# The various rotors sequence
rotor1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y',
        'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']

rotor2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M',
        'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']

rotor3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y',
        'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']

rotor4 = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X',
        'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']

rotor5 = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L',
        'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']

rotors_list = [rotor1, rotor2, rotor3, rotor4, rotor5]
rotors_notch_list = ["Q", "E", "V", "J", "Z"]

class PlugBoard:
    def __init__(self, pairs):
        #pairs : "AB CD EF HI JK" => ["AB","CD","EF","HI","JK"]
        self.pair_map = {}
        for pair in pairs.split():
            self.pair_map[pair[0]] = pair[1]
            self.pair_map[pair[1]] = pair[0]
    
    def swap_pairs(self, text):
        output = ""
        for letter in text:
            if self.pair_map.get(letter):
                output += self.pair_map[letter]
            else:
                output += letter
        return output

#keyboard = PlugBoard("AB CD EF HI JK")
#letters = "A DOG EATS CARROT"
#swapped_letters = keyboard.swap_pairs(letters)
#print("exited plugboard as: ", swapped_letters)

class Reflector:
    def __init__(self):
        self.reflector_list = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z',
        'C', 'W', 'V', 'J', 'A', 'T']
    reflector_dict = {"A": "Y", "Y": "A", "B": "R", "R": "B", "C": "U", "U": "C", "D": "H", "H": "D", "E": "Q", "Q": "E",
                "F": "S", "S": "F", "G": "L", "L": "G", "I": "P", "P": "I", "J": "X", "X": "J", "K": "N", "N": "K",
                "M": "O", "O": "M", "T": "Z", "Z": "T", "V": "W", "W": "V"}
    
    def reflect_pairs(self, letter):
        if letter in alphabet_list:
            return self.reflector_dict[letter]
        else:
            return letter

#keyboard = PlugBoard("AB CD EF HI JK")
#letters = "A DOG EATS CARROT"
#swapped_letters = keyboard.swap_pairs(letters)
#print("exited plugboard as: ", swapped_letters)
            #rotor logic
#my_reflector = Reflector()
#reflected_letters = ""
#for letter in swapped_letters:
    #reflected_letters += my_reflector.reflect_pairs(letter)
#print("exited reflector as: ", reflected_letters)

def caeser_shift(str, amount):
    output = ""
#Function to shift the rotor when a letter is entered
    for i in range(len(str)):
        c = str[i]
        code = ord(c)
        if (code >=65) and (code <=90):
            c = chr(((code-65+amount)%26)+65)
        output += c
    
    return output

class Rotor:
    def __init__(self, rotor_number, ring_settings,ring_position):
        self.rotor_list = rotors_list[rotor_number-1]
        self.rotor_notch = rotors_notch_list[rotor_number-1]
        self.rotor_letter = ring_position
        self.rotor_setting = ring_settings
        self.rotor_list = caeser_shift(self.rotor_list, alphabet_list.index(self.rotor_setting))
        self.offset = None
        self.set_offset()

    def set_offset(self):
        self.offset = alphabet_list.index(self.rotor_letter)

    def encrypt_letter(self, letter):
        index = alphabet_list.index(letter)
        index = (index + self.offset) % len(alphabet_list)
        temp = self.rotor_list[index]
        index = alphabet_list.index(temp)
        return alphabet_list[(index-self.offset+ len(alphabet_list)% len(alphabet_list))]

    def encrypt_letter_reverse(self, letter):
        index = alphabet_list.index(letter)
        index = (index + self.offset) % len(alphabet_list)
        temp = alphabet_list[index]
        index = self.rotor_list.index(temp)
        return alphabet_list[(index-self.offset+ len(alphabet_list)% len(alphabet_list))]


def encode(input_text):
    fast_rotor = Rotor(rotors[2],ring_settings[2],ring_positions[2])
    medium_rotor = Rotor(rotors[1],ring_settings[1],ring_positions[1])
    slow_rotor = Rotor(rotors[0],ring_settings[0],ring_positions[0])
    keyboard = PlugBoard("AB CD EF HI JK")
    reflector = Reflector()

    #plugboard swapping
    input_text = keyboard.swap_pairs(input_text)

    encoded_message = ""

    for letter in input_text:

        if letter in alphabet_list: 

            #Rotate, once I get a letter I rotate the rotor before encryption
            notch_found = False
            # fast rotor always rotates
            if fast_rotor.rotor_letter == fast_rotor.rotor_notch:
                notch_found = True
            fast_rotor.rotor_letter = alphabet_list[
                (alphabet_list.index(fast_rotor.rotor_letter) + 1) % len(alphabet_list)]
            # Check if medium needs to rotate
            if notch_found:
                notch_found = False
                if medium_rotor.rotor_letter == medium_rotor.rotor_notch:
                    notch_found = True
                medium_rotor.rotor_letter = alphabet_list[
                    (alphabet_list.index(medium_rotor.rotor_letter) + 1) % len(alphabet_list)]
                # Check if slow needs to rotate
                if notch_found:
                    notch_found = False
                    slow_rotor.rotor_letter = alphabet_list[
                        (alphabet_list.index(slow_rotor.rotor_letter) + 1) % len(alphabet_list)]
            else:
                # Check for double jump
                if medium_rotor.rotor_letter == medium_rotor.rotor_notch:
                    medium_rotor.rotor_letter = alphabet_list[(alphabet_list.index(medium_rotor.rotor_letter) + 1) % len(alphabet_list)]
                    slow_rotor.rotor_letter = alphabet_list[(alphabet_list.index(slow_rotor.rotor_letter) + 1) % len(alphabet_list)]
        
        # re sit the offset after the rotation
            fast_rotor.set_offset()
            medium_rotor.set_offset()
            slow_rotor.set_offset()

        # encrypt the letter through the three rotors in sequence
            letter = fast_rotor.encrypt_letter(letter)
            letter = medium_rotor.encrypt_letter(letter)
            letter = slow_rotor.encrypt_letter(letter)

        # reflector
            letter = reflector.reflect_pairs(letter)
        
        # reverse encrypt
            letter = slow_rotor.encrypt_letter_reverse(letter)
            letter = medium_rotor.encrypt_letter_reverse(letter)
            letter = fast_rotor.encrypt_letter_reverse(letter)

        encoded_message += letter

# plugboard swapping number 2
    encoded_message = keyboard.swap_pairs(encoded_message)

    return encoded_message

# main program:

rotors = [1, 2, 3]

while True:
    input_user = input("Enter rotor numbers in this sequence 'slow, medium, fast' : ").split(",")
    input_user = [x.strip() for x in input_user]
    if len(input_user) != 3:
        print("INVALID ROTOR NUMBERS!!")
        continue
    for i, rot in enumerate(input_user):
        if rot not in ("1", "2", "3", "4", "5"):
            print("INVALID ROTOR NUMBERS!!")
            continue
        rotors[i] = int(rot)
    break

ring_settings = "ABC"
while True:
    ring_settings = ""
    input_user = input("Enter ring settings(letter) in this sequence, 'slow, medium, fast', ex: 'A,B,C' : ").split(",")
    input_user = [x.strip() for x in input_user]
    if len(input_user) != 3:
        print("INVALID RING SETTINGS!!")
        continue
    for i, rot in enumerate(input_user):
        if rot not in alphabet_list:
            print("INVALID RING SETTINGS!!")
            continue
        ring_settings += rot
    break
ring_positions = "DEF"
while True:
    ring_positions = ""
    input_user = input("Enter ring positions(letter) in this sequence 'slow, medium, fast', ex: 'A,B,C' : ").split(",")
    input_user = [x.strip() for x in input_user]
    if len(input_user) != 3:
        print("INVALID RING POSITIONS!!")
        continue
    for i, rot in enumerate(input_user):
        if rot not in alphabet_list:
            print("INVALID RING POSITIONS!!")
            continue
        ring_positions += rot
    break

input_text = input("Enter text to encrypt/decrypt: ").upper().strip()

output = encode(input_text)
print("Encrypted message: ", output)

    







