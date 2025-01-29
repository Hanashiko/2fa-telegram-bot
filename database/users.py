from database.connection import get_connection, close_connection, execute_query, execute_query_fetchone, execute_query_fetchall

class UsersManager:
	@staticmethod
	def create_table():
		query = """
		create table if not exists users (
			id bigint primary key,
			code varchar(33)
		) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
		"""
		execute_query(query)

	@staticmethod
	def delete_table():
		query = "drop table if exists users"
		execute_query(query)

	@staticmethod
	def add(id):
		query = "insert into users (id) values (%s)"
		values = (id,)
		execute_query(query,values)

	@staticmethod
	def delete(id):
		query = "delete from users where id = %s"
		values = (id,)
		execute_query(query, values)

	@staticmethod
	def edit(id, code):
		query = "update users set code = %s where id = %s"
		values = (code, id)
		execute_query(query,values)

	@staticmethod
	def get(id):
		query = "select id, code from users where id = %s"
		values = (id,)
		result = execute_query_fetchone(query,values)
		return result

	@staticmethod
	def get_all():
		query = "select id, code from users"
		result = execute_query_fetchall(query)
		return result

	@staticmethod
	def user_exists(name, surname):
		query = "SELECT COUNT(*) FROM users WHERE name = %s AND surname = %s"
		values = (name, surname,)
		result = execute_query_fetchone(query,values)
		return result[0] > 0