class Trie:

    def __init__(self):
        self.root_node = {}

    def check_present_and_add(self, word):
        current_node = self.root_node
        new_word = False

        for char in word:
            if char not in current_node:
                new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        if '*' not in current_node:
            new_word = True
            current_node['*'] = {}

        return new_word

    def print_words(self, word=None, node=None):
        if word is None:
            word = ''
        if node is None:
            node = self.root_node

        for char in node:
            if char == '*':
                print word
            else:
                self.print_words(word=word + char, node=node[char])


t = Trie()

print t.check_present_and_add('hello')
print t.check_present_and_add('he')
print t.check_present_and_add('hi')
print t.check_present_and_add('hippy')
print t.check_present_and_add('hippo')
print t.check_present_and_add('daniel')
print t.check_present_and_add('dada')
print t.check_present_and_add('doodaday')
print t.check_present_and_add('dapper')
print t.check_present_and_add('dapperdan')

print t.check_present_and_add('hippy')
print t.check_present_and_add('doodaday')

t.print_words()
