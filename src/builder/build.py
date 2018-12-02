import sys

#Add code path to sys path
sys.path.append("./build/")
sys.path.append("./connector/")
sys.path.append("./data-source/")
sys.path.append("./configuration/")

#Import C4 Model generators
from c4systemcontext import C4SystemContext
from c4container import C4Container
from c4component import C4Component
from c4code import C4Code

#Create c4 model layer generators
c4SystemContext = C4SystemContext()
c4Container = C4Container()
c4Component = C4Component()
c4Ccode = C4Code()

#Generate models
c4SystemContext.build()
c4Container.build()
c4Component.build()
c4Ccode.build()