import Pyro4
import sys
from Grafo import Grafo

sys.excepthook = Pyro4.util.excepthook

mitienda = Pyro4.Proxy("PYRONAME:ejemplo.grafo")
g1 = Grafo("uno")
g2 = Grafo("dos")
g3 = Grafo("tres")



