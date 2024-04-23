# SELECT
GET_ALL_GRADES = "SELECT * FROM notas"
GET_GRADES_BY_STUDENT_ID_SUBJECT_ID = "SELECT * FROM notas WHERE estudiante_id = %s AND materia_id = %s"
GET_AVERAGE_GRADE_BY_STUDENT_ID_SUBJECT_ID = "SELECT AVG(nota) FROM notas WHERE estudiante_id = %s AND materia_id = %s"
# UPDATE
UPDATE_GRADE = "UPDATE notas SET fecha = %s, nota = %s WHERE estudiante_id = %s AND materia_id = %s AND fecha = %s"
# DELETE
DELETE_GRADE = "DELETE FROM notas WHERE estudiante_id = %s AND materia_id = %s"
# INSERT
INSERT_GRADE = "INSERT INTO notas (estudiante_id, materia_id, fecha, nota) VALUES (%s, %s, %s, %s)"