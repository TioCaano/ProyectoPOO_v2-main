import pwinput
from modelos.dao import EmpleadoDAO
from modelos.dto import EmpleadoDTO
from modelos.entidades import Empleado
from servicios.utilidades import (
    calcular_hash_contrasena,
    validar_run_chileno,
    verificar_contrasena,
    normalizar_run
)


class ControladorEmpleados:
    def __init__(self):
        self.dao = EmpleadoDAO()

    def crear_empleado_inicial_si_no_existen(self):
        if self.dao.contar() == 0:
            print("No hay empleados. Debes crear un Gerente inicial.")
            self.crear_empleado()

    def crear_empleado(self):
        print("\n=== Crear Empleado ===")
        codigo = input("Codigo: ").strip()
        run_input= input("RUN: ").strip()
        if not validar_run_chileno(run_input):
            print("RUN invalido. Use formato: 12345678-9.")
            return
        try:
            run= normalizar_run(run_input)
        except ValueError as e:
                print(f"RUN invalido: {e}")
                return
        if self.dao.buscar_por_run(run_input):
            print("El RUN ya existe. Ingrese un RUN distinto.")
            return
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        cargo = input("Cargo (Gerente/Ejecutivo): ").strip().title()
        if cargo not in ("Gerente", "Ejecutivo"):
            print("Cargo invalido.")
            return
        contrasena = pwinput.pwinput("Contrasena: ",mask="*")
        contrasena2 = pwinput.pwinput("Repite la contrasena: ",mask="*")
        if contrasena != contrasena2:
            print("Las contrasenas no coinciden.")
            return
        datos = EmpleadoDTO(
            codigo=codigo,
            run=run,
            nombre=nombre,
            apellido=apellido,
            cargo=cargo,
            hash_contrasena=calcular_hash_contrasena(contrasena),
        )
        if self.dao.crear(datos):
            print("Empleado creado correctamente.")
        else:
            print("Error al crear empleado.")

    def listar_empleados(self):
        empleados = self.dao.listar()
        return [Empleado(datos) for datos in empleados]

    def eliminar_empleado(self, empleado_id: int):
        if self.dao.eliminar(empleado_id):
            print("Empleado eliminado (si existia).")
        else:
            print("Error al eliminar empleado.")

    def login(self):
        intentos = 3
        while intentos > 0:
            print("\n=== Login Empleados ===")
            run = input("RUN: ").strip()
            contrasena = pwinput.pwinput("Contrasena: ")
            if not validar_run_chileno(run_input):
                intentos -= 1
                print(f"RUN invalido. Intentos restantes: {intentos}")
                continue

            try:
                run = normalizar_run(run_input)
            except ValueError:
                intentos -= 1
                print(f"RUN invalido. Intentos restantes: {intentos}")
                continue
            if not validar_run_chileno(run):
                intentos -= 1
                print(f"RUN invalido. Intentos restantes: {intentos}")
                continue

            datos = self.dao.buscar_por_run(run)
            if not datos:
                intentos -= 1
                print(f"Empleado no encontrado. Intentos restantes: {intentos}")
                continue

            if not verificar_contrasena(contrasena, datos.hash_contrasena):
                intentos -= 1
                print(f"Contrasena incorrecta. Intentos restantes: {intentos}")
                continue

            empleado = Empleado(datos)
            print(f"Bienvenido/a {empleado.nombre_completo()} ({empleado.obtener_cargo()})")
            return empleado

        print("Maximo de intentos alcanzado. Saliendo del login...\n\n")
        return None
