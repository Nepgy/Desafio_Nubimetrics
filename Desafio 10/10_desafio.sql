SELECT CountryRegionCode, AVG(Sales.SalesTaxRate.TaxRate) as Avg_tax_rate
FROM Person.StateProvince
INNER JOIN Sales.SalesTaxRate
ON Person.StateProvince.StateProvinceID = Sales.SalesTaxRate.StateProvinceID
GROUP BY CountryRegionCode