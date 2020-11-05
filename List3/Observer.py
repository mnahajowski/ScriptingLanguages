from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List



class Subject(ABC):

    @abstractmethod
    def subscribe(self, observer: Observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class SingleSubject(Subject):
    __state: int = None

    __observers: List[Observer] = []

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, newState):
        self.__state = newState

    @property
    def observers(self):
        return self.__observers

    def subscribe(self, observer: Observer) -> None:
        print("Subject attached to an observer")
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify(self) -> None:
        print("State of subject changed. Notifying observers...")
        for observer in self.observers:
            observer.update(self)

    def changingState(self) -> None:
        print("\nSubject is changing state...")
        self.state = randrange(0, 10)

        print(f"Subject's' state has just changed to: {self.__state}")
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class SingleObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state <= 5:
            print("Reacting to the subject state - observer A")


class SingleObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state == 0 or subject.state >= 1:
            print("Reacting to the subject state - observer B")


if __name__ == "__main__":
    subject = SingleSubject()

    observer_a = SingleObserverA()
    subject.subscribe(observer_a)

    observer_b = SingleObserverB()
    subject.subscribe(observer_b)

    subject.changingState()
    subject.changingState()
    subject.changingState()

    subject.unsubscribe(observer_a)
    subject.changingState()
    subject.changingState()
