from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List



class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
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

    def attach(self, observer: Observer):
        print("Subject attached to an observer")
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        print("State of subject changed. Notifying observers...")
        for observer in self.observers:
            observer.update(self)

    def some_business_logic(self):
        print("\nSubject is changing state...")
        self.state = randrange(0, 10)

        print(f"Subject's' state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject):
        pass


class SingleObserverA(Observer):
    def update(self, subject: Subject):
        if subject.state < 3:
            print("Reacting to the subject state - observer A")


class SingleObserverB(Observer):
    def update(self, subject: Subject):
        if subject.state == 0 or subject.state >= 2:
            print("Reacting to the subject state - observer B")


if __name__ == "__main__":
    subject = SingleSubject()

    observer_a = SingleObserverA()
    subject.attach(observer_a)

    observer_b = SingleObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
