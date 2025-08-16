import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env si existe
load_dotenv()

# Configuración de OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Validar que la API key esté configurada
if not OPENAI_API_KEY:
    raise ValueError("No se encontró OPENAI_API_KEY. Por favor configúrala en el archivo .env")

# Configuración del modelo
MODEL = "gpt-4o"  # Asegúrate de usar un modelo válido
