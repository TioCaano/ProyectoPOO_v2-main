from modelos.base_datos import base_datos
from vistas import VistaConsola

if __name__ == "__main__":
    vista = VistaConsola()
    try:
        vista.menu_principal()
    except KeyboardInterrupt:
        print("\nInterrupcion del usuario. Saliendo...")
    finally:
        base_datos.cerrar()
