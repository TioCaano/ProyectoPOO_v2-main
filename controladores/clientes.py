from modelos.dao import ClienteDAO
from modelos.dto import ClienteDTO
from modelos.entidades import Cliente
from servicios import validar_run_chileno, validar_telefono


class ControladorClientes:
    def __init__(self):
        self.dao = ClienteDAO()

    def crear_cliente(self):
        print("\n=== Crear Cliente ===")
        run = input("RUN: ").strip()
        if not validar_run_chileno(run):
            print("RUN invalido. Use formato: 12345678-9.")
            return
        if self.dao.buscar_por_run(run):
            print("El RUN ya existe. Ingrese un RUN distinto.")
            return
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        direccion = input("Direccion: ").strip()
        telefono = input("Telefono (solo numeros, opcional +): ").strip()
        if not validar_telefono(telefono):
            print("Telefono invalido. Use solo numeros, opcional prefijo +.")
            return

        datos = ClienteDTO(run=run, nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono)
        if self.dao.crear(datos):
            print("Cliente creado correctamente.")
        else:
            print("Error al crear cliente.")

    def listar_clientes(self):
        return [Cliente(datos) for datos in self.dao.listar()]

    def editar_cliente(self, cliente_id: int):
        datos = self.dao.buscar_por_id(cliente_id)
        if not datos:
            print("Cliente no encontrado.")
            return

        print("Deja en blanco para mantener el valor actual.")
        nombre = input(f"Nombre ({datos.nombre}): ").strip() or datos.nombre
        apellido = input(f"Apellido ({datos.apellido}): ").strip() or datos.apellido
        direccion = input(f"Direccion ({datos.direccion}): ").strip() or datos.direccion
        telefono_ingresado = input(f"Telefono ({datos.telefono}): ").strip()
        telefono = datos.telefono if telefono_ingresado == "" else telefono_ingresado
        if telefono_ingresado and not validar_telefono(telefono):
            print("Telefono invalido. Use solo numeros, opcional prefijo +.")
            return

        datos.nombre = nombre
        datos.apellido = apellido
        datos.direccion = direccion
        datos.telefono = telefono

        if self.dao.actualizar(datos):
            print("Cliente actualizado correctamente.")
        else:
            print("Error al actualizar cliente.")

    def eliminar_cliente(self, cliente_id: int):
        if self.dao.eliminar(cliente_id):
            print("Cliente eliminado (si existia).")
        else:
            print("Error al eliminar cliente.")
