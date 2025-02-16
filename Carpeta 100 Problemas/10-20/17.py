class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None  # Pila vacía

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def tamaño(self):
        return len(self.items)


class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None  # Cola vacía

    def frente(self):
        if not self.esta_vacia():
            return self.items[0]
        return None

    def tamaño(self):
        return len(self.items)


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        if actual:  # Nodo encontrado
            if anterior:
                anterior.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")




# Prueba de Pila
print("Pila:")
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print("Elemento desapilado:", pila.desapilar())  # 3
print("Cima de la pila:", pila.cima())  # 2

# Prueba de Cola
print("\nCola:")
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print("Elemento desencolado:", cola.desencolar())  # 1
print("Frente de la cola:", cola.frente())  # 2

# Prueba de Lista Enlazada
print("\nLista Enlazada:")
lista = ListaEnlazada()
lista.insertar_inicio(1)
lista.insertar_inicio(2)
lista.insertar_final(3)
lista.mostrar() 
lista.eliminar(1)
lista.mostrar() 
