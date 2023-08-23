class Persona:
    def __init__(self,nombre=None,edad=None,dni=None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if nuevo_nombre != "":
            self._nombre = nuevo_nombre
        else:
            print("El nombre no puede estar vacio")
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,nueva_edad):
        if isinstance(nueva_edad,int) and nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad debe ser un numero entero no negativo")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self,nuevo_dni):
        if isinstance(nuevo_dni,int) and len(str(nuevo_dni)) >= 7:
            self._dni = nuevo_dni
        else:
            print("El dni debe contener al menos 7 numeros")
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18
