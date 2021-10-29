
from game.actor import Actor
from game.point import Point

class Buffer(Actor):
    """A line that displays text during the game. The responsibility of Buffer is to keep track of it's appearnce, the letters
    the player types, and whether the player has cleared it.

    Stereotype:
        Information Holder

    Attributes:
        _text (string): The letters the player has typed.
        _position (Point): The buffer's position in 2d space.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        self._text = ""
        self._position = Point(0, 0)
    
    def add_letter(self, letter):
        pass

    def clear_buffer(self):
        pass

    def get_buffer(self):
        """Returns the current buffer.
        
        Args:
            self (Buffer): an instance of Buffer.
        """
        return self._text