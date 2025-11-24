from datetime import datetime

from modelos.dao import ArriendoDAO, ClienteDAO, VehiculoDAO
from modelos.dto import ArriendoDTO
from modelos.entidades import Arriendo, Cliente, Empleado, Vehiculo
from servicios import obtener_valor_uf


class ControladorArriendos:
    def __init__(self):
        self.dao = ArriendoDAO()
        self.dao_vehiculos = VehiculoDAO()
        self.dao_clientes = ClienteDAO()

    def crear_arriendo(self, empleado: Empleado):
        print("\n=== Crear Arriendo ===")
        vehiculos = [Vehiculo(datos) for datos in self.dao_vehiculos.listar(disponibles=True)]
        if not vehiculos:
            print("No hay vehiculos disponibles.")
            return

        for vehiculo in vehiculos:
            datos_vehiculo = vehiculo.obtener_datos()
            print(
                f"[{datos_vehiculo.id}] {datos_vehiculo.patente} - {datos_vehiculo.marca} {datos_vehiculo.modelo} "
                f"({datos_vehiculo.anio}) | UF/dia: {datos_vehiculo.precio_diario_uf}"
            )

        try:
            vehiculo_id = int(input("ID de vehiculo: "))
        except ValueError:
            print("ID invalido.")
            return

        datos_vehiculo = self.dao_vehiculos.buscar_por_id(vehiculo_id)
        if not datos_vehiculo or datos_vehiculo.estado != "DISPONIBLE":
            print("Vehiculo no disponible.")
            return

        clientes = [Cliente(datos) for datos in self.dao_clientes.listar()]
        if not clientes:
            print("No hay clientes registrados.")
            return

        for cliente in clientes:
            datos_cliente = cliente.obtener_datos()
            print(f"[{datos_cliente.id}] {datos_cliente.run} - {datos_cliente.nombre} {datos_cliente.apellido}")

        try:
            cliente_id = int(input("ID de cliente: "))
        except ValueError:
            print("ID invalido.")
            return

        datos_cliente = self.dao_clientes.buscar_por_id(cliente_id)
        if not datos_cliente:
            print("Cliente no encontrado.")
            return

        try:
            inicio_str = input("Fecha/hora inicio (YYYY-MM-DD HH:MM): ")
            fin_str = input("Fecha/hora fin (YYYY-MM-DD HH:MM): ")
            fecha_inicio = datetime.strptime(inicio_str, "%Y-%m-%d %H:%M")
            fecha_fin = datetime.strptime(fin_str, "%Y-%m-%d %H:%M")
            if fecha_fin <= fecha_inicio:
                print("La fecha de fin debe ser posterior a la de inicio.")
                return
        except ValueError:
            print("Formato de fecha invalido.")
            return

        valor_uf = obtener_valor_uf(fecha_inicio)
        dias = (fecha_fin - fecha_inicio).days or 1
        total_uf = float(datos_vehiculo.precio_diario_uf) * dias
        total_clp = total_uf * valor_uf

        print(
            f"Dias: {dias} | UF/dia: {datos_vehiculo.precio_diario_uf} | Total UF: {total_uf:.2f} | "
            f"UF en CLP: {valor_uf:.2f} | Total CLP: {total_clp:.0f}"
        )

        if input("Confirmar arriendo? (s/n): ").strip().lower() != "s":
            print("Arriendo anulado por el usuario.")
            return

        datos_arriendo = ArriendoDTO(
            vehiculo_id=datos_vehiculo.id,
            cliente_id=datos_cliente.id,
            empleado_id=empleado.obtener_id(),
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            valor_uf=valor_uf,
            total_uf=total_uf,
            total_clp=total_clp,
            estado="VIGENTE",
        )

        if self.dao.crear(datos_arriendo):
            self.dao_vehiculos.actualizar_estado(datos_vehiculo.id, "ARRENDADO")
            print("Arriendo creado correctamente.")
        else:
            print("Error al crear arriendo.")

    def listar_arriendos(self):
        return self.dao.listar()

    def cancelar_arriendo(self):
        print("\n=== Cancelar Arriendo ===")
        arriendos = self.dao.listar()
        if not arriendos:
            print("No hay arriendos.")
            return

        for arriendo in arriendos:
            print(
                f"[{arriendo['id']}] Veh: {arriendo['patente']} | Cliente: {arriendo['nombre_cliente']} {arriendo['apellido_cliente']} "
                f"| Inicio: {arriendo['fecha_inicio']} | Estado: {arriendo['estado']}"
            )

        try:
            arriendo_id = int(input("ID de arriendo a cancelar: "))
        except ValueError:
            print("ID invalido.")
            return

        datos_arriendo = self.dao.buscar_por_id(arriendo_id)
        if not datos_arriendo:
            print("Arriendo no encontrado.")
            return

        arriendo_modelo = Arriendo(datos_arriendo)
        if not arriendo_modelo.puede_cancelarse(datetime.now()):
            print("No se puede cancelar: faltan menos de 4 horas para el inicio.")
            return

        if self.dao.actualizar_estado(arriendo_id, "CANCELADO"):
            self.dao_vehiculos.actualizar_estado(datos_arriendo.vehiculo_id, "DISPONIBLE")
            print("Arriendo cancelado correctamente.")
        else:
            print("Error al cancelar arriendo.")
