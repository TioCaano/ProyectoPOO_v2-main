class EmpleadoDTO:
    def __init__(self, id=None, codigo=None, run=None, nombre=None, apellido=None, cargo=None, hash_contrasena=None):
        self.id = id
        self.codigo = codigo
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.hash_contrasena = hash_contrasena


class ClienteDTO:
    def __init__(self, id=None, run=None, nombre=None, apellido=None, direccion=None, telefono=None):
        self.id = id
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono


class VehiculoDTO:
    def __init__(self, id=None, patente=None, marca=None, modelo=None, anio=None, precio_diario_uf=None, estado="DISPONIBLE"):
        self.id = id
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio_diario_uf = precio_diario_uf
        self.estado = estado


class ArriendoDTO:
    def __init__(
        self,
        id=None,
        vehiculo_id=None,
        cliente_id=None,
        empleado_id=None,
        fecha_inicio=None,
        fecha_fin=None,
        valor_uf=None,
        total_uf=None,
        total_clp=None,
        estado="VIGENTE",
    ):
        self.id = id
        self.vehiculo_id = vehiculo_id
        self.cliente_id = cliente_id
        self.empleado_id = empleado_id
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.valor_uf = valor_uf
        self.total_uf = total_uf
        self.total_clp = total_clp
        self.estado = estado
