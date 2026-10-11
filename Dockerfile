# 1. Capa Base: Distribucion ligera de Linux con entorno de ejecucion
FROM python:3.11-alpine

# 2. Variables de entorno del sistema operativo dentro del contenedor
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# 3. Directorio de trabajo en el sistema de archivos del contenedor
WORKDIR /app

# 4. Aprovechamiento del Layer Caching: Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia del codigo fuente hacia el sistema de archivos de la capa superior
COPY app.py .

# 6. Metadata de documentacion: Puerto que el proceso escuchara
EXPOSE 5000

# 7. Punto de entrada (PID 1): Ejecucion del servidor
CMD ["python", "app.py"]
