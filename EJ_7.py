from EJ_6 import Persona

class Cuenta(Persona):
    def __init__(self, nombre=None, edad=None, dni=None,cantidad=None):
        super().__init__(nombre, edad, dni)
        self._cantidad = cantidad

    @property
    def cantidad(self):
        return self._cantidad
    
    def mostrar(self):
        super().mostrar()
        print(f"Cantidad: {self.cantidad}")

    def ingresar(self,cantidad):
        if cantidad < 0:
            print("No se realizaron modificaciones")
        else:
            self._cantidad += cantidad
            print(f"Ingreso exitoso.Su nuevo saldo es {self.cantidad}")

    def retirar(self,cantidad):
        self._cantidad -= cantidad
        print(f"Retiro exitoso.Su nuevo saldo es {self.cantidad}")

