import os
import json
from models.usuario import Usuario

ARCHIVO_USUARIOS = "data/usuarios.json"

class GestorUsuarios:
    def __init__(self):
        os.makedirs(os.path.dirname(ARCHIVO_USUARIOS), exist_ok=True)
        self.usuarios = self._cargar_usuarios()

    def _cargar_usuarios(self):
        try:
            if not os.path.exists(ARCHIVO_USUARIOS):
                with open(ARCHIVO_USUARIOS, "w") as archivo:
                    json.dump({}, archivo)
                return {}

            with open(ARCHIVO_USUARIOS, "r") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, IOError):
            print("⚠️ Error al leer el archivo. Restaurando archivo vacío.")
            with open(ARCHIVO_USUARIOS, "w") as archivo:
                json.dump({}, archivo)
            return {}

    def _guardar_usuarios(self):
        try:
            with open(ARCHIVO_USUARIOS, "w") as archivo:
                json.dump(self.usuarios, archivo, indent=4)
        except IOError as e:
            print(f"❌ Error al guardar los datos: {e}")

    def registrar_usuario(self, usuario):
        if usuario.nombre in self.usuarios:
            return False
        self.usuarios[usuario.nombre] = usuario.to_dict()
        self._guardar_usuarios()
        return True

    def autenticar_usuario(self, nombre, contraseña):
        datos = self.usuarios.get(nombre)
        if datos and datos["contraseña"] == contraseña:
            return Usuario.from_dict(nombre, datos)
        return None

    def obtener_datos_usuario(self, nombre):
        return self.usuarios.get(nombre)

    def obtener_todos_los_usuarios(self):
        return self.usuarios

    def cambiar_rol(self, nombre, nuevo_rol):
        if nombre in self.usuarios and nuevo_rol in ["admin", "estandar"]:
            self.usuarios[nombre]["rol"] = nuevo_rol
            self._guardar_usuarios()
            return True
        return False

    def eliminar_usuario(self, nombre):
        if nombre in self.usuarios:
            del self.usuarios[nombre]
            self._guardar_usuarios()
            return True
        return False
