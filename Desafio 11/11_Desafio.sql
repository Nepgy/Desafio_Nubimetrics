SELECT DISTINCT Person.CountryRegion.name AS country_name, sales.Currency.name AS currency_name, max(FORMAT(Sales.CurrencyRate.AverageRate, 'N2')) AS currency_rate, FORMAT(AVG(sales.SalesTaxRate.TaxRate), 'N2') AS avg_rax_rate

FROM Sales.CurrencyRate


INNER JOIN sales.Currency
ON Sales.CurrencyRate.ToCurrencyCode = sales.Currency.CurrencyCode

INNER JOIN Sales.CountryRegionCurrency
ON Sales.Currency.CurrencyCode = Sales.CountryRegionCurrency.CurrencyCode

INNER JOIN Person.CountryRegion
ON Person.CountryRegion.CountryRegionCode = Sales.CountryRegionCurrency.CountryRegionCode

INNER JOIN Person.StateProvince
ON Person.CountryRegion.CountryRegionCode = Person.StateProvince.CountryRegionCode

INNER JOIN Sales.SalesTaxRate
ON Person.StateProvince.StateProvinceID = Sales.SalesTaxRate.StateProvinceID

WHERE Sales.CurrencyRate.AverageRate != 0 AND Sales.SalesTaxRate.TaxRate != 0

GROUP BY Person.CountryRegion.name, sales.Currency.name
ORDER BY currency_rate DESC