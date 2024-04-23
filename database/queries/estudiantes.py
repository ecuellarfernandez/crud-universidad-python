GET_ALL_STUDENTS = "SELECT * FROM estudiantes"
GET_STUDENT_BY_ID = "SELECT * FROM estudiantes WHERE id = %s"
GET_STUDENT_BY_NAME = "SELECT * FROM estudiantes WHERE nombre_completo LIKE %s"
#UPDATE
UPDATE_STUDENT = "UPDATE estudiantes SET nombre_completo = %s, fecha_nacimiento = %s, carrera = %s WHERE id = %s"
#DELETE
DELETE_STUDENT = "DELETE FROM estudiantes WHERE id = %s"
#INSERT
INSERT_STUDENT = "INSERT INTO estudiantes (nombre_completo, fecha_nacimiento, carrera) VALUES (%s, %s, %s)"