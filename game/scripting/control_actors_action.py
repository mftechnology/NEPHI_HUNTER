from nephi_hunter.constants import *
from nephi_hunter.game.scripting.action import Action
from nephi_hunter.game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('left'):
            self._direction = Point(-CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('right'):
            self._direction = Point(CELL_SIZE, 0)
        
        # shot
        if self._keyboard_service.is_key_down('space'):
            self._direction = Point(0, -CELL_SIZE)
        
     
        
        bow = cast.get_first_actor("bow")
        bow.turn_head(self._direction)