import sqlite3

def crearTabla():
    conn = sqlite3.connect("clasificaciones.db")
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS consultasUsuario (
                        idConsulta INTEGER PRIMARY KEY,
                        mensaje TEXT,
                        categoria TEXT,
                        idioma TEXT,
                        sentimiento TEXT,
                        resumen TEXT,
                        fecha DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                    """)
    conn.commit()
    conn.close()

def guardarClasificacion(mensaje,categoria,idioma,sentimiento,resumen):
    conn = sqlite3.connect("clasificaciones.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO consultasUsuario (mensaje,categoria,idioma,sentimiento,resumen) VALUES (?,?,?,?,?)", 
                  (mensaje, categoria, idioma, sentimiento, resumen), 
                  )
    conn.commit()
    conn.close()

def retornarConsultas():
    conn = sqlite3.connect("clasificaciones.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM consultasUsuario")
    datos = cursor.fetchall()
    conn.close()
    return datos

crearTabla()
    