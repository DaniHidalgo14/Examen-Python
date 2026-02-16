#CAMBIAR RUTA PARA QUE FUNCIONE LA BD
DB_PATH = r"C:\Users\Dani\PycharmProjects\Examen-Python\database\biblioteca.db"

CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS libros (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn              TEXT    NOT NULL UNIQUE CHECK(length(isbn) = 10),
    titulo            TEXT    NOT NULL,
    anio              INTEGER NOT NULL CHECK(anio BETWEEN 1500 AND 2026),
    fecha_adquisicion DATE    NOT NULL,
    prestado          INTEGER NOT NULL DEFAULT 0 CHECK(prestado IN (0, 1)),
    numero_usuario    INTEGER,
    fecha_prestamo    DATE
);'''

CARGA_INICIAL = '''-- 1. El Quijote (disponible)
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0306406152', 'El Quijote De La Mancha', 1605, '2023-03-15', 0, NULL, NULL);

-- 2. Cien Años de Soledad (prestado, vigente)
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0140157514', 'Cien Años De Soledad', 1967, '2023-05-20', 1, 1001, '2026-02-10');

-- 3. La Sombra del Viento (disponible)
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0143034901', 'La Sombra Del Viento', 2001, '2023-07-10', 0, NULL, NULL);

-- 4. 1984 (prestado, VENCIDO)
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0451524934', '1984', 1949, '2022-11-01', 1, 1002, '2025-12-01');

-- 5. El Principito (disponible)
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0156012197', 'El Principito', 1943, '2024-01-20', 0, NULL, NULL);

-- 6. Rayuela (prestado, VENCIDO)
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0394752848', 'Rayuela', 1963, '2023-09-05', 1, 1003, '2025-11-15');

-- 7. La Casa De Los Espíritus (disponible)
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0553273914', 'La Casa De Los Espiritus', 1982, '2024-06-12', 0, NULL, NULL);

-- 8. Ficciones (prestado, vigente)
INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)
VALUES ('0802130305', 'Ficciones', 1944, '2024-03-28', 1, 1004, '2026-02-05');'''

SELECT_ALL = '''select * from libros'''

INSERT_LIBRO = '''insert into libros(isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo) values(?, ?, ?, ?, ?, ?, ?);'''

SELECT_LIBRO = '''select * from libros where anio = ?'''

SELECT_DISPONIBLES = '''select * from libros where prestado = ?'''

UPDATE_LIBRO = '''update libros set titulo = ?, anio = ?, fecha_adquisicion = ?, prestado = ?, numero_usuario = ?, fecha_prestamo = ? where id = ?'''

DELETE_LIBRO = '''delete from libros where id = ?'''