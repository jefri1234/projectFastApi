

--crear el entorno virtual 
python -m venv venv
 
--activar el entorno virtual
venv/Scripts/activate

-- instalar dependencias que necesito
pip install fastapi

--GENERAR EL archivo requirements para listado de dependencias
pip freeze > requirements.txt


--instalar las dependencias
pip install -r requirements.txt

-- Esto te dirá la ubicación del ejecutable que estás usando.
where uvicorn

-- comando para correr el servidor en modo desarrollo
uvicorn main:app --reload


-- Ruta del proyecto en ejecucion
http://127.0.0.1:8000


-- command for deactivate virtual enviroment
deactivate
