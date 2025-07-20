class Usuario:
    def __init__(self, nombre, contraseña, rol="estandar"):
        self._nombre = nombre.strip()
        self._contraseña = contraseña.strip()
        self._rol = rol.strip().lower() if rol.lower() in ["admin", "estandar"] else "estandar"

        self._validar()

    def _validar(self):
        if not self._nombre:
            raise ValueError("El nombre de usuario no puede estar vacío.")
        if not self._contraseña:
            raise ValueError("La contraseña no puede estar vacía.")

    @property
    def nombre(self):
        return self._nombre

    @property
    def contraseña(self):
        return self._contraseña

    @property
    def rol(self):
        return self._rol

    def to_dict(self):
        return {
            "contraseña": self._contraseña,
            "rol": self._rol
        }

    @staticmethod
    def from_dict(nombre, data):
        return Usuario(nombre, data["contraseña"], data.get("rol", "estandar"))
#Encapuslamiento
# @property : Son una forma de exponer un atributo oculto como si fuera un atributo público, pero usando métodos para controlar su acceso.