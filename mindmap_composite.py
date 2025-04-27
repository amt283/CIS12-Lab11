import os

class MindMapComposite:
    """ Step 1: Write the __init__ method
    - Define an __init__ method that takes name and shape as parameters.
    - Initialize self.name, self.shape, and an empty list self.children.


    **Hint**: Use `self.children = []` to initialize the list."""

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    # Step 2: Write the add and remove methods
    # - Use append() to add and remove() to delete from the children list.

    def remove(self, child):
        self.children.remove(child)

    def add(self, child):
        self.children.append(child)

    # Step 3: Write the __str__ method
    # - Format the name using get_shape_representation() and return it.

    def get_shape_representation(self):
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}(("
        }
        return shapes.get(self.shape, '')

    def __str__(self):
        return self.get_shape_representation().format(self.name)

    # Step 4: Write the display method
    # - Print the name with the specified indentation.
    # - Loop over each child and call display with increased indentation.

    def display(self, indent=0):
        if indent == 0:
            print('mindmap'+os.linesep+'root', end='')
        print(' ' * indent + str(self) + '\n')
        for child in self.children:
            child.display(indent + 2)
