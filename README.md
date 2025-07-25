# MyPokeAPI

API con FastAPI, SQLAlchemy y Pydantic para gestionar datos Pokémon.

---

## Requisitos previos

- Python 3.8 o superior instalado.
- PowerShell (Windows) o terminal compatible.
- Node.js no es necesario para este proyecto.

---

## Instalación y configuración (Windows - PowerShell)



### 1. Clonar el repositorio
  
```bash
git clone <url-del-repositorio>
```

### 2. Abrir PowerShell en la carpeta del proyecto clonado.


### 3. Crear y activar el entorno virtual:
```powershell
python -m venv venv
venv\Scripts\activate.bat
```

Si da error de ejecución de scripts:  
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Luego volver a activar el entorno:  
```powershell
venv\Scripts\activate.bat
```

### 4. Instalar dependencias: 
```powershell
pip install -r requirements.txt
```

### 5. Ejecutar el servidor: 
```powershell
uvicorn app.main:app --reload
```

### 6.  Visitar en el navegador:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

