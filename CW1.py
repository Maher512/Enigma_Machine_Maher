import string

alphabet_list = list(string.ascii_uppercase + string.ascii_lowercase + "0123456789")
# hello


rotor1 = list("enSasuBTAC9EY2bkUytGDxjfNVJFXL0cd8rZQmR1l5PvKp46OzqhgiIH7MW3wo")
rotor2 = list("yBL8P7MpwTxn52l0CtEXRZmKdNvIeug9rcf1qSikVFzbjoQWhG3YsUa6JHA4DO")
rotor3 = list("0YImcSJKtwjoLD7Ug3l2bTfi8pOykzvBx9QERePq6aV15nFdMCNW4GrsZhXAuH")
rotor4 = list("PJk069AjmqX3QbasegIdwvGS7pNRhZuTKy8Y52EcVzUWt4HODrC1BLfoinMFxl")
rotor5 = list("5jSViv7BQo3FDrGfwnJTR89ZydshmzatuW4HNEPICOkqYecK1A02X6lgUbMxLp")

rotors_list = [rotor1, rotor2, rotor3, rotor4, rotor5]
rotors_notch_list = ["Q", "E", "V", "J", "Z"]


class PlugBoard:
    def __init__(self, pairs):
        # pairs : "AB CD EF HI JK" => ["AB","CD","EF","HI","JK"]
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


# keyboard = Plugboard("AB CD EF HI JK")
# letters = "A DOG EATS CARROT"
# swapped_letters = keyboard.swap_pairs(letters)
# print("exited plugboard as: ", swapped_letters)


class Reflector:
    def __init__(self):
        self.reflector_dict = {'a': 'm', 'm': 'a', 'b': 'U', 'U': 'b', 'c': 'y', 'y': 'c',
                            'd': 'e', 'e': 'd', 'f': '1', '1': 'f', 'g': 'V', 'V': 'g', 'h': 'Z',
                            'Z': 'h', 'i': 'H', 'H': 'i', 'j': 'n', 'n': 'j', 'k': 'I', 'I': 'k', 'l': 'C',
                            'C': 'l', 'o': 'R', 'R': 'o', 'p': 'Y', 'Y': 'p', 'q': 'W', 'W': 'q',
                            'r': '4', '4': 'r', 's': 'K', 'K': 's', 't': 'x', 'x': 't', 'u': 'B', 'B': 'u',
                            'v': '7', '7': 'v', 'w': 'E', 'E': 'w', 'z': '9', '9': 'z', 'A': 'S', 'S': 'A',
                            'D': 'G', 'G': 'D', 'F': '6', '6': 'F', 'J': 'P', 'P': 'J', 'L': 'O', 'O': 'L',
                            'M': '5', '5': 'M', 'N': 'X', 'X': 'N', 'Q': '0', '0': 'Q', 'T': '8',
                            '8': 'T', '2': '3', '3': '2'}

    def reflect_pairs(self, letter):
        if letter in alphabet_list:
            return self.reflector_dict[letter]
        else:
            return letter



def caeser_shift(str, amount):
    output = ""

    for i in range(len(str)):
        c = str[i]
        code = ord(c)
        if (code >= 65) and (code <= 90):
            c = chr(((code - 65 + amount) % 26) + 65)
        output += c

    return output


class Rotor:
    def __init__(self, rotor_number: int, ring_settings: str, ring_position: str):
        self.rotor_list = rotors_list[rotor_number - 1]
        self.rotor_notch = rotors_notch_list[rotor_number - 1]
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
        return alphabet_list[(index - self.offset + len(alphabet_list) % len(alphabet_list))]

    def encrypt_letter_reverse(self, letter):
        index = alphabet_list.index(letter)
        index = (index + self.offset) % len(alphabet_list)
        temp = alphabet_list[index]
        index = self.rotor_list.index(temp)
        return alphabet_list[(index - self.offset + len(alphabet_list) % len(alphabet_list))]


def encode(input_text) -> str:
    global rotors, ring_settings, ring_positions
    fast_rotor = Rotor(rotors[2], ring_settings[2], ring_positions[2])
    medium_rotor = Rotor(rotors[1], ring_settings[1], ring_positions[1])
    slow_rotor = Rotor(rotors[0], ring_settings[0], ring_positions[0])
    keyboard = PlugBoard("AB CD EF HI JK")
    reflector = Reflector()

    # plugboard swapping
    input_text = keyboard.swap_pairs(input_text)

    encoded_message = ""

    for letter in input_text:

        if letter in alphabet_list:

            # Rotate, once I get a letter I rotate the rotor before encryption
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
                    medium_rotor.rotor_letter = alphabet_list[
                        (alphabet_list.index(medium_rotor.rotor_letter) + 1) % len(alphabet_list)]
                    slow_rotor.rotor_letter = alphabet_list[
                        (alphabet_list.index(slow_rotor.rotor_letter) + 1) % len(alphabet_list)]

            # re sit the offset after the rotation
            fast_rotor.set_offset()
            medium_rotor.set_offset()
            slow_rotor.set_offset()

            # encrypt the letter through the three rotors in sequence
            letter = fast_rotor.encrypt_letter(letter)
            letter = medium_rotor.encrypt_letter(letter)
            letter = slow_rotor.encrypt_letter(letter)

            # data
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

input_text = input("Enter text to encrypt/decrypt: ").strip()

output = encode(input_text)
print("Encrypted message: ", output)
