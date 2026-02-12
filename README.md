# T5.2 Calidad de Software

T5.2 Calidad de Software

**A01105695**

**José Luis Lorenzo Augusto Galíndez Vences**


# Actividad 5.2 - Ejercicios de Programación con Estándares Industriales

Este repositorio contiene la solución a tres problemas de programación desarrollados en **Python**, siguiendo estrictamente el estándar de codificación **PEP-8** y validados mediante **PyLint**.

## 🎯 Objetivos

* Explicar la diferencia entre pruebas dinámicas y pruebas estáticas
* Describir los beneficios e impacto de la calidad de las prácticas asociadas a pruebas estáticas.
* Explicar el origen de las inspecciones como herramienta de pruebas estáticas.
* Describir las diferencias entre revisiones informales, caminatas estructuradas, inspecciones e inspecciones automáticas.
* Describir la relación de las herramientas de análisis estático y el código fuente.
* Experimentar con el uso de herramientas de análisis estático en el código fuente.


## 📂 Contenido del Repositorio

### Listas de entrada
El repositorio contiene las listas de entrada que son los archivos a utilizar, estos son los archivos 

1. TC1.ProductList.json

2. y los archivos TC1, TC2 Y TC3.Sales.json estos 3 archivos son con los que se ejecutan las pruebas de venta


## 🛠️ Requerimientos Técnicos 

* **Verificación Pylint 10.00/10**: Todos los códigos siguen el estándar de codificación PEP-8 con verificación Pylint 10.00/10
* **Manejo de Errores**: Los programas detectan datos inválidos en los archivos de entrada, notifican el error en consola y continúan con la ejecución del resto de los datos.
* **Salida de Resultados**: Los resultados se imprimen en la terminal y se guardan automáticamente en archivos de texto específicos (`StatisticsResults.txt`, `ConvertionResults.txt`, `WordCountResults.txt`).
* **Medición de Tiempo**: Cada programa registra e incluye el tiempo total de ejecución al final de los resultados.

## 🚀 Instrucciones de Ejecución

Para ejecutar cualquiera de los programas, utiliza la terminal y pasa como argumento el nombre del archivo que contiene los datos en cada caso

Por ejemplo para cada uno de los programas este sería el argumento:

```bash
python computeSales.py TC1.ProductList.json TC1.Sales.json
python computeSales.py TC1.ProductList.json TC2.Sales.json
python computeSales.py TC1.ProductList.json TC3.Sales.json
```

Además para poder verificar la calificación del programa que hace la ejecución se puede verificar con el siguiente comando

```bash
pylint computeSales.py 
```

<img width="665" height="76" alt="Screenshot 2026-02-12 at 8 07 41 a m" src="https://github.com/user-attachments/assets/3bdd56ab-9652-4a2d-bced-c573eaaa979a" />

