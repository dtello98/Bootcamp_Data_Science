use db_g6;

-- FUNCIONES DE AGRUPACIÓN
select max(salario) from empleado;
select min(salario) from empleado;
select avg(salario) from empleado;

select max(salario),min(salario),avg(salario)
from empleado;

select DISTINCT pais from empleado;

-- seleccionar el total de empleado por pais
select pais,count(*) from empleado
group by pais
order by count(*) desc;

select pais,area,
count(*),max(salario),min(salario),avg(salario)
from empleado
where salario > 5000
group by pais,area
order by pais,area;

select pais,count(*)
from empleado
group by pais
having count(*) > 100;