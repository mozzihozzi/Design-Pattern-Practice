from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    def operation1(self):
        pass

    def operation2(self):
        pass

    def template_method(self):
        print("Operation1 followed by Operation2")
        self.operation1()
        self.operation2()


class ConcreteClass(AbstractClass):
    def operation1(self):
        print("Concrete Class operation 1")

    def operation2(self):
        print("Concrete Class operation 2")


class Client:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()


if __name__ == '__main__':
    client = Client()
    client.main()
