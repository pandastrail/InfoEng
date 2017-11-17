# Select a Database to query
USE dwhmodel;

# Time Period of data
SELECT 
    min(OrderDate),
    max(OrderDate)
FROM
    orders_dim;

# Total Profit
SELECT
	sum(UnitPrice * Quantity) AS Profit_Total
FROM
	order_fact;

# Profit by Product and Category
SELECT 
	p.ProductName,
    c.CategoryName,
    sum(o.UnitPrice * o.Quantity) AS Profit_Product,
    sum(o.UnitPrice * o.Quantity)*100 / 1326883.09 AS Profit_Percentage
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

# Product ranking per Quantity showing average Price per Unit
SELECT
	avg(o.UnitPrice),
    sum(o.Quantity) AS Total_Qty,
    p.ProductName
FROM
	order_fact AS o
JOIN
	product_dim AS p ON p.ProductID = o.ProductID
GROUP BY
	p.ProductName;
  
# Profit by Category
SELECT 
    o.CategoryID,
    c.CategoryName,
    sum(o.UnitPrice * o.Quantity) AS Profit_Category,
    sum(o.UnitPrice * o.Quantity)*100 / 1326883.09 AS Profit_Percentage
FROM
    order_fact AS o
JOIN
	category_dim AS c ON o.CategoryID = c.CategoryID
GROUP BY
	o.CategoryID
ORDER BY
	Profit_Category DESC;
    
# Sales (Order) development over time
SELECT
    t.Year,
    t.Month,
	t.Month_Name,
	c.CategoryName,
    sum(o.Quantity) AS QtySum,
    avg(o.Discount) AS AvgDiscount
FROM
	order_fact AS o
JOIN
	time_dim AS t ON o.ShippedDateID = t.Date
JOIN
	category_dim AS c ON o.CategoryID = c.CategoryID
GROUP BY 
	t.Month, t.Year, c.CategoryName
ORDER BY
	t.Year ASC, t.Month ASC;