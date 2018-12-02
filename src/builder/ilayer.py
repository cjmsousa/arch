import abc

class iLayer(abc.ABC):

    def __init__(self):

        #Run super constructor
        super().__init__()

        print("Initializing " + self.__class__.__name__ + "builder...")
   
    @abc.abstractmethod
    def build(self):
       pass