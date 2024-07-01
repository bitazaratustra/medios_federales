# Comando para instalar dependencias
install_dependencies:
	@echo "Instalando dependencias..."
	pip install -r requirements.txt

# Comando para iniciar el servidor de desarrollo
run:
	@echo "Iniciando el servidor de desarrollo..."
	uvicorn main:app --reload

# Comando para ejecutar pruebas
test:
	@echo "Ejecutando pruebas..."
	pytest

# Comando para limpiar archivos innecesarios
clean:
	@echo "Limpiando archivos..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +

# Comando para reinstalar dependencias (limpiar y luego instalar)
reinstall: clean install

.PHONY: install run test clean reinstall
