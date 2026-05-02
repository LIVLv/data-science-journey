# Día 1 — Configuración del Entorno

## Lo que hice hoy
- Instalé Anaconda (Python 3.13.9)
- Instalé Git (2.54.0)
- Configuré identidad global de Git
- Generé par de llaves SSH y conecté con GitHub
- Cloné el repositorio y ejecuté mi primer ciclo git

## Conceptos clave aprendidos
- PATH: lista de direcciones donde Windows busca programas
- SSH: autenticación por par de llaves sin contraseña
- Repositorio: carpeta de proyecto bajo control de Git
- Commit: registro firmado de un estado del código
- Entorno virtual: burbuja aislada de dependencias por proyecto

## Flujo de trabajo dirio
''bash
conda activate dataci
cd Documents/data-cience-journey
git pull origin main
# ... trabajar ...
git add .
git commint -m "feat: descripcion"
git push origin main

Luego hacé el commit:

'''bash
git add .
git commit -m "docs: flujo de trabajo diario agragado al README"
git push origin main
'''

