class EngAlphabet():
    til = 'English'
    alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_examples = {'a': "Apple", 'b': "Ball", 'c': "Cat", 'd': "Dog", 'e': "Elephant", 'f': "Fish", 'g': "Giraffe", 'h': "House", 'i': "Ice cream", 'j': "Juice", 'k': "Kite", 'l': "Lion", 'm': "Monkey", 'n': "Nest", 'o': "Orange", 'p': "Pencil", 'q': "Queen", 'r': "Rabbit", 's': "Sun", 't': "Tiger", 'u': "Umbrella", 'v': "Violin", 'w': "Whale", 'x': "Xylophone", 'y': "Yacht", 'z': "Zebra"}
    alphabet_count = len(alphabet)
    
    def check(self, letter):
        if letter.lower() in self.alphabet:
            print(f"{letter.upper()}: {self.alphabet_examples[letter.lower()]}")
        else:
            print("Ingliz alifbosida bunday harf mavjud emas!")
            
test = EngAlphabet()

test.check('p')
test.check('Щ')