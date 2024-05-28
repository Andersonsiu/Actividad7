# Usar la imagen oficial de Python como base
FROM python:3.9-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el script de Python en el contenedor
COPY escalado.py .

# Ejecutar el script de Python
CMD ["python", "escalado.py"]

