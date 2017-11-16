
# Total Profit
SELECT
	sum(UnitPrice * Quantity) AS Profit_Total
FROM
	order_fact;

# Profit by Product and Category
SELECT 
	p.ProductName,
    c.CategoryName,
    sum(o.UnitPrice * o.Quantity) AS Profit_Product
FROM
    order_fact AS o
JOIN
	product_dim AS p ON o.ProductID = p.ProductID
JOIN
	category_dim AS c ON o.CategoryID = c.CategoryID
GROUP BY
	o.ProductID
ORDER BY
	Profit_Product DESC;
    
# Profit by Category
SELECT 
    o.CategoryID,
    c.CategoryName,
    sum(o.UnitPrice * o.Quantity) AS Profit_Category
FROM
    order_fact AS o
JOIN
	category_dim AS c ON o.CategoryID = c.CategoryID
GROUP BY
	o.CategoryID
ORDER BY
	Profit_Category DESC;