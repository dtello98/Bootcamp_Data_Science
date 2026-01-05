SELECT
nombre,salario,
CASE 
    WHEN salario >= 5000  THEN 'ALTO'
    WHEN salario >= 3000 THEN 'MEDIO'  
    ELSE 'BAJO'
END as nivel_salarial
from empleado;

--clasificar empleados por nacional y extranjero
select nombre,pais,
CASE 
    WHEN pais = 'Peru' THEN 'NACIONAL'  
    ELSE  'EXTRANJERO'
END as tipo_empleado
from empleado;