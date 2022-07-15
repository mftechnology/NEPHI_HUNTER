from nephi_hunter.constants import *
from nephi_hunter.game.casting.actor import Actor
from nephi_hunter.game.scripting.action import Action
from nephi_hunter.game.shared.point import Point
from nephi_hunter.game.casting.animals import Animals


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        bow = cast.get_first_actor("bow")
        arrow = cast.get_first_actor("arrow")
        animal = cast.get_first_actor("animal")
        poison = cast.get_first_actor("poison")
    
        body = animal.get_body()

        if body.get_position().equals(arrow.get_position()):
            body.update()

           # score.add_points(points)
          
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the arrow collides with one animal.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        animals = cast.get_first_actor("animals")
        body = animals.get_body()
                
        for animal in animals:
            if animal.get_position().equals(body.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
          #  snake = cast.get_first_actor("snakes")
          #  segments = snake.get_segments()
          #  food = cast.get_first_actor("foods")

            x = int(MAX_X / 2)
            y = int(MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

          #  for segment in segments:
          #      segment.set_color(constants.WHITE)
          #  food.set_color(constants.WHITE)