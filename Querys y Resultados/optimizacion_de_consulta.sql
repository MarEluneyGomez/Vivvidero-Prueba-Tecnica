
/* codigo a optimizar:
SELECT category, SUM(total_price)
FROM sales
WHERE total_price IS NOT NULL
GROUP BY category;
Herramientas: PostgreSQL*/

SELECT "Product Category", SUM("Total Revenue") As total_sum
FROM sales
GROUP BY "Product Category";

/*elimine la linea 'WHERE total_price IS NOT NULL' ya que la columna no cuenta con nulos, por lo que filrarlo de esta manera es inecesario
y agregue un nombre a el total de la suma, para mayor entendimiento al momento de visualizar el resultado.
Ademas como los nombres de las columnas no coincidian con los que yo utilice, le cambie los nombres por los correspondientes, para poder realizar la consulta correctamente.*/