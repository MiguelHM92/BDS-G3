-- Active: 1734576852746@@127.0.0.1@3306@datag3
-- 1. CONTAR:
SELECT COUNT(*) FROM empleado WHERE salario > 5000;

-- MAXIMO Y MINIMO:
SELECT MAX(salario),MIN(salario),AVG(salario) FROM empleado;

SELECT DISTINCT pais FROM empleado;

SELECT pais,COUNT(*) FROM empleado
GROUP BY pais
ORDER BY COUNT(*) DESC;

SELECT pais, MAX(salario), MIN(salario), AVG(salario) FROM empleado
GROUP BY pais;

SELECT pais,area,max(salario),MIN(salario),AVG(salario) FROM empleado
WHERE salario > 5000
GROUP BY pais,area;

SELECT pais,AVG(salario) FROM empleado
GROUP BY pais
HAVING AVG(salario) > 4000;

-- SUBCONSULTAS
SELECT * FROM empleado
WHERE salario > (SELECT AVG(salario) FROM empleado);

SELECT pais,COUNT(*),(SELECT AVG(salario) FROM empleado) AS salario_promedio FROM empleado
WHERE salario > (SELECT AVG(salario) FROM empleado)
GROUP BY pais ORDER BY COUNT(*) DESC;