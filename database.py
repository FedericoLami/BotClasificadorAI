import sqlite3

def crearTabla():
    conn = sqlite3.connect("clasificaciones.db")
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE consultasUsuario (
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


crearTabla()
    