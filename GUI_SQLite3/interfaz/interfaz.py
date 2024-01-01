import ttkbootstrap as tkb
# no va from ttkbootstrap.dialogs import Messagebox as tkm
from tkinter import messagebox
from tkinter.simpledialog import askinteger, askstring
import bd.bases_sqlite as bd
import sqlite3 as sql3
import os
from PIL import Image, ImageTk, ImageSequence

# rutas
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")

# objeto para manejar bases
bases = bd.BaseDatos()

class Login:
    def __init__(self):
        # definición ventana principal
        self.root = tkb.Window(title="Gestor bases de datos SQLite", themename="darkly")
        # insertar logo
        self.root.geometry("550x370")

        # contenido ventana usuarios creados: Carlos Mymadrid1$ y Carlos1 Mymadrid1$

        # logo imágenes
        logo_path = os.path.join(carpeta_imagenes, "logo.jpg")
        original_image = Image.open(logo_path)

        # Resize the image to your desired dimensions
        resized_image = original_image.resize((150, 370))

        logo_photo = ImageTk.PhotoImage(resized_image)

        self.image = tkb.Label(self.root, image=logo_photo)
        self.image.image = logo_photo  # This line is necessary to prevent the image from being garbage collected
        self.image.grid(row=0, column=0, rowspan=8, columnspan=2)

        label1 = tkb.Label(self.root, text="Indique su usuario", style="superhero", font=("Helvetica", 16), bootstyle="light", foreground="gray")
        label1.grid(row=1, column=3, columnspan=2, padx=10, pady=4)
        usuario = tkb.Entry(self.root, font=("Helvetica", 18), foreground="gray", width=30, bootstyle="light", background="gray")
        usuario.grid(row=2, column=3, columnspan=2, padx=10, pady=4)

        label2 = tkb.Label(self.root, text="Indique su contraseña", style="light", font=("Helvetica", 16), bootstyle="dark", foreground="gray")
        label2.grid(row=3, column=3, columnspan=3, padx=10, pady=4)
        contraseña = tkb.Entry(self.root, font=("Helvetica", 18), foreground="gray", width=30, bootstyle="light", background="gray", show="*")
        contraseña.grid(row=4, column=3, columnspan=2, pady=4, padx=10)

        label3 = tkb.Label(self.root, text="¿No tienes cuenta?", style="light", font=("Helvetica", 14), bootstyle="light", foreground="gray")
        label3.grid(row=6, column=3, padx=10, pady=4)

        creacion_cuenta = tkb.Button(self.root, text="Crea tu cuenta aquí", bootstyle="light-link", command=lambda : crear_cuenta())
        creacion_cuenta.grid(row=6, column=4, padx=10, pady=4)

        entrar = tkb.Button(self.root, text="Entrar", style="light", width=5, command= lambda : validar())
        entrar.grid(row=5, column=4, padx=10, pady=4)

        #lógica
        def validar():
            user = usuario.get()
            password = contraseña.get()

            print(user,password)

            user = usuario.get()
            password = contraseña.get()

            busqueda = bd.BaseDatos.consulta("Usuarios.db", "usuarios", "nombre", f"{user}")
            mensaje = tkb.Label(self.root, text="Usuario o contraseña incorrectos", style="light", font=("Helvetica", 14), bootstyle="light", foreground="gray")
            mensaje.grid(row=5, column=3, padx=10, pady=10)

            if not busqueda :
                mensaje.configure(text="Usuario o contraseña incorrectos")
                print("Usuario incorrecto")
                return
            elif busqueda[0][3] != password :
                mensaje.configure(text="Usuario o contraseña incorrectos")
                print("Contraseña incorrecta")
                return
            else :
                mensaje.configure(text=f"Bienvenido {user}")
                print("Login correcto")
                self.root.destroy()
                ventana_opciones = VentanaOpciones()
                return
                
        def crear_cuenta():
            print("Crear cuenta")
            create_account = Create_account()

        self.root.mainloop()

