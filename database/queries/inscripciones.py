# SELECT
GET_ALL_ENROLLMENTS = "SELECT * FROM inscripciones"
GET_ENROLLMENT_BY_STUDENT_ID = "SELECT * FROM inscripciones WHERE estudiante_id = %s"
GET_SUBJECTS_BY_STUDENT_ID = "SELECT m.* FROM inscripciones i JOIN materias m ON i.materia_id = m.id WHERE i.estudiante_id = %s"
# UPDATE
UPDATE_ENROLLMENT = "UPDATE inscripciones SET estudiante_id = %s, materia_id = %s WHERE estudiante_id = %s AND materia_id = %s"
# DELETE
DELETE_ENROLLMENT = "DELETE FROM inscripciones WHERE estudiante_id = %s AND materia_id = %s"
# INSERT
INSERT_ENROLLMENT = "INSERT INTO inscripciones (estudiante_id, materia_id) VALUES (%s, %s)"