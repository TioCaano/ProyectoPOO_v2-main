import os
from controladores import ControladorArriendos, ControladorClientes, ControladorEmpleados, ControladorVehiculos

class VistaConsola:
    def __init__(self):
        self.controlador_empleados = ControladorEmpleados()
        self.controlador_clientes = ControladorClientes()
        self.controlador_vehiculos = ControladorVehiculos()
        self.controlador_arriendos = ControladorArriendos()

    def limpiar_pantalla(self):
        os.system("cls" if os.name == "nt" else "clear")

    def pausar(self):
        input("Presiona Enter para continuar...")

    def menu_empleados(self):
        seguir = True
        while seguir:
            self.limpiar_pantalla()
            print("===========================================")
            print("=== Gestion de Empleados (solo Gerente) ===")
            print("===========================================")
            print("1. Crear empleado")
            print("2. Listar empleados")
            print("3. Eliminar empleado")
            print("0. Volver")
            op = input("Opcion: ").strip()
            if op == "1":
                self.controlador_empleados.crear_empleado()
                print("\n")
                self.pausar()
            elif op == "2":
                empleados = self.controlador_empleados.listar_empleados()
                if not empleados:
                    print("No hay empleados.")
                else:
                    for empleado in empleados:
                        datos = empleado.obtener_datos()
                        print(
                            f"[{datos.id}] {datos.codigo} - {datos.nombre} {datos.apellido} "
                            f"({datos.cargo}) RUN: {datos.run}"
                        )
                print("\n")
                self.pausar()
            elif op == "3":
                empleados = self.controlador_empleados.listar_empleados()
                if not empleados:
                    print("No hay empleados para eliminar.")
                else:
                    for empleado in empleados:
                        datos = empleado.obtener_datos()
                        print(f"[{datos.id}] {datos.codigo} - {datos.nombre} {datos.apellido} ({datos.cargo}) RUN: {datos.run}")
                    try:
                        emp_id = int(input("ID empleado: "))
                        self.controlador_empleados.eliminar_empleado(emp_id)
                    except ValueError:
                        print("ID invalido.")
                print("\n")
                self.pausar()
            elif op == "0":
                seguir = False
            else:
                print("Opcion invalida.")
                print("\n")
                self.pausar()

    def menu_clientes(self):
        seguir = True
        while seguir:
            self.limpiar_pantalla()
            print("===========================")
            print("=== Gestion de Clientes ===")
            print("===========================")
            print("1. Crear cliente")
            print("2. Listar clientes")
            print("3. Editar cliente")
            print("4. Eliminar cliente")
            print("0. Volver")
            op = input("Opcion: ").strip()
            if op == "1":
                self.controlador_clientes.crear_cliente()
                print("\n")
                self.pausar()
            elif op == "2":
                clientes = self.controlador_clientes.listar_clientes()
                if not clientes:
                    print("No hay clientes.")
                else:
                    for cliente in clientes:
                        datos = cliente.obtener_datos()
                        print(f"[{datos.id}] {datos.run} - {datos.nombre} {datos.apellido} | {datos.direccion} | {datos.telefono}")
                print("\n")
                self.pausar()
            elif op == "3":
                clientes = self.controlador_clientes.listar_clientes()
                if not clientes:
                    print("No hay clientes para editar.")
                else:
                    for cliente in clientes:
                        datos = cliente.obtener_datos()
                        print(f"[{datos.id}] {datos.run} - {datos.nombre} {datos.apellido}")
                    try:
                        cli_id = int(input("ID cliente: "))
                        self.controlador_clientes.editar_cliente(cli_id)
                    except ValueError:
                        print("ID invalido.")
                print("\n")
                self.pausar()
            elif op == "4":
                clientes = self.controlador_clientes.listar_clientes()
                if not clientes:
                    print("No hay clientes para eliminar.")
                else:
                    for cliente in clientes:
                        datos = cliente.obtener_datos()
                        print(f"[{datos.id}] {datos.run} - {datos.nombre} {datos.apellido}")
                    try:
                        cli_id = int(input("ID cliente: "))
                        self.controlador_clientes.eliminar_cliente(cli_id)
                    except ValueError:
                        print("ID invalido.")
                print("\n")
                self.pausar()
            elif op == "0":
                seguir = False
            else:
                print("Opcion invalida.")
                print("\n")
                self.pausar()

    def menu_vehiculos(self):
        seguir = True
        while seguir:
            self.limpiar_pantalla()
            print("============================")
            print("=== Gestion de Vehiculos ===")
            print("==================?=========")
            print("1. Crear vehiculo")
            print("2. Listar vehiculos")
            print("0. Volver")
            op = input("Opcion: ").strip()
            if op == "1":
                self.controlador_vehiculos.crear_vehiculo()
                print("\n")
                self.pausar()
            elif op == "2":
                vehiculos = self.controlador_vehiculos.listar_vehiculos()
                if not vehiculos:
                    print("No hay vehiculos.")
                else:
                    for vehiculo in vehiculos:
                        datos = vehiculo.obtener_datos()
                        print(
                            f"[{datos.id}] {datos.patente} - {datos.marca} {datos.modelo} "
                            f"({datos.anio}) | UF/dia: {datos.precio_diario_uf} | {datos.estado}"
                        )
                print("\n")
                self.pausar()
            elif op == "0":
                seguir = False
            else:
                print("Opcion invalida.")
                print("\n")
                self.pausar()

    def menu_arriendos(self, empleado):
        seguir = True
        while seguir:
            self.limpiar_pantalla()
            print("==============================")
            print("\n=== Gestion de Arriendos ===")
            print("==============================")
            print("1. Crear arriendo")
            print("2. Listar arriendos")
            print("3. Cancelar arriendo")
            print("0. Volver")
            op = input("Opcion: ").strip()
            if op == "1":
                self.controlador_arriendos.crear_arriendo(empleado)
                print("\n")
                self.pausar()
            elif op == "2":
                arriendos = self.controlador_arriendos.listar_arriendos()
                if not arriendos:
                    print("No hay arriendos.")
                else:
                    for a in arriendos:
                        print(
                            f"[{a['id']}] Veh: {a['patente']} | Cliente: {a['nombre_cliente']} {a['apellido_cliente']} "
                            f"| Empleado: {a['nombre_empleado']} {a['apellido_empleado']} "
                            f"| Inicio: {a['fecha_inicio']} | Fin: {a['fecha_fin']} "
                            f"| Total CLP: {a['total_clp']:.0f} | Estado: {a['estado']}"
                        )
                print("\n")
                self.pausar()
            elif op == "3":
                self.controlador_arriendos.cancelar_arriendo()
                print("\n")
                self.pausar()
            elif op == "0":
                seguir = False
            else:
                print("Opcion invalida.")
                print("\n")
                self.pausar()

    def menu_principal(self):
        self.limpiar_pantalla()
        print("=== Sistema de Arriendos ===")
        self.controlador_empleados.crear_empleado_inicial_si_no_existen()
        empleado = self.controlador_empleados.login()
        if not empleado:
            return
        salir = False
        while not salir:
            self.limpiar_pantalla()
            print("======================")
            print("=== Menu Principal ===")
            print("======================")
            if empleado.puede_gestionar_empleados():
                print("1. Gestion de Empleados")
                print("2. Gestion de Clientes")
                print("3. Gestion de Vehiculos")
                print("4. Gestion de Arriendos")
                print("0. Salir")
                op = input("Opcion: ").strip()
                if op == "1":
                    self.menu_empleados()
                elif op == "2":
                    self.menu_clientes()
                elif op == "3":
                    self.menu_vehiculos()
                elif op == "4":
                    self.menu_arriendos(empleado)
                elif op == "0":
                    print("Saliendo del sistema...\n\n")
                    salir = True
                else:
                    print("Opcion invalida.")
            else:
                print("1. Gestion de Clientes")
                print("2. Gestion de Arriendos")
                print("0. Salir")
                op = input("Opcion: ").strip()
                if op == "1":
                    self.menu_clientes()
                elif op == "2":
                    self.menu_arriendos(empleado)
                elif op == "0":
                    print("Saliendo del sistema...\n\n")
                    salir = True
                else:
                    print("Opcion invalida.")
