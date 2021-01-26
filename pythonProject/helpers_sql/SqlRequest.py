class SqlRequest:
    __instance = None

    @staticmethod
    def getInstance():
        if SqlRequest.__instance is None:
            SqlRequest()
        return SqlRequest.__instance

    def __init__(self):
        if SqlRequest.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SqlRequest.__instance = self

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, newContent):
        self.__content = newContent
