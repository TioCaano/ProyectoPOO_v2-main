from datetime import timedelta
from modelos.dto import EmpleadoDTO, ClienteDTO, VehiculoDTO, ArriendoDTO


class Persona:
    def __init__(self, run, nombre, apellido):
        self._run = run
        self._nombre = nombre
        self._apellido = apellido

    def obtener_run(self):
        return self._run

    def obtener_nombre(self):
        return self._nombre

    def obtener_apellido(self):
        return self._apellido

    def asignar_run(self, run):
        self._run = run

    def asignar_nombre(self, nombre):
        self._nombre = nombre

    def asignar_apellido(self, apellido):
        self._apellido = apellido

    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"


class Empleado(Persona):
    def __init__(self, dto: EmpleadoDTO):
        super().__init__(dto.run, dto.nombre, dto.apellido)
        self._datos = dto

    def obtener_cargo(self):
        return self._datos.cargo

    def asignar_cargo(self, cargo):
        self._datos.cargo = cargo

    def obtener_id(self):
        return self._datos.id

    def asignar_id(self, nuevo_id):
        self._datos.id = nuevo_id

    def obtener_datos(self):
        return self._datos

    def puede_gestionar_empleados(self):
        return self._datos.cargo == "Gerente"


class Cliente(Persona):
    def __init__(self, dto: ClienteDTO):
        super().__init__(dto.run, dto.nombre, dto.apellido)
        self._datos = dto

    def obtener_id(self):
        return self._datos.id

    def asignar_id(self, nuevo_id):
        self._datos.id = nuevo_id

    def obtener_datos(self):
        return self._datos


class Vehiculo:
    def __init__(self, dto: VehiculoDTO):
        self._datos = dto

    def obtener_id(self):
        return self._datos.id

    def asignar_id(self, nuevo_id):
        self._datos.id = nuevo_id

    def obtener_patente(self):
        return self._datos.patente

    def asignar_patente(self, patente):
        self._datos.patente = patente

    def obtener_estado(self):
        return self._datos.estado

    def asignar_estado(self, nuevo_estado):
        if nuevo_estado in ("DISPONIBLE", "ARRENDADO"):
            self._datos.estado = nuevo_estado

    def obtener_datos(self):
        return self._datos


class Arriendo:
    def __init__(self, dto: ArriendoDTO):
        self._datos = dto

    def obtener_id(self):
        return self._datos.id

    def asignar_id(self, nuevo_id):
        self._datos.id = nuevo_id

    def obtener_datos(self):
        return self._datos

    def puede_cancelarse(self, fecha_actual):
        delta = self._datos.fecha_inicio - fecha_actual
        return delta >= timedelta(hours=4)