class Create_account: #clase para crear cuentas nuevas
    def __init__(self):
        self.create = tkb.Toplevel(title="Ventana de creación de cuenta")
        self.create.geometry("550x450")

        #contenido
        entrada_usuario = tkb.Label(self.create, text="Indique su nombre de usuario", style="superhero", font=("Helvetica", 16), bootstyle="light", foreground="gray")
        entrada_usuario.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        new_user = tkb.Entry(self.create,  font=("Helvetica", 18), foreground="gray", width=30, bootstyle="light", background="gray")
        new_user.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        entrada_apellido = tkb.Label(self.create, text="Indique su apellido", style="superhero", font=("Helvetica", 16), bootstyle="light", foreground="gray")
        entrada_apellido.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        new_apellido = tkb.Entry(self.create, font=("Helvetica", 18), foreground="gray", width=30, bootstyle="light", background="gray")
        new_apellido.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        contra = tkb.Label(self.create, text="Indique su contraseña", style="superhero", font=("Helvetica", 16), bootstyle="light", foreground="gray")
        contra.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
        new_contra = tkb.Entry(self.create, font=("Helvetica", 18), foreground="gray", width=30, bootstyle="light", background="gray")
        new_contra.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

        confirm_contra = tkb.Label(self.create, text="Confirme su contraseña", style="superhero", font=("Helvetica", 16), bootstyle="light", foreground="gray")
        confirm_contra.grid(row=6, column=0, padx=10, pady=10, columnspan=2)
        new_confirm_contra = tkb.Entry(self.create,  font=("Helvetica", 18), foreground="gray", width=30, bootstyle="light", background="gray", show="*")
        new_confirm_contra.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

        mensaje_estandar = tkb.Label(self.create, text="", style="superhero", font=("Helvetica", 16), bootstyle="light", foreground="gray")
        mensaje_estandar.grid(row=8, column=0, padx=10, pady=10, rowspan=2)

        boton_crear = tkb.Button(self.create, text="Crear cuenta", style="light", width=10, command= lambda : crear())
        boton_crear.grid(row=8, column=1, padx=10, pady=10)

        def crear():
            nuevo_usuario = new_user.get()
            nuevo_apellido = new_apellido.get()
            nueva_conta = new_contra.get()
            confirma = new_confirm_contra.get()
            if nueva_conta != confirma :
                mensaje_estandar.configure(text="La contraseña y la confirmación no coinciden")
                return
            busqueda = bd.BaseDatos.todo("Usuarios.db", "select * from usuarios")
            print(busqueda)
            if not busqueda:
                id = 1
            else:
                id = max(item[0] for item in busqueda) + 1
            registro = (id, f"{nuevo_usuario}", f"{nuevo_apellido}", f"{nueva_conta}")
            unico = bd.BaseDatos.consulta("Usuarios.db", "usuarios", "nombre", f"{nuevo_usuario}")
            if not unico == [] :
                mensaje_estandar.configure(text="Nombre de usuario ya existente")
                print(unico)
                return
            else:
                bd.BaseDatos.insertar_1registro("Usuarios.db", "usuarios", registro)
                mensaje_estandar.configure(text="Usuario creado correctamente, puede cerrar esta ventana")

        self.create.mainloop()

