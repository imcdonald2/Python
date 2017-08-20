from collections import OrderedDict

glossary = OrderedDict()

glossary['list'] = "An ordered number of values stored in one variable."
glossary['dictionary'] = "A variable that holds a 'key-value' pair."
glossary['function'] = 'A specific block of code that can be executed repeatedly.'

for term, definition in glossary.items():
    print(term.title() + ": " + definition)
