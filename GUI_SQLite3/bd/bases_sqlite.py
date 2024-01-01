import sqlite3
import os
from datetime import datetime
import shutil
import glob

# Variables globales

carpeta_principal = os.path.dirname(__file__)

carpeta_respaldo = os.path.join(carpeta_principal, "respaldos")

carpeta_bases = os.path.join(carpeta_principal,"Bases")

# Clase BaseDatos

class BaseDatos:

    def todo(nombre_bd, sql):
        base = sqlite3.connect(os.path.join(carpeta_bases,nombre_bd))
        cursor = base.cursor()
        try:
            cursor.execute(sql)
            resultado = cursor.fetchall()
            print(resultado)
            return resultado
        except Exception as e:
            print(e)
            raise e
        finally:
            if base:
                base.close()

    def consulta(nombre_bd, nombre_tabla, campo, condicion):
        base = sqlite3.connect(os.path.join(carpeta_bases,nombre_bd))
        cursor = base.cursor()
        try:
            cursor.execute(f"select * from {nombre_tabla} where {campo}=:c", {"c": f"{condicion}"})
            resultado = cursor.fetchall()
            print(resultado)
            return resultado
        except Exception as e:
            print(e)
            raise e
        finally:
            if base:
                base.close()

    # Mostrar bases de datos del servidor
    def mostrar_bd():
        try:
            print("Aquí tiene las bases de datos:")
            bases = glob.glob(os.path.join(carpeta_bases, "*.db"))
            for base in bases:
                nombre_archivo = os.path.basename(base)
                print("-", nombre_archivo)
            return bases
        except Exception as e:
            print(e)
            raise e
        
    # Eliminar bases de datos
    def eliminar_bd(nombre_bd):
        try:
            os.remove(f"{os.path.join(carpeta_bases, nombre_bd)}")
            print("Base eliminada correctamente")
        except Exception as e:
            print(e)
            raise e

    # Crear bases de datos
    def crear_bd(nombre_bd):
        try:
            conexion = sqlite3.connect(os.path.join(carpeta_bases,nombre_bd))
            print(f"Se creó la base de datos {nombre_bd} o ya estaba creada.")
        except Exception as e:
            print(f"Ocurrió un error al intentar crear la base de datos {nombre_bd}: {e}")
        finally :
            if conexion:
                conexion.close()

    # Crear tablas en una base de datos
    def crear_tabla(nombre_bd, nombre_tabla, columnas):
        try:
            base = sqlite3.connect(os.path.join(carpeta_bases,nombre_bd))
            cursor = base.cursor()
            cursor.execute(f"create table {nombre_tabla} {columnas}")
            base.commit()
            print(f"Se creó la tabla {nombre_tabla} en la base de datos {nombre_bd} con las columnas {columnas}.")
        except Exception as e:
            print(f"Ocurrió un error al intentar crear la tabla {nombre_tabla} en la base de datos {nombre_bd}: {e}")
        finally :
            if base:
                base.close()

    # Método para mostrar tablas de una base de datos
    def mostrar_tablas(nombre_bd):
        try:
            base = sqlite3.connect(os.path.join(carpeta_bases,nombre_bd))
            sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
            cursor = base.cursor()
            cursor.execute(sql_query)
            print(f"Lista de tablas en la base de datos{nombre_bd}")
            resultado = cursor.fetchall()
            print(resultado)
            for tabla in resultado:
                print("-", tabla[0])
            return resultado
        except Exception as e:
            print(f"Error retrieving tables: {e}")
            raise e
        finally: 
            if base:
                base.close()

    # Método para mostrar columnas de una tabla
    def mostrar_columnas(nombre_bd, nombre_tabla):
        try:
            base = sqlite3.connect(os.path.join(carpeta_bases,nombre_bd))
            cursor = base.cursor()
            resultado = cursor.execute(f'''SELECT * FROM {nombre_tabla}''')
            print(f"Aquí tiene las columnas de la tabla {nombre_tabla} de la base {nombre_bd}:")
            columnas = []
            for column in resultado.description:
                print(column[0])
                columnas.append(column[0])
            print(columnas)
            return columnas
        except Exception as e:
            print(f"Ocurrió un error, comprueba el nombre de la tabla: {e}")
        finally:
            if base:
                base.close()

    # Método para insertar registros en una tabla
    def insertar_registros(nombre_bd, nombre_tabla, registros):
        try: 
            base = sqlite3.connect(os.path.join(carpeta_bases,nombre_bd))
            cursor = base.cursor()

            if not registros:  # Si la lista está vacía
                print("La lista de registro está vacía.")
                return

            # Construct the placeholder string for the columns
            columnas = ",".join(["?" for _ in range(len(registros[0]))])

            # Construct the SQL query with placeholders
            query = f"INSERT INTO {nombre_tabla} VALUES ({columnas})"

            # Execute the query with the provided records
            cursor.executemany(query, registros)
            base.commit()

            print("Registro añadido a la tabla.")
        except Exception as e:
            print(e)
            raise e
        finally:
            if base:
                base.close()


    # Método para insertar registros en una tabla
    def insertar_1registro(nombre_bd, nombre_tabla, registro):
        try: 
            base = sqlite3.connect(os.path.join(carpeta_bases, nombre_bd))
            cursor = base.cursor()

            if not registro:  # Si la lista está vacía
                print("La lista de registro está vacía.")
                return

            # Construct the placeholder string for the columns
            columnas = ",".join(["?" for _ in range(len(registro))])

            # Print the number of columns and the constructed column string
            print(f"Number of columns in table: {len(registro)}")
            print(f"Column string: {columnas}")

            # Construct the SQL query with placeholders
            query = f"INSERT INTO {nombre_tabla} VALUES ({columnas})"
            
            # Print the constructed SQL query
            print(f"SQL Query: {query}")

            # Execute the query with the provided records
            cursor.execute(query, registro)
            base.commit()

            print("Registro añadido a la tabla.")
        except Exception as e:
            print(e)
            raise e
        finally:
            if base:
                base.close()

    def eliminar_registro_por_campo(nombre_bd, nombre_tabla, campo, condicion):
        try:
            base = sqlite3.connect(os.path.join(carpeta_bases, nombre_bd))
            cursor = base.cursor()
            if not campo:
                print("No ha indicado un campo a través del cual buscar el registro a eliminar")
                return
            if not condicion:  # Si la lista está vacía
                print("No ha indicado una condicion.")
                return
            
            cursor.execute(f"DELETE FROM {nombre_tabla} WHERE {campo} = {condicion}")
            base.commit()
            print("Registro eliminado de la tabla.")

        except Exception as e:
            print(f"Error deleting record: {e}")
            base.rollback()
            raise e
        
        finally : 
            if base:
                base.close()

    def vaciar_tabls(nombre_bd, nombre_tabla):
            base = sqlite3.connect(os.path.join(carpeta_bases, nombre_bd))
            cursor = base.cursor()
            
            try:
                cursor.execute(f"DELETE FROM {nombre_tabla}")
                base.commit()
                print("Registro eliminado de la tabla.")

            except Exception as e:
                print(f"Error deleting record: {e}")
                base.rollback()
                raise e
            
            finally : 
                if base:
                    base.close()

    # Método para realizar copias de seguridad de bases de datos
    def crear_copia_seguridad(nombre_bd):
        try:
            base = os.path.join(carpeta_bases, nombre_bd)
            # Obtenemos la fecha y hora actuales
            fecha_hora = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

            # Creamos el nombre del archivo de copia de seguridad
            nombre_archivo = f"{nombre_bd}_{fecha_hora}.db"

            # Creamos el directorio de copias de seguridad si no existe
            if not os.path.exists(carpeta_respaldo):
                os.mkdir(carpeta_respaldo)

            # Copiamos el archivo de la base de datos al directorio de copias de seguridad
            shutil.copyfile(f"{base}.db", os.path.join(carpeta_respaldo, nombre_archivo))

            print(f"Copia de seguridad de la base de datos '{nombre_bd}' creada correctamente en '{carpeta_respaldo}/{nombre_archivo}'.")
        except Exception as e:
            print(e)
            raise e

    # Método para actualizar registros en una tabla
    def actualizar_registro(nombre_bd, nombre_tabla, campos, valores):
        try:
            base = sqlite3.connect(os.path.join(carpeta_bases, nombre_bd))
            cursor = base.cursor()
            sql = f"UPDATE {nombre_tabla} SET {campos} WHERE {valores}"
            cursor.execute(sql)
            base.commit()
            print("Registro actualizado en la tabla.")

        except Exception as e:
            print(f"Error updating record: {e}")
            raise e
        
        finally:
            if base:
                base.close()

    def eliminar_tabla(nombre_bd, nombre_tabla):
        try:
            base = sqlite3.connect(os.path.join(carpeta_bases, nombre_bd))
            cursor = base.cursor()
            sql = f"DROP TABLE {nombre_tabla}"
            cursor.execute(sql)
            base.commit()
            print("Tabla eliminada correctamente.")

        except Exception as e:
            print(f"Error updating record: {e}")
            raise e
        
        finally:
            if base:
                base.close()