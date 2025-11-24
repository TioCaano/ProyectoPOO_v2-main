from modelos.base_datos import base_datos
from modelos.dto import ArriendoDTO, ClienteDTO, EmpleadoDTO, VehiculoDTO


class EmpleadoDAO:
    def __init__(self, conexion=base_datos):
        self.base = conexion

    def crear(self, datos: EmpleadoDTO) -> bool:
        consulta = """
            INSERT INTO empleados (codigo, run, nombre, apellido, cargo, password_hash)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        parametros = (datos.codigo, datos.run, datos.nombre, datos.apellido, datos.cargo, datos.hash_contrasena)
        resultado = self.base.ejecutar(consulta, parametros, confirmar=True)
        return resultado is not None

    def listar(self):
        consulta = "SELECT * FROM empleados"
        filas = self.base.ejecutar(consulta, obtener_todos=True) or []
        return [
            EmpleadoDTO(
                id=fila["id"],
                codigo=fila["codigo"],
                run=fila["run"],
                nombre=fila["nombre"],
                apellido=fila["apellido"],
                cargo=fila["cargo"],
                hash_contrasena=fila["password_hash"],
            )
            for fila in filas
        ]

    def eliminar(self, empleado_id: int) -> bool:
        consulta = "DELETE FROM empleados WHERE id = %s"
        resultado = self.base.ejecutar(consulta, (empleado_id,), confirmar=True)
        return resultado is not None

def buscar_por_run(self, run: str):
    run_sin = run.replace("-", "")
    consulta = """
        SELECT * FROM empleados
        WHERE run = %s OR REPLACE(run, '-', '') = %s
    """
    fila = self.base.ejecutar(consulta, (run, run_sin), obtener_uno=True)
    if not fila:
        return None
    return EmpleadoDTO(
        id=fila["id"],
        codigo=fila["codigo"],
        run=fila["run"],
        nombre=fila["nombre"],
        apellido=fila["apellido"],
        cargo=fila["cargo"],
        hash_contrasena=fila["password_hash"],
        )

def contar(self) -> int:
        consulta = "SELECT COUNT(*) AS total FROM empleados"
        fila = self.base.ejecutar(consulta, obtener_uno=True)
        return fila["total"] if fila else 0


class ClienteDAO:
    def __init__(self, conexion=base_datos):
        self.base = conexion

    def crear(self, datos: ClienteDTO) -> bool:
        consulta = """
            INSERT INTO clientes (run, nombre, apellido, direccion, telefono)
            VALUES (%s, %s, %s, %s, %s)
        """
        parametros = (datos.run, datos.nombre, datos.apellido, datos.direccion, datos.telefono)
        resultado = self.base.ejecutar(consulta, parametros, confirmar=True)
        return resultado is not None

    def listar(self):
        consulta = "SELECT * FROM clientes"
        filas = self.base.ejecutar(consulta, obtener_todos=True) or []
        return [
            ClienteDTO(
                id=fila["id"],
                run=fila["run"],
                nombre=fila["nombre"],
                apellido=fila["apellido"],
                direccion=fila["direccion"],
                telefono=fila["telefono"],
            )
            for fila in filas
        ]

    def buscar_por_id(self, cliente_id: int):
        consulta = "SELECT * FROM clientes WHERE id = %s"
        fila = self.base.ejecutar(consulta, (cliente_id,), obtener_uno=True)
        if not fila:
            return None
        return ClienteDTO(
            id=fila["id"],
            run=fila["run"],
            nombre=fila["nombre"],
            apellido=fila["apellido"],
            direccion=fila["direccion"],
            telefono=fila["telefono"],
        )

    def buscar_por_run(self, run: str):
        consulta = "SELECT * FROM clientes WHERE run = %s"
        fila = self.base.ejecutar(consulta, (run,), obtener_uno=True)
        if not fila:
            return None
        return ClienteDTO(
            id=fila["id"],
            run=fila["run"],
            nombre=fila["nombre"],
            apellido=fila["apellido"],
            direccion=fila["direccion"],
            telefono=fila["telefono"],
        )

    def actualizar(self, datos: ClienteDTO) -> bool:
        consulta = """
            UPDATE clientes
            SET nombre = %s, apellido = %s, direccion = %s, telefono = %s
            WHERE id = %s
        """
        parametros = (datos.nombre, datos.apellido, datos.direccion, datos.telefono, datos.id)
        resultado = self.base.ejecutar(consulta, parametros, confirmar=True)
        return resultado is not None

    def eliminar(self, cliente_id: int) -> bool:
        consulta = "DELETE FROM clientes WHERE id = %s"
        resultado = self.base.ejecutar(consulta, (cliente_id,), confirmar=True)
        return resultado is not None


class VehiculoDAO:
    def __init__(self, conexion=base_datos):
        self.base = conexion

    def crear(self, datos: VehiculoDTO) -> bool:
        consulta = """
            INSERT INTO vehiculos (patente, marca, modelo, anio, precio_diario_uf, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        parametros = (datos.patente, datos.marca, datos.modelo, datos.anio, datos.precio_diario_uf, datos.estado)
        resultado = self.base.ejecutar(consulta, parametros, confirmar=True)
        return resultado is not None

    def listar(self, disponibles=None):
        if disponibles is None:
            consulta = "SELECT * FROM vehiculos"
            parametros = None
        elif disponibles:
            consulta = "SELECT * FROM vehiculos WHERE estado = 'DISPONIBLE'"
            parametros = None
        else:
            consulta = "SELECT * FROM vehiculos WHERE estado != 'DISPONIBLE'"
            parametros = None

        filas = self.base.ejecutar(consulta, parametros, obtener_todos=True) or []
        return [
            VehiculoDTO(
                id=fila["id"],
                patente=fila["patente"],
                marca=fila["marca"],
                modelo=fila["modelo"],
                anio=fila["anio"],
                precio_diario_uf=fila["precio_diario_uf"],
                estado=fila["estado"],
            )
            for fila in filas
        ]

    def buscar_por_id(self, vehiculo_id: int):
        consulta = "SELECT * FROM vehiculos WHERE id = %s"
        fila = self.base.ejecutar(consulta, (vehiculo_id,), obtener_uno=True)
        if not fila:
            return None
        return VehiculoDTO(
            id=fila["id"],
            patente=fila["patente"],
            marca=fila["marca"],
            modelo=fila["modelo"],
            anio=fila["anio"],
            precio_diario_uf=fila["precio_diario_uf"],
            estado=fila["estado"],
        )

    def buscar_por_patente(self, patente: str):
        consulta = "SELECT * FROM vehiculos WHERE patente = %s"
        fila = self.base.ejecutar(consulta, (patente,), obtener_uno=True)
        if not fila:
            return None
        return VehiculoDTO(
            id=fila["id"],
            patente=fila["patente"],
            marca=fila["marca"],
            modelo=fila["modelo"],
            anio=fila["anio"],
            precio_diario_uf=fila["precio_diario_uf"],
            estado=fila["estado"],
        )

    def actualizar_estado(self, vehiculo_id: int, nuevo_estado: str) -> bool:
        consulta = "UPDATE vehiculos SET estado = %s WHERE id = %s"
        resultado = self.base.ejecutar(consulta, (nuevo_estado, vehiculo_id), confirmar=True)
        return resultado is not None


class ArriendoDAO:
    def __init__(self, conexion=base_datos):
        self.base = conexion

    def crear(self, datos: ArriendoDTO) -> bool:
        consulta = """
            INSERT INTO arriendos (vehiculo_id, cliente_id, empleado_id,
                                   fecha_inicio, fecha_fin, valor_uf,
                                   total_uf, total_clp, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        parametros = (
            datos.vehiculo_id,
            datos.cliente_id,
            datos.empleado_id,
            datos.fecha_inicio,
            datos.fecha_fin,
            datos.valor_uf,
            datos.total_uf,
            datos.total_clp,
            datos.estado,
        )
        resultado = self.base.ejecutar(consulta, parametros, confirmar=True)
        return resultado is not None

    def listar(self):
        consulta = """
            SELECT a.*, v.patente,
                   c.nombre AS nombre_cliente, c.apellido AS apellido_cliente,
                   e.nombre AS nombre_empleado, e.apellido AS apellido_empleado
            FROM arriendos a
            JOIN vehiculos v ON a.vehiculo_id = v.id
            JOIN clientes c ON a.cliente_id = c.id
            JOIN empleados e ON a.empleado_id = e.id
        """
        return self.base.ejecutar(consulta, obtener_todos=True) or []

    def buscar_por_id(self, arriendo_id: int):
        consulta = "SELECT * FROM arriendos WHERE id = %s"
        fila = self.base.ejecutar(consulta, (arriendo_id,), obtener_uno=True)
        if not fila:
            return None
        return ArriendoDTO(
            id=fila["id"],
            vehiculo_id=fila["vehiculo_id"],
            cliente_id=fila["cliente_id"],
            empleado_id=fila["empleado_id"],
            fecha_inicio=fila["fecha_inicio"],
            fecha_fin=fila["fecha_fin"],
            valor_uf=fila["valor_uf"],
            total_uf=fila["total_uf"],
            total_clp=fila["total_clp"],
            estado=fila["estado"],
        )

    def actualizar_estado(self, arriendo_id: int, nuevo_estado: str) -> bool:
        consulta = "UPDATE arriendos SET estado = %s WHERE id = %s"
        resultado = self.base.ejecutar(consulta, (nuevo_estado, arriendo_id), confirmar=True)
        return resultado is not None
