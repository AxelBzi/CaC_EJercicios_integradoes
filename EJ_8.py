from EJ_7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, nombre, edad, dni, cantidad,bonificacion):
        super().__init__(nombre, edad, dni, cantidad)
        self._bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self,porcentaje):
        self._bonificacion = porcentaje

    def es_titular_valido(self):
        return super().es_mayor_de_edad() and self.edad <= 25

    def retirar(self,cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No es titular valido")

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificacion: {self.bonificacion}%")
    
