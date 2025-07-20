from models.usuario import Usuario
from services.gestor_usuarios import GestorUsuarios

class SistemaUsuarios:
    def __init__(self):
        self.gestor = GestorUsuarios()

    def iniciar(self):
        while True:
            print("\n=== Sistema de Gestión de Usuarios ===")
            print("1. Registrar usuario")
            print("2. Iniciar sesión")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.iniciar_sesion()
            elif opcion == "3":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida.")

    def registrar_usuario(self):
        print("\n--- Registro de Usuario ---")
        try:
            nombre = input("Nombre de usuario: ").strip()
            contraseña = input("Contraseña: ").strip()
            rol = input("Rol (admin/estandar): ").strip().lower()

            usuario = Usuario(nombre, contraseña, rol)
            if self.gestor.registrar_usuario(usuario):
                print("✅ Usuario registrado exitosamente.")
            else:
                print("❌ El nombre de usuario ya existe.")
        except ValueError as e:
            print(f"⚠️ Error: {e}")

    def iniciar_sesion(self):
        print("\n--- Iniciar Sesión ---")
        nombre = input("Usuario: ").strip()
        contraseña = input("Contraseña: ").strip()
        usuario = self.gestor.autenticar_usuario(nombre, contraseña)
        if usuario:
            print(f"🔓 Sesión iniciada como {usuario.nombre}")
            self.menu_por_rol(usuario)
        else:
            print("❌ Nombre de usuario o contraseña incorrectos.")

    def menu_por_rol(self, usuario):
        if usuario.rol == "estandar":
            print(f"\n--- Menú Estándar ({usuario.nombre}) ---")
            print("1. Ver mis datos")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                datos = self.gestor.obtener_datos_usuario(usuario.nombre)
                print(f"\n📄 Nombre: {usuario.nombre}")
                print(f"🔐 Rol: {datos.get('rol', 'Desconocido')}")
            else:
                print("❌ Opción no válida.")
        elif usuario.rol == "admin":
            while True:
                print(f"\n--- Menú Admin ({usuario.nombre}) ---")
                print("1. Ver todos los usuarios")
                print("2. Cambiar rol de un usuario")
                print("3. Eliminar un usuario")
                print("4. Salir")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    self.listar_usuarios()
                elif opcion == "2":
                    self.cambiar_rol()
                elif opcion == "3":
                    self.eliminar_usuario()
                elif opcion == "4":
                    break
                else:
                    print("❌ Opción no válida.")

    def listar_usuarios(self):
        print("\n📋 Lista de usuarios:")
        usuarios = self.gestor.obtener_todos_los_usuarios()
        for nombre, datos in usuarios.items():
            print(f"- {nombre} ({datos['rol']})")

    def cambiar_rol(self):
        nombre = input("Nombre del usuario a modificar: ").strip()
        nuevo_rol = input("Nuevo rol (admin/estandar): ").strip().lower()
        if self.gestor.cambiar_rol(nombre, nuevo_rol):
            print("✅ Rol actualizado correctamente.")
        else:
            print("❌ Error al actualizar rol. Verifique el nombre y rol.")

    def eliminar_usuario(self):
        nombre = input("Nombre del usuario a eliminar: ").strip()
        confirmacion = input(f"¿Está seguro de eliminar a '{nombre}'? (s/n): ").lower()
        if confirmacion == "s":
            if self.gestor.eliminar_usuario(nombre):
                print("🗑️ Usuario eliminado correctamente.")
            else:
                print("❌ Usuario no encontrado.")
        else:
            print("❎ Eliminación cancelada.")
