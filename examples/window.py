from pygameengine import window

w = window.Window()
e = w.event_system

def print_keys(ev):
    print(ev.data)

print(e.subscribe('key_press', print_keys))

w.run()
