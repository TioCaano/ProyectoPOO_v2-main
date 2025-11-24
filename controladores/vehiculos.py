from modelos.dao import VehiculoDAO
from modelos.dto import VehiculoDTO
from modelos.entidades import Vehiculo


class ControladorVehiculos:
    def __init__(self):
        self.dao = VehiculoDAO()

    def crear_vehiculo(self):
        print("\n=== Crear Vehiculo ===")
        patente = input("Patente: ").strip().upper()
        if self.dao.buscar_por_patente(patente):
            print("La patente ya existe. Ingrese una patente distinta.")
            return
        marca = input("Marca: ").strip()
        modelo = input("Modelo: ").strip()
        try:
            anio = int(input("Anio: "))
            precio_diario_uf = float(input("Precio diario en UF: "))
        except ValueError:
            print("Anio o precio invalido.")
            return

        datos = VehiculoDTO(
            patente=patente,
            marca=marca,
            modelo=modelo,
            anio=anio,
            precio_diario_uf=precio_diario_uf,
            estado="DISPONIBLE",
        )

        if self.dao.crear(datos):
            print("Vehiculo creado correctamente.")
        else:
            print("Error al crear vehiculo.")

    def listar_vehiculos(self, disponibles=None):
        return [Vehiculo(datos) for datos in self.dao.listar(disponibles)]
