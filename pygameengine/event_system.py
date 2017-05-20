from pygameengine import event
import collections
import uuid

class EventSystem:
    def __init__(self):
        self.event_queue = collections.deque([])
        self.subscriptions = collections.defaultdict(dict)

    def publish(self, event_type, event_data={}):
        """
        Called by outside objects to push events
        """
        print("Event published: {}, {}".format(event_type, event_data))
        self.event_queue.append(event.Event(event_type, event_data))

    def flush_single(self):
        """
        Flush one event
        """
        if len(self.event_queue) == 0:
            return None

        e = self.event_queue.popleft()

        for callback in self.subscribers_for(e).values():
            callback(event)

    def flush(self):
        """
        Flush entire event queue
        """
        while len(self.event_queue) > 0:
            self.flush_single()

    def subscribers_for(self, e):
        """
        Get all the subscribers for a specific event type
        """
        return self.subscriptions.get(e.type, {})

    def subscribe(self, event_type, callback):
        """
        Subscribe a callback to an event. Returns a UUID in case an object
        wants to unsubscribe.
        """
        caller_uuid = uuid.uuid4()
        self.subscriptions[event_type][caller_uuid] = callback
        return caller_uuid

    def unsubscribe(self, event_type, uuid):
        """
        Unsubscribe from a particular event type
        """
        del self.subscriptions[event_type][uuid]
