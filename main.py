class enigma:
    def __init__(self, starting_pos, rotors, ringsettings, plugboard):
        self.starting_pos = starting_pos
        self.rotors = rotors
        self.ringsettings = ringsettings
        self.plugboard = plugboard

    def encrypt(self, stting):
        """
        encrypt the string
        """
        encrypted_string = ""
        return encrypted_string


class plugboard:
    def __init__(self, c1: str, c2: str):
        self.c1 = c1
        self.c2 = c2

    def pairMap(self):
        """
        replace letter c1 with c2 or c2 with c1
        """


class rotor:
    def __init__(self, keys, notch, starting_pos, offset):
        self.keys = keys  # this is an array/list
        self.notch = notch
        self.starting_pos = starting_pos
        self.offset = offset
        # Dont forget to implment the starting position and the offset

    def advance(self):
        # advance rotor by 1
        pass

    def mapchar2keys(self, char):
        # maps the character to the corresponding key on the rotor
        pass


class reflector:
    def __init__(self, keys):
        self.keys = keys  # this is an array/list

    def mapchar2keys(self, char):
        # maps the character to the corresponding key on the rotor
        pass