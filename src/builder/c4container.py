from ilayer import iLayer
from outsystems import OutSystems

class C4Container(iLayer):

    def __init__(self):

        #Run super constructor
        super().__init__()

    def build(self):
        
        #Create data sources
        extranet = OutSystems("extranet")

        #Get application list
        extranetApplications = extranet.getApplications()