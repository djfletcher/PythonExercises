import random

class Hangman:

    def __init__(self):
        self.num_wrong_guesses = 0
        self.letters_guessed = set()

    def run(self):
        self.setup()
        while not self.game_over():
            self.play_turn()

        if self.won():
            print "Correct! The word was {}!".format(self.secret_word.upper())
        if self.lost():
            print "Hahahahahha you suck. The word was {} ..dork".format(self.secret_word.upper())

    def setup(self):
        self.word_length = None

        while not self.word_length:
            raw = raw_input("Enter word length: ")
            try:
                self.word_length = int(raw)
            except ValueError:
                pass

        self.filter_words()
        self.choose_word()

    def play_turn(self):
        print "You've guessed the following letters:"
        for letter in sorted(self.letters_guessed):
            print letter.upper() + ' ',
        print "\nNow listen here.. you only have {} guesses remaining.".format(8 - self.num_wrong_guesses)
        self.display_word()
        letter = self.get_guess()
        self.letters_guessed.add(letter)
        if letter in self.secret_word:
            print "Holy cow... you're right!\n"
        else:
            self.num_wrong_guesses += 1
            print "nope lul\n"

    def get_guess(self):
        while True:
            raw = raw_input("Enter a letter: ")
            if raw in self.letters_guessed:
                print "You already guessed that letter!"
            elif raw in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
                return raw
            else:
                print "That's not a valid input."

    def display_word(self):
        displayed = [char.upper() if char in self.letters_guessed else '_' for char in self.secret_word]
        print ' '.join(displayed)

    def filter_words(self):
        dictionary = open('/usr/share/dict/words', 'r')
        words = dictionary.readlines()
        dictionary.close()
        self.word_pool = { word.strip().lower() for word in words if len(word.strip()) == self.word_length }
        return self.word_pool

    def choose_word(self):
        self.secret_word = random.choice(tuple(self.word_pool))
        return self.secret_word

    def game_over(self):
        return self.won() or self.lost()

    def won(self):
        for letter in self.secret_word:
            if letter not in self.letters_guessed:
                return False
        return True

    def lost(self):
        return self.num_wrong_guesses >= 8

hangman = Hangman()
hangman.run()
