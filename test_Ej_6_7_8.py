from EJ_6 import Persona
from EJ_7 import Cuenta
from EJ_8 import CuentaJoven


print("---------Test Clase Persona---------")
persona = Persona("Axel",24,12345678)
persona.mostrar()
print(persona.es_mayor_de_edad())
persona.nombre = "Carlos"
persona.edad = 17
persona.dni = 1122334455
persona.mostrar()
print(persona.es_mayor_de_edad())
print("---------Test Clase Cuenta---------")
cuenta = Cuenta("Pedro",24,22336655,5000)
cuenta.mostrar()
cuenta.retirar(500)
cuenta.ingresar(500)
print("---------Test Clase CuentaJoven---------")
cuenta_joven = CuentaJoven("Juan",19,12345469,2000,10)
cuenta_joven.mostrar()
cuenta_joven.retirar(200)
cuenta_joven.edad = 30
cuenta_joven.retirar(500)