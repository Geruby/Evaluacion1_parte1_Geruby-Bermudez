import pprint
import gc

class Grafo(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

    def set_next(self, next):
        print('Enlanzando nodos {}.next = {}'.format(self, next))
        self.next = next

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__, self.nombre)

#creando ciclo con grafos
uno = Grafo('uno')
dos = Grafo('dos')
tres = Grafo('tres')
uno.set_next(dos)
dos.set_next(tres)
tres.set_next(uno)
    
# Eliminar las referencias a los nodos grafo
uno = dos = tres = None

# Mostrar el efecto de la recolección de basura
for i in range(2):
    print('\nColectando {} ...'.format(i))
    n = gc.collect()
    print('Objetos inalcanzables:', n)
    print('Basura restante:', end=' ')
    pprint.pprint(gc.garbage)

 