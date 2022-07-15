from nephi_hunter.game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        desert = cast.get_first_actor("desert")
        #bow = cast.get_first_actor("bow")
        #arrow = cast.get_first_actor("arrow")
        #animal = cast.get_first_actor("animal")
        #poison = cast.get_first_actor("poison")
        #segments = snake.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(desert)
        #self._video_service.draw_actor(bow)
        #self._video_service.draw_actors(arrow)
        #self._video_service.draw_actor(animal)
        #self._video_service.draw_actor(poison)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()