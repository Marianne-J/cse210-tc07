from time import sleep
from game import constants
from game.words import Words
from game.score import Score
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): The input mechanism.
        _keep_playing (boolean): Whether or not the game can continue.
        _output_service (OutputService): The output mechanism.
        _score (Score): The current score.
        _buffer (Buffer): Stores the player's input
        _words (Words): A controller / storage for the words traveling across the screen
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        self._words = Words()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the inputted character from the keyboard and resolving that input.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()

        if letter == "*":
            self._buffer.clear_buffer()
        else:
            self._buffer.add_letter(letter)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means comparing the buffer to the words, adding points, and 
        checking if any words have reached the edge of the screen.

        Args:
            self (Director): An instance of Director.
        """
        buffer_contents = self._buffer.get_buffer()
        match_count = self._words.check_words(buffer_contents)
        self._score.add_points(3 * match_count)

        self._words.move_words()

        self._expire_words()


        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In this case,
        that means telling the output service to draw the actors and refreshing the screen.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actors(self._words.get_words())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _expire_words(self):
        """Grabs the list of words and checks their x position. If they've reached the edge of the screen, 
        replaces them with new words.

        Args:
            self (Director): An instance of Director.
        """
        current_words = self._words.get_words()

        for x in current_words:
            if (x.get_position().get_x() >= constants.MAX_X - 1):
                self._words.replace_word(x.get_text())

        