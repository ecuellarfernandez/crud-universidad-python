# SELECT
GET_ALL_SUBJECTS = "SELECT * FROM materias"
GET_SUBJECT_BY_ID = "SELECT * FROM materias WHERE id = %s"
GET_SUBJECT_BY_NAME = "SELECT * FROM materias WHERE nombre LIKE %s"
# UPDATE
UPDATE_SUBJECT = "UPDATE materias SET codigo = %s, nombre = %s, creditos = %s WHERE id = %s"
# DELETE
DELETE_SUBJECT = "DELETE FROM materias WHERE id = %s"
# INSERT
INSERT_SUBJECT = "INSERT INTO materias (codigo, nombre, creditos) VALUES (%s, %s, %s)"

#STUDENT

GET_SUBJECTS_BY_STUDENT = "SELECT m.* FROM materias m JOIN inscripciones i ON m.id = i.materia_id WHERE i.estudiante_id = %s"
GET_SUBJECTS_BY_STUDENT_NAME = "SELECT m.* FROM materias m JOIN inscripciones i ON m.id = i.materia_id JOIN estudiantes e ON i.estudiante_id = e.id WHERE e.nombre_completo LIKE %s"