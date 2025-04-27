from html.entities import name2codepoint


class MindMapLeaf:
    """- Step 1: Write the __init__ method
    - Define an __init__ method that takes two parameters: name and shape.
    - Assign these parameters to the instance variables self.name and self.shape.

    **Hint**: Use `self.name = name` and `self.shape = shape` to assign attributes."""

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape



    # Step 2: Write the __str__ method
    # - Define __str__ that formats the name using get_shape_representation().

    def __str__(self):
        return self.get_shape_representation().format(self.name)

    # Step 3: Write the display method
    # - Print the name with indentation using " " * indent + str(self).

    def display(self, indent=0):
        print(' ' * indent + str(self))

    # Step 4: Write the get_shape_representation method
    # - Create a shapes dictionary with shape templates.
    # - Use shapes.get to return the appropriate shape template.

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