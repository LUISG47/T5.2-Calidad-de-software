# pylint: disable=invalid-name
"""
Módulo para calcular el costo total de ventas desde archivos JSON.
Actividad 5.2 - Ejercicio de programación 2.
"""

import sys
import time
import json
import os


def load_json_file(file_path):
    """Carga datos desde un archivo JSON con manejo de errores."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file_ptr:
            return json.load(file_ptr)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error al cargar el archivo {file_path}: {error}")
        return None


# pylint: disable=too-many-locals
def main():
    """Función principal para el cálculo de ventas."""
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Uso: python computeSales.py "
              "priceCatalogue.json salesRecord.json")
        return

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    # Cargar datos
    prices_data = load_json_file(price_file)
    sales_data = load_json_file(sales_file)

    if prices_data is None or sales_data is None:
        return

    # Crear diccionario de precios para búsqueda rápida
    price_catalogue = {item['title']: item['price'] for item in prices_data}

    total_cost = 0.0
    errors = []

    # Procesar ventas
    for sale in sales_data:
        product_name = sale.get('Product')
        quantity = sale.get('Quantity', 0)

        if product_name in price_catalogue:
            total_cost += price_catalogue[product_name] * quantity
        else:
            error_msg = f"Error: Producto '{product_name}' no encontrado."
            errors.append(error_msg)
            print(error_msg)

    elapsed_time = time.time() - start_time

    # Generar nombre de archivo dinámico concatenado
    test_case_name = os.path.basename(sales_file).split('.')[0]
    output_filename = f"SalesResults{test_case_name}.txt"

    # Preparar salida amigable
    output = (
        "--- REPORTE DE VENTAS ---\n"
        f"Archivo de Ventas: {sales_file}\n"
        f"Archivo de Precios: {price_file}\n"
        "-------------------------\n"
        f"TOTAL DE VENTAS: ${total_cost:,.2f}\n"
        "-------------------------\n"
        f"Tiempo de ejecución: {elapsed_time:.6f} segundos\n"
    )

    if errors:
        output += f"\nSe encontraron {len(errors)} errores de coincidencia.\n"

    # Imprimir en pantalla y guardar en archivo
    print(output)
    with open(output_filename, 'w', encoding='utf-8') as res_file:
        res_file.write(output)


if __name__ == "__main__":
    main()
