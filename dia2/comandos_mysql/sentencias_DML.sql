-- SENTENCIAS DML
-- CRUD
-- C - INSERT
-- R - SELECT
-- U - UPDATE
-- D - DELETE

--INSERT
insert into alumno(nro_documento,nombre) values('100','cesar mayta');
-- INSERTAR VARIOS REGISTROS
insert into alumno(nro_documento,nombre)
VALUES
('200','Ana Martinez'),
('300','Luis Lopez'),
('400','Arturo Gonzales'),
('500','Monica Tejada'),
('600','Raul Rivera'),
('700','Andrea Valencia'),
('800','Sofia Mamani'),
('900','Carlos Perez'),
('1000','Jesus Concha');

-- ACTUALIZAR DATOS(UPDATE)

update alumno SET
email = 'codigo@gmail.com';
-- UPDATE CON WHERE
update alumno 
set email='cesar@gmail.com' where id = 1;
-- UPDATE CON FUNCIONES
update alumno
set email = CONCAT(lower(replace(nombre,' ' ,'.')),'@gmail.com') where id > 1;

-- SELECT
select * from alumno;
select nombre,email from alumno;
select nombre from alumno where id > 5;
select * from alumno order by nombre asc;

-- DELETE
delete from alumno where id = 3;
truncate table alumno;