from catalog.product.infrastructure.product_container import ProductContainer
from abstract_event_bus import AbstractEventBus

import queue

from typing import TypeVar, Generic
T = TypeVar('T')


class EventBus(AbstractEventBus):
    def __init__(self):
        product_container = ProductContainer()
        self.events: queue.Queue = queue.Queue()
        self.event_map: dict[str, list[T]] = {
            "catalog.product.created_event": [
                product_container.translate_product_name(),
            ],
        }

    def publish(self, event: dict):
        self.events.put(event)

    def consume(self, eventName: str, limit: int):
        if eventName not in self.event_map:
            raise Exception(f"No handlers for event {eventName}")

        handlers = self.event_map[eventName]
        current_event = self.events.get_nowait()

        for _ in range(limit):
            for handler in handlers:
                handler.execute(current_event["payload"])
            