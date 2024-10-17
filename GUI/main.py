
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Conexion.conexion import Database
from PIL import Image, ImageTk

def ventana_login():
    ventana_login = Tk()
    ventana_login.title("Inicio de Sesión")
    ventana_login.geometry("600x500")

    imagen_fondo = Image.open("codigo.ico")
    imagen_fondo = imagen_fondo.resize((600,500), Image.LANCZOS)  # Cambié ANTIALIAS por LANCZOS
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    fondo_label = Label(ventana_login, image=imagen_fondo_tk)  # Cambié 'ventana' por 'ventana_login'
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    marco_login = LabelFrame(ventana_login, text="Iniciar Sesión", fg="purple", padx=20, pady=20)
    marco_login.pack(padx=50, pady=50)

    usuario = StringVar()
    contrasena = StringVar()

    # Etiquetas y entradas para usuario y contraseña
    Label(marco_login, text="Usuario:").grid(row=0, column=0, padx=10, pady=10, sticky=E)
    txtusuario = Entry(marco_login, textvariable=usuario)
    txtusuario.grid(row=0, column=1, padx=10, pady=10)

    Label(marco_login, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10, sticky=E)
    txtcontrasena = Entry(marco_login, textvariable=contrasena, show="*")
    txtcontrasena.grid(row=1, column=1, padx=10, pady=10)

    import mysql.connector  # Asegúrate de tener este paquete instalado

    # Conectar a la base de datos
    def conectar_db():
        return mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia esto por tu usuario de MySQ
            database="proyecto_estaciones"
        )

    def verificar_login():
        user = usuario.get()  # Obtener el nombre de usuario
        password = contrasena.get()  # Obtener la contraseña

        # Conectar a la base de datos
        db = conectar_db()
        cursor = db.cursor()

        # Preparar la consulta SQL
        sql = "SELECT * FROM usuario WHERE usuario = %s AND contrasena = %s"
        cursor.execute(sql, (user, password))
        resultado = cursor.fetchone()  # Obtener un único registro

        # Verificar si el usuario existe
        if resultado:
            ventana_login.destroy()
            main_window()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

        # Cerrar la conexión
        cursor.close()
        db.close()

    # Botón de inicio de sesión
    btn_login = Button(marco_login, text="Iniciar Sesión", command=verificar_login, bg="purple", fg="white")
    btn_login.grid(row=2, columnspan=2, padx=10, pady=10)

    def ventana_registro():
        ventana_reg = Toplevel()
        ventana_reg.title("Registro")
        ventana_reg.geometry("600x500")  # Aumenté el tamaño para acomodar todos los campos
        imagen_fondo = Image.open("carro.ico")
        imagen_fondo = imagen_fondo.resize((600,600), Image.LANCZOS)
        imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
        fondo_label = Label(ventana_reg, image=imagen_fondo_tk)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)


        marco_registro = LabelFrame(ventana_reg, text="Registrar Usuario", fg="purple", padx=20, pady=20)
        marco_registro.pack(padx=50, pady=50)

        nuevo_usuario = StringVar()
        nueva_contrasena = StringVar()
        nuevo_nombre = StringVar()
        nuevo_apellido = StringVar()
        nuevo_edad = StringVar()
        nueva_fecha_nacimiento = StringVar()
        nuevo_horoscopo = StringVar()

        # Etiquetas y entradas para nuevo usuario y contraseña
        Label(marco_registro, text="Usuario:").grid(row=0, column=0, padx=10, pady=5, sticky=E)
        txtnuevo_usuario = Entry(marco_registro, textvariable=nuevo_usuario)
        txtnuevo_usuario.grid(row=0, column=1, padx=10, pady=5)

        Label(marco_registro, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5, sticky=E)
        txtnuevo_contrasena = Entry(marco_registro, textvariable=nueva_contrasena, show="*")
        txtnuevo_contrasena.grid(row=1, column=1, padx=10, pady=5)

        Label(marco_registro, text="Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky=E)
        txtnuevo_nombre = Entry(marco_registro, textvariable=nuevo_nombre)
        txtnuevo_nombre.grid(row=2, column=1, padx=10, pady=5)

        Label(marco_registro, text="Apellido:").grid(row=3, column=0, padx=10, pady=5, sticky=E)
        txtnuevo_apellido = Entry(marco_registro, textvariable=nuevo_apellido)
        txtnuevo_apellido.grid(row=3, column=1, padx=10, pady=5)

        Label(marco_registro, text="Edad:").grid(row=4, column=0, padx=10, pady=5, sticky=E)
        txtnuevo_edad = Entry(marco_registro, textvariable=nuevo_edad)
        txtnuevo_edad.grid(row=4, column=1, padx=10, pady=5)

        Label(marco_registro, text="Fecha Nacimiento:").grid(row=5, column=0, padx=10, pady=5, sticky=E)
        txtnuevo_fecha_nacimiento = Entry(marco_registro, textvariable=nueva_fecha_nacimiento)
        txtnuevo_fecha_nacimiento.grid(row=5, column=1, padx=10, pady=5)

        Label(marco_registro, text="Tipo Horóscopo:").grid(row=6, column=0, padx=10, pady=5, sticky=E)
        txtnuevo_horoscopo = Entry(marco_registro, textvariable=nuevo_horoscopo)
        txtnuevo_horoscopo.grid(row=6, column=1, padx=10, pady=5)

        def registrar_usuario():
            user = nuevo_usuario.get()
            password = nueva_contrasena.get()

            # Aquí puedes integrar la lógica para insertar el nuevo usuario en la base de datos.
            # Ejemplo de validación simulada:
            if user and password:
                # Simula registro en la base de datos
                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
                ventana_reg.destroy()
            else:
                messagebox.showerror("Error", "Todos los campos son requeridos")

        # Botón para registrar el nuevo usuario
        btn_registrar = Button(marco_registro, text="Registrar", command=registrar_usuario, bg="purple", fg="white")
        btn_registrar.grid(row=7, columnspan=2, padx=10, pady=10)

        ventana_reg.mainloop()

    # Botón de registro
    btn_registro = Button(marco_login, text="Registrar", command=ventana_registro, bg="black", fg="white")
    btn_registro.grid(row=3, columnspan=2, padx=10, pady=10)


    ventana_login.mainloop()


def main_window():
    ventana = Tk()
    ventana.title("Energy World")
    ventana.iconbitmap("verde.ico")
    ventana.geometry("800x600")  # Ajusté el tamaño para acomodar mejor los elementos
    imagen_fondo = Image.open("carro.ico")
    imagen_fondo = imagen_fondo.resize((600, 600), Image.LANCZOS)
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
    fondo_label = Label(main_window, image=imagen_fondo_tk)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Aquí va el código de la ventana principal que ya tienes implementado
    # ...


if __name__ == "__main__":
    ventana_login()  # Inicia con la ventana de inicio de sesión



def main():
    ventana = Tk()
    ventana.title("Energy World")
    ventana.iconbitmap("verde.ico")
    ventana.geometry("800x600")  # Ajusté el tamaño para acomodar mejor los elementos

    imagen_fondo = Image.open("carro.ico")
    imagen_fondo = imagen_fondo.resize((500, 400), Image.LANCZOS)
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
    fondo_label = Label(main, image=imagen_fondo_tk)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    marco = LabelFrame(ventana, text="Estaciones Energy World", fg="purple")
    marco.place(x=50, y=50, width=700, height=500)

    db = Database()
    Estaciones = StringVar()
    ubicacion = StringVar()
    precio = StringVar()
    ciudad = StringVar()
    id_estacion = StringVar()  # Para almacenar el ID seleccionado


    # Etiquetas y entradas
    Label(marco, text="Estaciones:").grid(column=0, row=0, padx=10, pady=5, sticky=E)
    txtestaciones = Entry(marco, textvariable=Estaciones)
    txtestaciones.grid(column=1, row=0, padx=10, pady=5, sticky=W)

    Label(marco, text="Ubicación:").grid(column=0, row=1, padx=10, pady=5, sticky=E)
    txtubicacion = Entry(marco, textvariable=ubicacion)
    txtubicacion.grid(column=1, row=1, padx=10, pady=5, sticky=W)

    Label(marco, text="Precio:").grid(column=0, row=2, padx=10, pady=5, sticky=E)
    txtprecio = Entry(marco, textvariable=precio)
    txtprecio.grid(column=1, row=2, padx=10, pady=5, sticky=W)

    Label(marco, text="Ciudad:").grid(column=0, row=3, padx=10, pady=5, sticky=E)
    txtciudad = Entry(marco, textvariable=ciudad)
    txtciudad.grid(column=1, row=3, padx=10, pady=5, sticky=W)

    # Mensaje
    lblMensaje = Label(marco, text="Nombre De las Unidades Disponibles", fg="purple")
    lblMensaje.grid(column=0, row=4, columnspan=4, padx=10, pady=5)

    # Treeview con Scrollbar
    tree_frame = Frame(marco)
    tree_frame.grid(column=0, row=5, columnspan=4, padx=10, pady=5)

    scrollbar = Scrollbar(tree_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    tvEstaciones = ttk.Treeview(tree_frame, yscrollcommand=scrollbar.set, selectmode="browse")
    tvEstaciones.pack()

    scrollbar.config(command=tvEstaciones.yview)

    tvEstaciones["columns"] = ("id", "Estaciones", "Ubicacion", "Precio", "Ciudad")
    tvEstaciones.column("#0", width=0, stretch=NO)
    tvEstaciones.column("id", width=50, anchor=CENTER)
    tvEstaciones.column("Estaciones", width=150, anchor=CENTER)
    tvEstaciones.column("Ubicacion", width=150, anchor=CENTER)
    tvEstaciones.column("Precio", width=100, anchor=CENTER)
    tvEstaciones.column("Ciudad", width=100, anchor=CENTER)

    tvEstaciones.heading("#0", text="")
    tvEstaciones.heading("id", text="ID", anchor=CENTER)
    tvEstaciones.heading("Estaciones", text="Estaciones", anchor=CENTER)
    tvEstaciones.heading("Ubicacion", text="Ubicación", anchor=CENTER)
    tvEstaciones.heading("Precio", text="Precio", anchor=CENTER)
    tvEstaciones.heading("Ciudad", text="Ciudad", anchor=CENTER)

    # Funciones de botones
    def vaciar_tabla():
        for fila in tvEstaciones.get_children():
            tvEstaciones.delete(fila)

    def llenar_tabla():
        vaciar_tabla()
        try:
            sql = "SELECT * FROM energy_world"
            db.cursor.execute(sql)
            filas = db.cursor.fetchall()
            for fila in filas:
                id = fila[0]
                tvEstaciones.insert("", END, iid=id, text=id, values=(id, fila[1], fila[2], fila[3], fila[4]))
        except Exception as e:
            lblMensaje.config(text=f"Error al cargar datos: {e}")

    def eliminar():
        selected = tvEstaciones.selection()
        if selected:
            id = selected[0]
            try:
                sql = "DELETE FROM energy_world WHERE id = %s"
                db.cursor.execute(sql, (id,))
                db.connection.commit()
                tvEstaciones.delete(id)
                lblMensaje.config(text="Registro eliminado correctamente")
                limpiar_campos()
            except Exception as e:
                lblMensaje.config(text=f"Error al eliminar: {e}")
        else:
            lblMensaje.config(text="Seleccione un registro para eliminar")

    def nuevo():
        est = Estaciones.get().strip()
        ubi = ubicacion.get().strip()
        pre = precio.get().strip()
        ciu = ciudad.get().strip()

        if est and ubi and pre and ciu:
            try:
                sql = "INSERT INTO energy_world (Estaciones, Ubicacion, Precio, Ciudad) VALUES (%s, %s, %s, %s)"
                db.cursor.execute(sql, (est, ubi, pre, ciu))
                db.connection.commit()
                lblMensaje.config(text="Registro añadido correctamente")
                llenar_tabla()
                limpiar_campos()
            except Exception as e:
                lblMensaje.config(text=f"Error al añadir: {e}")
        else:
            lblMensaje.config(text="Todos los campos son requeridos")

    def modificar():
        selected = tvEstaciones.selection()
        if selected:
            id = selected[0]
            est = Estaciones.get().strip()
            ubi = ubicacion.get().strip()
            pre = precio.get().strip()
            ciu = ciudad.get().strip()

            if est and ubi and pre and ciu:
                try:
                    sql = "UPDATE energy_world SET Estaciones=%s, Ubicacion=%s, Precio=%s, Ciudad=%s WHERE id=%s"
                    db.cursor.execute(sql, (est, ubi, pre, ciu, id))
                    db.connection.commit()
                    lblMensaje.config(text="Registro modificado correctamente")
                    llenar_tabla()
                    limpiar_campos()
                except Exception as e:
                    lblMensaje.config(text=f"Error al modificar: {e}")
            else:
                lblMensaje.config(text="Todos los campos son requeridos para modificar")
        else:
            lblMensaje.config(text="Seleccione un registro para modificar")

    def seleccionar_fila(event):
        selected = tvEstaciones.selection()
        if selected:
            item = tvEstaciones.item(selected)
            values = item['values']
            id_estacion.set(values[0])
            Estaciones.set(values[1])
            ubicacion.set(values[2])
            precio.set(values[3])
            ciudad.set(values[4])

    def limpiar_campos():
        Estaciones.set("")
        ubicacion.set("")
        precio.set("")
        ciudad.set("")
        id_estacion.set("")
        tvEstaciones.selection_remove(tvEstaciones.selection())

    # Botones con posicionamiento corregido
    btnEliminar = Button(marco, text="Eliminar", command=eliminar, width=15, bg="black", fg="white")
    btnEliminar.grid(column=0, row=6, padx=10, pady=10)

    btnNuevo = Button(marco, text="Nuevo", command=nuevo, width=15, bg="purple", fg="white")
    btnNuevo.grid(column=1, row=6, padx=10, pady=10)

    btnModificar = Button(marco, text="Modificar", command=modificar, width=15, bg="purple", fg="white")
    btnModificar.grid(column=2, row=6, padx=10, pady=10)

    btnLimpiar = Button(marco, text="Limpiar", command=limpiar_campos, width=15, bg="black", fg="white")
    btnLimpiar.grid(column=3, row=6, padx=10, pady=10)

    # Evento de selección en el Treeview
    tvEstaciones.bind("<<TreeviewSelect>>", seleccionar_fila)

    # Inicializar la tabla con datos
    llenar_tabla()

    ventana.mainloop()

if __name__ == "__main__":
    main()

