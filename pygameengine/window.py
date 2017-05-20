import pyglet
from pygameengine.event_system import EventSystem

class Window:
    def __init__(self, event_system=EventSystem()):
        self.window = pyglet.window.Window()
        self.event_system = event_system

    def on_draw(self):
        self.window.clear()

    def on_key_press(self, symbol, modifiers):
        self.event_system.publish('key_press', {"symbol": symbol, "modifiers": modifiers})

    def on_mouse_press(self, x, y, button, modifiers):
        self.event_system.publish('mouse_press', {"x": x, "y": y, "button": button, "modifiers": modifiers})

    def update(self, dt):
        self.event_system.flush()

    def wrap(self):
        self.window.event(self.on_draw)
        self.window.event(self.on_key_press)
        self.window.event(self.on_mouse_press)

        pyglet.clock.schedule_interval(self.update, 1/60.0)

    def run(self):
        self.wrap()
        self.event_system.publish('start')
        pyglet.app.run()