class FuncionesPrograma:
    def ventana_consultas(self):
        ventana = tkb.Toplevel(title="Ventana de consultas", resizable=(False,False))
        ventana.geometry("600x450")

        label_base = tkb.Label(ventana, text="Indique el nombre de la base de datos ", )
        label_base.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        base = tkb.Entry(ventana, bootstyle="light", width=20)
        base.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        label_tabla = tkb.Label(ventana, text="Indique el nombre de la tabla", )
        label_tabla.grid(row=0, column=2, padx=10, pady=10, columnspan=2)
        tabla = tkb.Entry(ventana, bootstyle="light", width=20)
        tabla.grid(column=2, row=1, columnspan=2, padx=10, pady=10)

        label_campo = tkb.Label(ventana, text="Indique el campo en el que hacer la búsqueda ", )
        label_campo.grid(column=0, row=2, padx=10, pady=10, columnspan=2)
        campo = tkb.Entry(ventana, bootstyle="light", width=20)
        campo.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        label_condicion = tkb.Label(ventana, text="Indique la condición de búsqueda", )
        label_condicion.grid(row=2, column=2, padx=10, pady=10, columnspan=2)
        condicion = tkb.Entry(ventana, bootstyle="light", width=20)
        condicion.grid(column=2, row=3, columnspan=2, padx=10, pady=10)

        boton_enviar = tkb.Button(ventana,
                                  width=5,
                                  text="Enviar",
                                  command= lambda: enviar())
        boton_enviar.grid(row=4, column=3, padx=10, pady=10)

        boton_borrar = tkb.Button(ventana,
                                  width=5,
                                  text="Borrar",
                                  command= lambda: borrar())
        boton_borrar.grid(row=5, column=3, padx=10, pady=10)

        texto = tkb.Text(ventana,
                         width=40,
                         height=10)
        texto.grid(row=4, column=0, columnspan=3, rowspan=3, padx=10, pady=10)

        boton_volver = tkb.Button(ventana,
                                  width=5,
                                  text="Volver",
                                  command= lambda: volver())
        boton_volver.grid(row=6, column=3, padx=10, pady=10)

        def enviar():
            try:
                #borra el contenido de "texto"
                texto.delete('1.0', 'end')
                bases = base.get()
                # obtiene el contenido del entry
                tablas = tabla.get()
                condiciones = condicion.get()
                campos = campo.get()
                # llama al método base_datos.consulta() con los datos como argumento
                resultado = bd.BaseDatos.consulta(f"{bases}", f"{tablas}", f"{campos}", f"{condiciones}")
                print(resultado)

                if resultado == []:
                    texto.insert('end', "Ningún registro encontrado")
                else:
                    for registro in resultado:
                        texto.insert('end', registro)
                        texto.insert('end', '\n')
                    # Actualiza el contador de registros devueltos
                    numero_registros = len(resultado)
                    
                    label1 = tkb.Label(ventana, text="Registros devueltos: ", )
                    label1.grid(row=7, column=0, padx=10, pady=10)

                    label2 =tkb.Label(ventana, text=f"{numero_registros}", )
                    label2.grid(row=8, column=0, padx=10, pady=10)
                    datos = ""
            except Exception as e:
                label1 = tkb.Label(ventana, text="¡Ooops!", )
                label1.grid(row=7, column=0, padx=10, pady=10, columnspan=3)

                label2 =tkb.Label(ventana, text=f"Ha sucedido el siguiente error: {e}", )
                label2.grid(row=8, column=0, padx=10, pady=10, columnspan=3)
                messagebox.showerror("Error", e)
                #tkm.show_error(message=f"Ha ocurrido el siguiente error: {e}", title="Error", parent=ventana, alert=True)
        
        def volver():
            ventana.destroy()

        def borrar():
            #borra todo el contenido 
            texto.delete('1.0', 'end')

        ventana.mainloop()

    def ventana_mostrar_bases_datos(self):
        ventana = tkb.Toplevel(title="Ventana para ver bases de datos", resizable=(False, False))
        ventana.geometry("550x250")
        texto = tkb.Text(ventana,
                         width=40,
                         height=12)
        texto.grid(row=0, column=0, padx=10, pady=10, rowspan=4, columnspan=2)

        boton_ver = tkb.Button(ventana, text="Ver bases", width=8, command= lambda: ver())
        boton_ver.grid(row=2, column=2, padx=10, pady=10)

        boton_volver = tkb.Button(ventana, text="Volver", width=8, command= ventana.destroy)
        boton_volver.grid(row=3, column=2, padx=10, pady=10)

        def ver():
            bases = bd.BaseDatos.mostrar_bd()
            texto.insert('end', 'Aquí tiene las bases de datos:')
            texto.insert('end', '\n')
            for base in bases :
                nombre_archivo = os.path.basename(base)
                texto.insert('end', nombre_archivo)
                texto.insert('end', '\n')

        ventana.mainloop()
    
    def ventana_eliminar_bases_datos(self):
        ventana = tkb.Toplevel(title="Ventana para eliminar bases de datos", resizable=(False, False))
        ventana.geometry("750x55")

        base = tkb.Entry(ventana,
                         bootstyle="light",
                         width=50)
        base.grid(row=0, column=0, padx=10, pady=10)

        def eliminar():
            try:
                bases = base.get()
                nombre = f"{bases}"+".db"
                bd.BaseDatos.eliminar_bd(nombre)
                messagebox.showinfo("Info", f"{nombre} eliminada correctamente")
            except Exception as e:
                print(e)
                messagebox.showerror("Error", e)

        enviar = tkb.Button(ventana, text="Eliminar", command= lambda: eliminar() )
        enviar.grid(row=0, column=1, padx=10, pady=10)

        tkb.Button(ventana, text="Volver", command= lambda: ventana.destroy()).grid(row=0, column=2, padx=10, pady=10)

        ventana.mainloop()

    
    def ventana_crear_bases_datos(self):
        ventana = tkb.Toplevel(title="Ventana para crear bases de datos", resizable=(False, False))
        ventana.geometry("900x150")

        name = tkb.Entry(ventana,
                         bootstyle="light",
                         width=50)
        name.grid(row=1, column=0, padx=10, pady=10)

        tkb.Label(ventana, text="Indique el nombre de la nueva base de datos:").grid(row=0, column=0, padx=10, pady=10)

        tkb.Button(ventana, text="Crear base de datos", command= lambda: crear()).grid(row=1, column=1, padx=10, pady=10)

        tkb.Button(ventana, text="Volver", command= lambda: ventana.destroy()).grid(row=1, column=2, padx=10, pady=10)

        def crear():
            base = name.get()
            nombre = f"{base}"+".db"
            try:
                bd.BaseDatos.crear_bd(f"{nombre}")
                tkb.Label(ventana, text="Se ha creado la base correctamente o ya existía").grid(row=2, column=0, columnspan=3, padx=10, pady=10)
            except Exception as e:
                tkb.Label(ventana, text=f"Ocurrió el siguiente error: {e}").grid(row=2, column=0, columnspan=3, padx=10, pady=10)
                messagebox.showerror("Error", {e})

        ventana.mainloop()
    
    def ventana_crear_respaldos(self):
        ventana = tkb.Toplevel(title="Ventana para crear copias de seguridad", resizable=(False, False))
        ventana.geometry("900x150")

        name = tkb.Entry(ventana,
                         bootstyle="light",
                         width=50)
        name.grid(row=1, column=0, padx=10, pady=10)

        tkb.Label(ventana, text="Indique el nombre de la base de datos:").grid(row=0, column=0, padx=10, pady=10)

        tkb.Button(ventana, text="Crear base copia", command= lambda: crear()).grid(row=1, column=1, padx=10, pady=10)

        tkb.Button(ventana, text="Volver", command= lambda: ventana.destroy()).grid(row=1, column=2, padx=10, pady=10)

        def crear():
            base = name.get()
            nombre = f"{base}"
            try:
                bd.BaseDatos.crear_copia_seguridad(f"{nombre}")
                tkb.Label(ventana, text="Se ha creado la copia de seguridad correctamente").grid(row=2, column=0, columnspan=3, padx=10, pady=10)
            except Exception as e:
                tkb.Label(ventana, text=f"Ocurrió el siguiente error: {e}").grid(row=2, column=0, columnspan=3, padx=10, pady=10)
                messagebox.showerror("Error", {e})

        ventana.mainloop()
    
    def ventana_crear_tablas(self):
        numero_columnas = askinteger("Número de columnas", "¿Cuántas columnas quiere que tenga su tabla?")
        #print(numero_columnas)

        FuncionesPrograma.creacion(numero_columnas)
                
    def ventana_eliminar_tablas(self):
        ventana = tkb.Toplevel("Ventana para eliminar tablas")
        ventana.geometry("500x300")

        tkb.Label(ventana, text="Indique el nombre de la base de datos:", style="light").grid(row=0, column=0, padx=5, pady=5)
        base = tkb.Entry(ventana, style="light", width=30)
        base.grid(row=0, column=1, padx=5, pady=5)

        tkb.Label(ventana, text="Indique el nombre de la tabla a eliminar:", style="light").grid(row=1, column=0, padx=5, pady=5)
        tabla = tkb.Entry(ventana, style="light", width=30)
        tabla.grid(row=1, column=1, padx=5, pady=5)

        tkb.Button(ventana, text="Eliminar", command= lambda: eliminar()).grid(row=2, column=1, padx=5, pady=5)

        tkb.Button(ventana, text="Volver", command= lambda: ventana.destroy()).grid(row=3, column=1, padx=5, pady=5)

        def eliminar():
            bases = f"{base.get()}.db"
            nombre = tabla.get()
            if bases == ".db" or not nombre:
                messagebox.showerror("Error", "No ha indicado una base y/o tabla")
                return
            try:
                bd.BaseDatos.eliminar_tabla(bases, nombre)
                messagebox.showinfo("Éxito", f"La tabla {nombre} ha sido eliminada correctamente de la base {bases}")
            
            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"Ha suceedido el siguiente error: {e}")
    
    def ventana_mostrar_tablas(self):
        ventana = tkb.Toplevel("Ventana para mostrar tablas")
        ventana.geometry("600x300")

        tkb.Label(ventana, text="Indique la base de datos de la que quiere conocer las tablas", style="light", borderwidth=0).grid(row=0, column=0, padx=5, pady=5, columnspan=3)

        bases = tkb.Entry(ventana, width=30, style="light")
        bases.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        texto = tkb.Text(ventana, width=60, height=10)
        texto.grid(row=2, column=0, columnspan=4, padx=5, pady=5, rowspan=5)

        tkb.Button(ventana, text="Mostrar Tablas", style="light", command= lambda: mostrar()).grid(row=1, column=2, padx=5, pady=5)

        tkb.Button(ventana, text="Volver", style="light", command= lambda: ventana.destroy()).grid(row=1, column=3, padx=5, pady=5)

        def mostrar():
            texto.delete('1.0', 'end')
            base = f"{bases.get()}.db"
            if base == ".db":
                messagebox.showerror("Error", "No ha indicado una base de datos")
                return
            
            try:
                tablas = bd.BaseDatos.mostrar_tablas(base)

                if tablas ==[ ]:
                    texto.insert('end', 'La base de datos no contiene tablas')
                
                else:
                    texto.insert('end', f'A continuación encontrará las tablas de la base de datos {base}:')
                    texto.insert('end', '\n')
                    for tabla in tablas:
                        texto.insert('end', f'-{tabla[0]}')
                        texto.insert('end', '\n')
            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"Ha sucedido el siguiente error: {e}")

        ventana.mainloop()
    
    def ventana_mostrar_columnas(self):
        ventana = tkb.Toplevel("Ventana para mostrar columnas")
        ventana.geometry("600x300")

        tkb.Label(ventana, text="Indique la base de datos ", style="light", borderwidth=0).grid(row=0, column=0, padx=5, pady=5, columnspan=3)

        bases = tkb.Entry(ventana, width=30, style="light")
        bases.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        tkb.Label(ventana, text="Indique la tabla de la que quiere conocer las columnas", style="light", borderwidth=0).grid(row=2, column=0, padx=5, pady=5, columnspan=3)

        tablas = tkb.Entry(ventana, width=30, style="light")
        tablas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        texto = tkb.Text(ventana, width=60, height=10)
        texto.grid(row=4, column=0, columnspan=4, padx=5, pady=5, rowspan=5)

        tkb.Button(ventana, text="Mostrar Columnas", style="light", command= lambda: mostrar()).grid(row=1, column=2, padx=5, pady=5)

        tkb.Button(ventana, text="Volver", style="light", command= lambda: ventana.destroy()).grid(row=1, column=3, padx=5, pady=5)

        def mostrar():
            texto.delete('1.0', 'end')
            base = f"{bases.get()}.db"
            tabla = f"{tablas.get()}"
            if base == ".db" or tabla == []:
                messagebox.showerror("Error", "No ha indicado una base de datos y/o una tabla")
                return
            
            try:
                columnas = bd.BaseDatos.mostrar_columnas(base, tabla)

                if columnas ==[ ]:
                    texto.insert('end', 'La tabla no contiene columnas')
                
                else:
                    texto.insert('end', f'A continuación encontrará las tablas de la base de datos {base}:')
                    texto.insert('end', '\n')
                    for columna in columnas:
                        texto.insert('end', f'-{columna}')
                        texto.insert('end', '\n')
            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"Ha sucedido el siguiente error: {e}")

        ventana.mainloop()
    
    def ventana_insertar_registros(self):
        ventana = tkb.Toplevel("Ventana para insertar múltiples registros")
        ventana.geometry("500x400")

        tkb.Label(ventana, text="Indique el nombre de la base de datos", style="light").grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        bases = tkb.Entry(ventana, width=30, style="light")
        bases.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        tkb.Label(ventana, text="Indique el nombre de la tabla a la que añadir los registros", style="light").grid(row=2, column=0, padx=5, pady=5, columnspan=2)
        tablas = tkb.Entry(ventana, width=30, style="light")
        tablas.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

        tkb.Label(ventana, text="Indique la lista de tuplas que contenga los regisstros", style="light").grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        registro = tkb.Entry(ventana, width=30, style="light")
        registro.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

        tkb.Button(ventana, text="Insertar", style="light", command= lambda: insertar()).grid(row=5, column=2, padx=5, pady=5)

        tkb.Button(ventana, text="Volver", style="light", command= lambda: ventana.destroy()).grid(row=6, column=2, padx=5, pady=5)

        def insertar():
            base = f"{bases.get()}.db"

            tabla = tablas.get()

            registros = registro.get()

            if base == ".db":
                messagebox.showerror("Error", "No ha indicado una base de datos")
                return

            elif not tabla:
                messagebox.showerror("Error", "No ha indicado una tabla")
                return
            
            elif not registros:
                messagebox.showerror("Error", "No ha indicado la lista que contenga registros")
                return
            
            else:
                try:
                    bd.BaseDatos.insertar_registros(base, tabla, registros)
                    messagebox.showinfo("Éxito", "Registros añadidos correctamente")

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", f"Ha sucedido el siguiente error: {e}")
    
    def ventana_insertar_1registro(self):
        ventana = tkb.Toplevel("Ventana para insertar 1 registro")
        ventana.geometry("800x500")

        tkb.Label(ventana, text="Indique el nombre de la base de datos", style="light").grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        bases = tkb.Entry(ventana, width=30, style="light")
        bases.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        tkb.Label(ventana, text="Indique el nombre de la tabla a la que añadir los registros", style="light").grid(row=2, column=0, padx=5, pady=5, columnspan=2)
        tablas = tkb.Entry(ventana, width=30, style="light")
        tablas.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

        tkb.Button(ventana, text="Empezar proceso", style="light", command= lambda: mostrar()).grid(row=2, column=2, padx=5, pady=5)

        tkb.Button(ventana, text="Volver", style="light", command= lambda: ventana.destroy()).grid(row=1, column=2, padx=5, pady=5)

        def mostrar():
            base = f"{bases.get()}.db"
            tabla = f"{tablas.get()}"
            if base == ".db" or not tabla:
                messagebox.showerror("Error", "No ha indicado una base de datos y/o una tabla")
                return

            try:
                columnas = bd.BaseDatos.mostrar_columnas(base, tabla)

                numero = len(columnas)

                if columnas == []:
                    tkb.Label(ventana, text="La tabla no contiene columnas, seleccione otra tabla", style="light").grid(row=4, column=0, padx=5, pady=5, columnspan=2)
                
                else:

                    entry_widgets = {}
                    label_names = []
                    contador = 5

                    for i in range(min(numero, len(columnas))):
                        label_names.append(f"{contador}")
                        label_names[i] = tkb.Label(ventana, style="light", text=f"Inique el contenido de la columna {columnas[i]}")
                        label_names[i].grid(row=contador, column=0, padx=5, pady=5)

                        entry_widgets[i] = tkb.Entry(ventana, style="light", width=30)
                        entry_widgets[i].grid(row=contador, column=1, padx=5, pady=5)

                        contador += 1

                    tkb.Button(ventana, text="Enviar", style="light", command=lambda: enviar(entry_widgets)).grid(row=contador+1, column=2, padx=5, pady=5)

                    def enviar(entry_widgets):
                        base = f"{bases.get()}.db"
                        tabla = f"{tablas.get()}"
                        
                        # Filter out empty values from Entry widgets
                        values = [entry.get() for entry in entry_widgets.values() if entry.get()]

                        # Print retrieved values for debugging
                        print("Retrieved values:", values)

                        # Verify the number of retrieved values
                        print("Number of values:", len(values))

                        # Construct the registro list
                        registro = tuple(values)

                        # Print the constructed registro for debugging
                        print("Constructed registro:", registro)

                        try: 
                            bd.BaseDatos.insertar_1registro(base, tabla, registro)
                            messagebox.showinfo("Éxito", "Inserto insertado correctamente")

                        except Exception as e:
                            print(e)
                            messagebox.showerror("Error", f"Ha sucedido el siguiente error: {e}")

            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"Ha sucedido el siguiente error: {e}")
 
    def ventana_eliminar_registros(self):
        ventana = tkb.Toplevel("Ventana para eliminar registros")
        ventana.geometry("550x300")

        tkb.Label(ventana, text="Indique la base por favor").grid(row=0, column=0, padx=5, pady=5)
        bases = tkb.Entry(ventana, style="light", width=30)
        bases.grid(row=0, column=1, padx=5, pady=5)

        tkb.Label(ventana, text="Indique la tabla por favor").grid(row=1, column=0, padx=5, pady=5)
        tablas = tkb.Entry(ventana, style="light", width=30)
        tablas.grid(row=1, column=1, padx=5, pady=5)

        tkb.Label(ventana, text="Indique el campo por favor").grid(row=2, column=0, padx=5, pady=5)
        campos = tkb.Entry(ventana, style="light", width=30)
        campos.grid(row=2, column=1, padx=5, pady=5)

        tkb.Label(ventana, text="Indique las condiciones por favor").grid(row=3, column=0, padx=5, pady=5)
        condiciones = tkb.Entry(ventana, style="light", width=30)
        condiciones.grid(row=3, column=1, padx=5, pady=5)

        tkb.Button(ventana, text="Elminar", style="light", command= lambda: eliminar()).grid(row=4, column=1, padx=5, pady=5)

        tkb.Button(ventana, text="Volver", style="light", command= lambda: ventana.destroy()).grid(row=5, column=1, padx=5, pady=5)

        def eliminar():
            base = f"{bases.get()}.db"
            tabla = tablas.get()
            condicion = condiciones.get()
            campo = campos.get()

            if base == ".db" or not tabla or not condicion or not campo:
                messagebox.showerror("Error", "No ha rellenado todos los campos")
                return

            else:
                try:
                    bd.BaseDatos.eliminar_registro_por_campo(base, tabla, campo, condicion)
                    messagebox.showinfo("Éxito", "Registro eliminado con éxito")

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", f"Ha sucedido el siguiente error: {e}")
    
    def ventana_vaciar_tablas(self):
        ventana = tkb.Toplevel("Ventana para actualizar registros")
        ventana.geometry("550x300")

        tkb.Label(ventana, text="Indique la base por favor").grid(row=0, column=0, padx=5, pady=5)
        bases = tkb.Entry(ventana, style="light", width=30)
        bases.grid(row=0, column=1, padx=5, pady=5)

        tkb.Label(ventana, text="Indique la tabla por favor").grid(row=1, column=0, padx=5, pady=5)
        tablas = tkb.Entry(ventana, style="light", width=30)
        tablas.grid(row=1, column=1, padx=5, pady=5)

        tkb.Button(ventana, text="Actualizar", style="light", command= lambda: actualizar()).grid(row=2, column=1, padx=5, pady=5)

        tkb.Button(ventana, text="Volver", style="light", command= lambda: ventana.destroy()).grid(row=3, column=1, padx=5, pady=5)

        def actualizar():
            base = f"{bases.get()}.db"
            tabla = tablas.get()

            if base == ".db" or not tabla :
                messagebox.showerror("Error", "No ha rellenado todos los campos")
                return

            else:
                try:
                    bd.BaseDatos.vaciar_tabls(base, tabla)
                    messagebox.showinfo("Éxito", "Registro actualizado con éxito")

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", f"Ha sucedido el siguiente error: {e}")
    
    def ventana_actualizar_registros(self):
        ventana = tkb.Toplevel("Ventana para actualizar registros")
        ventana.geometry("550x300")

        tkb.Label(ventana, text="Indique la base por favor").grid(row=0, column=0, padx=5, pady=5)
        bases = tkb.Entry(ventana, style="light", width=30)
        bases.grid(row=0, column=1, padx=5, pady=5)

        tkb.Label(ventana, text="Indique la tabla por favor").grid(row=1, column=0, padx=5, pady=5)
        tablas = tkb.Entry(ventana, style="light", width=30)
        tablas.grid(row=1, column=1, padx=5, pady=5)

        tkb.Label(ventana, text="Indique el campo por favor").grid(row=2, column=0, padx=5, pady=5)
        campos = tkb.Entry(ventana, style="light", width=30)
        campos.grid(row=2, column=1, padx=5, pady=5)

        tkb.Label(ventana, text="Indique los valores por favor").grid(row=3, column=0, padx=5, pady=5)
        condiciones = tkb.Entry(ventana, style="light", width=30)
        condiciones.grid(row=3, column=1, padx=5, pady=5)

        tkb.Button(ventana, text="Actualizar", style="light", command= lambda: actualizar()).grid(row=4, column=1, padx=5, pady=5)

        tkb.Button(ventana, text="Volver", style="light", command= lambda: ventana.destroy()).grid(row=5, column=1, padx=5, pady=5)

        def actualizar():
            base = f"{bases.get()}.db"
            tabla = tablas.get()
            condicion = condiciones.get()
            campo = campos.get()

            if base == ".db" or not tabla or not condicion or not campo:
                messagebox.showerror("Error", "No ha rellenado todos los campos")
                return

            else:
                try:
                    bd.BaseDatos.actualizar_registro(base, tabla, campo, condicion)
                    messagebox.showinfo("Éxito", "Registro actualizado con éxito")

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", f"Ha sucedido el siguiente error: {e}")

    def creacion(numero):
        ventana = tkb.Toplevel("Ventana creación de tablas")
        ventana.geometry("600x400")

        contador = 0
        entrada = 0
        entry_widgets = {}
        label_names = []

        cuenta = 2 * numero

        for i in range(cuenta):
            label_names.append(f"{contador}")
            label_names[i] = tkb.Label(ventana, style="light", text=f"Inique la sintaxis para la columna nº {i//2}")
            label_names[i].grid(row=contador//2, column=0, padx=5, pady=5)

            entry_widgets[i] = tkb.Entry(ventana, style="light", width=30)
            entry_widgets[i].grid(row=contador//2, column=1, padx=5, pady=5)

            entrada += 1
            contador += 1

        #print(label_names)
        #print(entry_widgets)

        tkb.Label(ventana, text="Indique el nombre de la tabla debajo", style="light").grid(row=contador, column=0, padx=5, pady=5)
        tkb.Label(ventana, text="Indique el nombre de la base debajo", style="light").grid(row=contador, column=1, padx=5, pady=5)

        tkb.Button(ventana, text="Crear tabla", style="light", width=8, command=lambda: crear(entry_widgets)).grid(row=contador+2, column=1, padx=5, pady=5)
        tkb.Button(ventana, text="Volver", style="light", width=8, command=lambda: ventana.destroy()).grid(row=contador+4, column=1, padx=5, pady=5)

        mas_info = tkb.Button(ventana, text="Más información", bootstyle="light-link", command=lambda: info())
        mas_info.grid(row=contador+3, column=1, padx=5, pady=5)

        nombre_tabla = tkb.Entry(ventana, style="light", width=30)
        nombre_tabla.grid(row=contador+1, column=0, padx=5, pady=5)

        nombre_base = tkb.Entry(ventana, style="light", width=30)
        nombre_base.grid(row=contador+1, column=1, padx=5, pady=5)

        def crear(entry_widgets):
            base = f"{nombre_base.get()}.db"
            nombre = nombre_tabla.get()
            
            # Filter out empty values from Entry widgets
            values = [entry.get() for entry in entry_widgets.values() if entry.get()]
            
            # Concatenate values with commas
            columnas = ",".join(values)
            
            # Wrap the result in parentheses
            columnas = f"({columnas})"

            if base == ".db" or not nombre:
                messagebox.showerror("Error", "Compruebe que ha indicado un nombre de base de datos y de tabla")
                return
            
            print(columnas)
            try :
                bd.BaseDatos.crear_tabla(base, nombre, columnas)
                messagebox.showinfo("Éxito", f"La tabla {nombre} se ha creado exitosamente en la base de dato {base}")

            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"Ha sucedido el siguiente error: {e}")
        
        def info():
            rot = tkb.Toplevel("Información sobre sintaxis sql")
            rot.geometry("500x400")
            tkb.Label(rot, text="La sintaxis de cada columna en sql tiene que ser el nombre de la columna seguido del tipo de dato y primary_key en caso de que sea clave primaria", style="light").grid(row=0, column=0, padx=5, pady=5, columnspan=5)
            texto = tkb.Text(rot, width=40, height=20)
            tkb.Button(rot, text="Volver", style="light", width=8, command=lambda: rot.destroy()).grid(row=2, column=1, padx=5, pady=5)
            texto.grid(row=1, column=0, padx=5, pady=5, columnspan=3)
            info = ["Tipos de datos en sql:", "Números int: integer", "Números float: real", "String: text", "Blob: blob", "Valores nulos: null", "Sqlite3 no acepta booleanos, pero con integer puedes hacer binario que es similar", "No acepta qutoincrement"]
            for i in info:
                registro = i
                texto.insert('end', registro)
                texto.insert('end', '\n')

            rot.mainloop()

        ventana.mainloop()


objeto_funciones = FuncionesPrograma()

class VentanaOpciones:
    # Lista de textos de los botones
    botones = {'Consulta SQL': objeto_funciones.ventana_consultas, 
               'Mostrar Bases de Datos': objeto_funciones.ventana_mostrar_bases_datos,
               'Eliminar Bases de Datos': objeto_funciones.ventana_eliminar_bases_datos,
               'Crear Bases de Datos': objeto_funciones.ventana_crear_bases_datos, 
               'Crear Respaldos': objeto_funciones.ventana_crear_respaldos,
               'Crear Tablas': objeto_funciones.ventana_crear_tablas,
               'Eliminar Tablas': objeto_funciones.ventana_eliminar_tablas,
               'Mostrar Tablas': objeto_funciones.ventana_mostrar_tablas,
               'Mostrar Columnas': objeto_funciones.ventana_mostrar_columnas,
               'Insertar Registros': objeto_funciones.ventana_insertar_registros,
               'Insertar 1 Registro': objeto_funciones.ventana_insertar_1registro,
               'Eliminar Registros': objeto_funciones.ventana_eliminar_registros,
               'Vaciar Tablas': objeto_funciones.ventana_vaciar_tablas,
               'Actualizar Registros': objeto_funciones.ventana_actualizar_registros    
               }
    
    def __init__(self):
        self.root = tkb.Window(themename="darkly", title="Opciones para trabajar con bases de datos.")

        #Contador para la posición de los botones
        contador = 0

        # Crea los botones y establece su texto
        for texto_boton in self.botones:
            button = tkb.Button(
                master=self.root,
                text=texto_boton,
                width=20,
                command=self.botones[texto_boton],
                style="light",            
            )
            button.grid(row=contador//3, column=contador%3, padx=5, pady=5)
        
            # Incrementa el contador
            contador += 1

        tkb.Button(self.root, text="Terminar programa", width=20, command= lambda: self.root.destroy(), style="light").grid(row=contador//3, column=contador%3, padx=5, pady=5)

        self.root.mainloop()