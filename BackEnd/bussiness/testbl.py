from repository.testdl import TestDL

class TestBL:
    dl = None
    def __init__(self) -> None:
        self.dl = TestDL()
    
    def TestConnect(self):
        result = self.dl.TestConnect()
        return result

    def TestMongo(self):
        self.dl.TestMongo()
