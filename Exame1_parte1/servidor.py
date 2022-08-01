import Pyro4
import pprint
import gc
from Grafo import Grafo
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class Grafo_ciclo():
    pass

def main():
    Pyro4.Daemon.serveSimple(
        {
            Grafo_ciclo: "ejemplo.grafo"
        },
        host = "127.0.0.1",
        ns = True)

if __name__=="__main__":
    main()