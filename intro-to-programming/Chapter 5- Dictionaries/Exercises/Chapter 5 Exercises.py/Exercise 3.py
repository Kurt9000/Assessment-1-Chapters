print("\n"+"Exercise 3")
glossary = {
    "import": "Is a statement used to bring external modules or libraries into the program.",
    "string": "A sequence of sentences or characters enclosed within a single or double quotes.",
    "lists": "A series of items in a particular order that are enclosed in square brackets.",
    "for-loop": "A way to repeat a set of actions for each item in a list, sequence, or range.",
    "if-else": "Is a conditional statement used to execute a code based on whether a condition is true or false.",
    "input": "A function used to take user input during program execution.",
    "dictionary": "A collection of key-value pairs, enclosed in curly braces.",
    "integer": "A data type representing whole numbers, both positive and negative.",
    "tuple": "An immutable sequence of items, similar to a list but enclosed in parentheses.",
    "boolean": "A data type that can only hold one of two values which is True or False."
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning}")
