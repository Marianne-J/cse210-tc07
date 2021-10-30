from game import constants
from game.actor import Actor
from game.point import Point
import random


class Words:
    """A collection of the words (Actors) displayed on the screen.
    Each item on the list is an instance of Actor, which holds its own 
    appearance, position and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _words (Array): holds each word (which is an instance of Actor)
    """


    def __init__(self):
        """The class constructor.
        
        Args:
            self (Words): an instance of Words.
        """
        
        self._words = []


    def get_words(self):
        """Returns the array of Actors.
        
        Args:
            self (Words): an instance of Words.
            word (String): a string corresponding to the
                name of an Actor in self._words.
        """

        return self._words


    def move_words(self):
        """Moves each word (instance of Actor) using the
        inherited method move_next()
        
        Args:
            self (Words): an instance of Words.

        Returns: Nothing
        """

        for word in self._words:
            word.move_next()




    def check_words(self, buffer):
        """Checks if any of the words from self._words
        are contained in the string of text.
        If found in text, words are replaced with _replace_word()
        
        Args:
            self (Words): an instance of Words.
            text (String): will be checked.

        Returns: (Int) - the number of words that were
            matched and replaced.
        """

        matches = 0

        for word in self._words:

            word_name = word._text

            if word_name in buffer:
                self._replace_word(word_name)
                matches += 1

        return matches


    def _replace_word(self, word):
        """To be used in check_words().
        Compares the argument word with the words in self._words
        and replaces it on the array using _add_word().
        
        Args:
            self (Words): an instance of Words.
            word (String): a string corresponding to the
                name of an Actor in self._words.

        Returns: Nothing
        """

        index = 0

        for i in self._words:

            if (i._text == word):
                self._words[index] = self._add_word()

            index += 1


    def _add_word(self, position, velocity):
        """To be used in _prepare_words() and _replace_word().
        Generates a new instance of actor with a random name,
        location, and velocity. 
        
        Args:
            self (Words): an instance of Words.
        """
        word = Actor()
        word.set_text(random.choice(open(constants.PATH + "/words.txt").read().splitlines()))
        word.set_position(position)
        word.set_velocity(velocity)
        self._words.append(word)


    def _prepare_words(self):
        """Uses _add_word() to fill the array self._words with
        five new instances of Actor.
        
        Args:
            self (Words): an instance of Words.
        """
        for n in range(constants.STARTING_WORDS):
            position = Point(random.randint(0,constants.MAX_X - 1), random.randint(0,constants.MAX_Y - 1))
            velocity = Point(random.randint(0,10), random.randint(0,10))
            self._add_word(position, velocity)
