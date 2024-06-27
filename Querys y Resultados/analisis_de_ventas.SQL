SELECT region, product_category, SUM(total_revenue) AS total_sales
FROM sales
GROUP BY region, product_category;