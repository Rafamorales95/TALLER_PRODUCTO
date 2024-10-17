from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Conexion.conexion import Database
from PIL import Image, ImageTk
import mysql.connector


def ventana_login():
    ventana_login = Tk()
    ventana_login.title("Inicio de Sesión")
    ventana_login.geometry("600x500")

    imagen_fondo = Image.open("codigo.ico")
    imagen_fondo = imagen_fondo.resize((600, 500), Image.LANCZOS)
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    fondo_label = Label(ventana_login, image=imagen_fondo_tk)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    marco_login = LabelFrame(ventana_login, text="Iniciar Sesión", fg="purple", padx=20, pady=20)
    marco_login.pack(padx=50, pady=50)

    usuario = StringVar()
    contrasena = StringVar()

    Label(marco_login, text="Usuario:").grid(row=0, column=0, padx=10, pady=10, sticky=E)
    txtusuario = Entry(marco_login, textvariable=usuario)
    txtusuario.grid(row=0, column=1, padx=10, pady=10)

    Label(marco_login, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10, sticky=E)
    txtcontrasena = Entry(marco_login, textvariable=contrasena, show="*")
    txtcontrasena.grid(row=1, column=1, padx=10, pady=10)

    def conectar_db():
        return mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia esto por tu usuario de MySQL
            database="proyecto_estaciones"
        )

    def verificar_login():
        user = usuario.get()
        password = contrasena.get()

        db = conectar_db()
        cursor = db.cursor()

        sql = "SELECT * FROM usuario WHERE usuario = %s AND contrasena = %s"
        cursor.execute(sql, (user, password))
        resultado = cursor.fetchone()

        if resultado:
            ventana_login.destroy()
            main_window()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

        cursor.close()
        db.close()

    btn_login = Button(marco_login, text="Iniciar Sesión", command=verificar_login, bg="purple", fg="white")
    btn_login.grid(row=2, columnspan=2, padx=10, pady=10)

    def ventana_registro():
        ventana_reg = Toplevel(ventana_login)
        ventana_reg.title("Registro")
        ventana_reg.geometry("600x500")

        imagen_fondo = Image.open("carro.ico")
        imagen_fondo = imagen_fondo.resize((600, 600), Image.LANCZOS)
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

        # Registro de usuario y contraseña
        Label(marco_registro, text="Usuario:").grid(row=0, column=0, padx=10, pady=5, sticky=E)
        Entry(marco_registro, textvariable=nuevo_usuario).grid(row=0, column=1, padx=10, pady=5)

        Label(marco_registro, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5, sticky=E)
        Entry(marco_registro, textvariable=nueva_contrasena, show="*").grid(row=1, column=1, padx=10, pady=5)

        # Otros campos
        Label(marco_registro, text="Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky=E)
        Entry(marco_registro, textvariable=nuevo_nombre).grid(row=2, column=1, padx=10, pady=5)

        Label(marco_registro, text="Apellido:").grid(row=3, column=0, padx=10, pady=5, sticky=E)
        Entry(marco_registro, textvariable=nuevo_apellido).grid(row=3, column=1, padx=10, pady=5)

        Label(marco_registro, text="Edad:").grid(row=4, column=0, padx=10, pady=5, sticky=E)
        Entry(marco_registro, textvariable=nuevo_edad).grid(row=4, column=1, padx=10, pady=5)

        Label(marco_registro, text="Fecha Nacimiento:").grid(row=5, column=0, padx=10, pady=5, sticky=E)
        Entry(marco_registro, textvariable=nueva_fecha_nacimiento).grid(row=5, column=1, padx=10, pady=5)

        Label(marco_registro, text="Tipo Horóscopo:").grid(row=6, column=0, padx=10, pady=5, sticky=E)
        Entry(marco_registro, textvariable=nuevo_horoscopo).grid(row=6, column=1, padx=10, pady=5)

        def registrar_usuario():
            user = nuevo_usuario.get()
            password = nueva_contrasena.get()
            if user and password:
                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
                ventana_reg.destroy()
            else:
                messagebox.showerror("Error", "Todos los campos son requeridos")

        btn_registrar = Button(marco_registro, text="Registrar", command=registrar_usuario, bg="purple", fg="white")
        btn_registrar.grid(row=7, columnspan=2, padx=10, pady=10)

        ventana_reg.mainloop()

    btn_registro = Button(marco_login, text="Registrar", command=ventana_registro, bg="black", fg="white")
    btn_registro.grid(row=3, columnspan=2, padx=10, pady=10)

    ventana_login.mainloop()


def main_window():
    ventana_principal = Tk()
    ventana_principal.title("Energy World")
    ventana_principal.iconbitmap("verde.ico")
    ventana_principal.geometry("800x600")

    imagen_fondo = Image.open("carro.ico")
    imagen_fondo = imagen_fondo.resize((800, 600), Image.LANCZOS)
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)
    fondo_label = Label(ventana_principal, image=imagen_fondo_tk)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    marco = LabelFrame(ventana_principal, text="Estaciones Energy World", fg="purple")
    marco.place(x=50, y=50, width=700, height=500)

    # Resto del código de la ventana principal...

    ventana_principal.mainloop()


if __name__ == "__main__":
    ventana_login()
