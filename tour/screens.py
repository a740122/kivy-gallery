from functools import partial
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty


class ScreenMgr(ScreenManager):
    transition = FadeTransition()

    def __init__(self):
        super(ScreenMgr, self).__init__()
        self.add_widget(Overview())
        self.add_widget(Stage())
        self.add_widget(Explorer())

        for scrn in self.screens:
            scrn.setupActions((self.setCurrentScreen, s) for s in self.screens)

    def setCurrentScreen(self, screen, *args):
        """Resets the current's screen SideBarLabel and displays the given screen.
        Uses args in definition for the handling the incoming btn instance.
        """
        self.current = screen.name


class BaseScreen(Screen):
    """Screen containing a SideBar in addition to its featured widget.
    """
    menu = ObjectProperty()
    lbl = ObjectProperty()

    def on_pre_leave(self):
        """Assures that the menu is handled properly on a screen transition.
        """
        super(BaseScreen, self).on_pre_leave()
        self.lbl.collapse()

    def setupActions(self, actions):
        """Connects its menu with the given actions.
        """
        for action, screen in actions:
            self.menu.setupAction(screen.name, partial(action, screen))


class Overview(BaseScreen):
    """BaseScreen showing all media widgets available in the app.
    """
    pass

class Stage(BaseScreen):
    """BaseScreen for viewing a single media item at a time.
    """
    pass

class Explorer(BaseScreen):
    """BaseScreen showing previously displayed media items.
    """
    pass

