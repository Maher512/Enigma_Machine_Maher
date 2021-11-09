# hello
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']

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

    
    def reflect_pairs(self, letter):
        if letter in alphabet_list:
            return self.reflector_list[alphabet_list.index(letter)]
        else:
            return letter


keyboard = PlugBoard("AB CD EF HI JK")
letters = "A DOG EATS CARROT"
swapped_letters = keyboard.swap_pairs(letters)
print("exited plugboard as: ", swapped_letters)
my_reflector = Reflector()
reflected_letters = ""
for letter in swapped_letters:
    reflected_letters += my_reflector.reflect_pairs(letter)
print("exited reflector as: ", reflected_letters)


class Rotor:
    def __init__(self, rotor):
        self.rotor = rotor





