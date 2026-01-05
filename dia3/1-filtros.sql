-- FILTROS
select * from empleado where pais ='Peru';
select * from empleado where salario > 5000;
select * from empleado where salario > 5000 and pais = 'Peru';
select * from empleado
where salario > 5000
and (pais = 'Peru' or pais = 'Colombia');
select * from empleado
where pais in ('Chile','Argentina');
select * from empleado
where salario between 10000 and 15000;