from abstract_event_bus import AbstractEventBus

class EventBus(AbstractEventBus):
    def publish(self, event):
        pass

    def consume(self, eventName, limit):
        pass