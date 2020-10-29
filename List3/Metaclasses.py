def abstractfunc(func):
    func.__isabstract__ = True
    return func


class Interface(type):

    def __init__(self, name, bases, namespace):
        for base in bases:
            must_be_implemented = getattr(base, 'abstract_methods', [])
            class_methods_implemented = getattr(self, 'all_methods', [])
            for method in must_be_implemented:
                if method not in class_methods_implemented:
                    error_string = f"""Can't create abstract class {name}!
                    {name} must implement abstract method {method} of class {base.__name__}!"""
                    raise TypeError(error_string)

    def __new__(metaclass, name, bases, namespace):
        namespace['abstract_methods'] = Interface._get_abstract_methods(namespace)
        namespace['all_methods'] = Interface._get_all_methods(namespace)
        class_instance = super().__new__(metaclass, name, bases, namespace)
        return class_instance

    def _get_abstract_methods(namespace):
        return [name for name, method in namespace.items() if
                callable(method) and getattr(method, '__isabstract__', False)]

    def _get_all_methods(namespace):
        return [name for name, method in namespace.items() if callable(method)]


class ITelegramInterface(metaclass=Interface):

    @abstractfunc
    def sendMessage(self):
        pass

    @abstractfunc
    def receiveMessage(self):
        pass


class BusTelegram(ITelegramInterface):

    def sendMessage(self):
        pass

    def receiveMessage(self):
        pass


class TramTelegram(ITelegramInterface):

    def sendNewMessage(self):
        pass

    def receiveMessage(self):
        pass



if __name__ == "__main__":
    network = BusTelegram
    fakeNetwork = TramTelegram
