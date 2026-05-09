# Clasificador de Mensajes con IA

Sistema de clasificación automática de mensajes usando inteligencia artificial. Recibe texto en lenguaje natural, lo analiza con Claude (Anthropic) y devuelve una clasificación estructurada en JSON que incluye categoría, idioma, sentimiento y resumen. Los resultados se persisten en una base de datos y se exponen a través de una API REST con interfaz web.

Pensado para automatizar el procesamiento inicial de mensajes de clientes en entornos empresariales: soporte técnico, e-commerce, atención al cliente, y cualquier sistema que necesite enrutar mensajes de forma automática sin intervención humana.

---

## Demo

![Demo del clasificador](demo.gif)

---

## Tecnologías utilizadas

| Capa | Tecnología |
|------|-----------|
| Modelo de lenguaje | Claude Haiku (Anthropic API) |
| Backend / API REST | FastAPI + Uvicorn |
| Base de datos | SQLite |
| Frontend | HTML · CSS · JavaScript vanilla |
| Configuración | python-dotenv |
| Entorno | Python 3.x + venv |

---

## Arquitectura del proyecto

```
bot_clasificador/
├── clasificador.py     # Lógica de clasificación con Claude
├── database.py         # Conexión y operaciones con SQLite
├── main.py             # API REST con FastAPI (endpoints)
├── index.html          # Interfaz web
├── .env                # Variables de entorno (no se sube a GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

Cada archivo tiene una única responsabilidad:

- `clasificador.py` se comunica con la API de Anthropic y devuelve un diccionario con los resultados.
- `database.py` maneja toda la persistencia: creación de tabla, inserción y consulta de registros.
- `main.py` expone dos endpoints REST y coordina las capas anteriores.

---

## Endpoints de la API

### `POST /clasificar`

Recibe un mensaje en texto libre y devuelve su clasificación.

**Request:**
```json
{
  "mensaje": "Mi pedido llegó roto y nadie me responde"
}
```

**Response:**
```json
{
  "categoria": "queja",
  "idioma": "español",
  "sentimiento": "negativo",
  "resumen": "Cliente reporta producto dañado sin respuesta del equipo de soporte"
}
```

Categorías posibles: `consulta` · `queja` · `urgente` · `spam`

### `GET /clasificaciones`

Devuelve todos los registros almacenados en la base de datos.

---

## Instalación y uso

### Requisitos previos

- Python 3.10 o superior
- API Key de Anthropic ([console.anthropic.com](https://console.anthropic.com))

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/bot-clasificador.git
cd bot-clasificador

# 2. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
# Crear archivo .env en la raíz del proyecto:
ANTHROPIC_API_KEY=tu-api-key-aquí

# 5. Iniciar el servidor
uvicorn main:app --reload
```

### Interfaz web

Con el servidor corriendo, abrí `index.html` directamente en el navegador.

### Documentación interactiva de la API

```
http://127.0.0.1:8000/docs
```

FastAPI genera automáticamente una interfaz para probar todos los endpoints.

---

## Casos de uso empresariales

- **Soporte técnico:** clasificar tickets entrantes y enrutarlos al equipo correcto según categoría y urgencia.
- **E-commerce:** detectar quejas de clientes en tiempo real para priorizar atención.
- **Análisis de feedback:** procesar respuestas de encuestas o reseñas y extraer sentimiento de forma automática.
- **Moderación:** identificar spam o mensajes fuera de contexto antes de que lleguen a un agente humano.

---

## Autor

**Federico Lami**
[LinkedIn](https://www.linkedin.com/in/federicolami/)