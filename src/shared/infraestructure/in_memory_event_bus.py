
from shared.domain.abstract_event_bus import AbstractEventBus
import queue

from typing import TypeVar, Generic
T = TypeVar('T')


class InMemoryEventBus(AbstractEventBus):
    def __init__(self, event_map: dict[str, list[T]]):
        self.events: queue.Queue = queue.Queue()
        self.event_map: dict[str, list[T]] = event_map

    def publish(self, event: dict):
        self.events.put(event)

    def consume(self, eventName: str, limit: int):
        if eventName not in self.event_map:
            raise Exception(f"No handlers for event {eventName}")

        handlers = self.event_map[eventName]

        for _ in range(limit):
            current_event = self.events.get_nowait()
            for handler in handlers:
                handler.execute(current_event["payload"])
            