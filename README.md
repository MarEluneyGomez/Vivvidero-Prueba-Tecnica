# DOCUMENTACION DE script.py
Este codigo esta hecho por Martín Eluney Gómez Piñeiro, para la prueba tecnica de VivVidero.

## Trabajo pedido

Utilizando Python, crea un pipeline de datos que lea los datos del archivo CSV
proporcionado, realice una transformación simple (por ejemplo, calcular el precio total si no
está presente como columna) y guarde los datos transformados en una base de datos
PostgreSQL.

## Librerias utilizadas
+ Pandas
+ SQLAlchemy

## codigo explicado
 
1. Función 'crate_dataframe': una pequeña funcion que lee el csv prporcionado y lo convierte en un dataframe

2. Función 'transform_dataframe': una funcion que tiene 3 funciones principales
    + Cambio de tipo de dato a datatime en la columna 'Date'.
    + Valor promedio por unidad: Una pequeña cuenta que divide el precio total de la venta (Total Revenue) por la cantridad productos de un cieto tipo vendidos(Units sold),
     con el objetivo de averiguar si hubo algun tipo de descuento o error al momento de la venta.
    + Cambio de nombres en las columnas para seguir con los estandares conocidos (sin mayusculas ni espacios).

3. Función 'upload_table': una función que se encarga de 
 + Realizar la conexion con la base de datos.
 + Establecer los nombres de las columnas y los tipos de datos de la tabla a crear.
 + Convertir el dataframe transformado en una tabla SQL, o, en caso de ya existir la tabla, se agregue a la tabla ya existente.

 Ademas cuenta con un manejo de excepcion de errores para poder manejar más facilmente cualquier error que pueda suceder al intentrar subir el dataframe a la base de datos

4. Función main: Se encarga de llamar y ejecutar en orden las funciones anteriormente definidas.

