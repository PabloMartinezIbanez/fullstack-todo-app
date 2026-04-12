# fullstack-todo-app

Repositorio de prueba para TFG orientado a evaluar agentes de IA en CI sobre un proyecto fullstack mediano con backend ligero, frontend basico y suite poliglota de tests.

## Objetivo

- Simular un escenario realista con varias capas de codigo.
- Incluir problemas intencionales para SonarQube.
- Incluir un par de tests con fallo para forzar diagnostico y reparacion.
- Medir el tiempo que tarda la IA en proponer arreglos completos.

## Stack

- Backend: Python + Flask
- Frontend: HTML, CSS, JavaScript vanilla
- Modulo adicional: Java
- CI: Jenkins + SonarQube + shared library FixWithAI

## Estructura

- Jenkinsfile
- ai-tests-config.json
- INTENTIONAL_SONAR_ISSUES.md
- requirements/python_requirements.txt
- scripts/run_java_tests.sh
- src/backend/
- src/frontend/
- src/java/com/example/task/
- tests/python/
- tests/javascript/
- tests/java/com/example/task/

## Endpoints del backend

- GET /health
- GET /tasks
- GET /tasks?priority=high
- GET /tasks/<id>
- GET /tasks/stats
- POST /tasks

Ejemplo de body para POST /tasks:

```json
{
  "title": "Prepare weekly report",
  "description": "Gather metrics and publish dashboard",
  "priority": "high",
  "due_date": "2026-05-15"
}
```

## Ejecucion local

### 1) Instalar dependencias Python

```bash
python -m pip install -r requirements/python_requirements.txt
```

### 2) Ejecutar backend

```bash
PYTHONPATH=src/backend python -m flask --app src/backend/app run --port 5000
```

### 3) Ejecutar frontend

Opcion simple: servir carpeta frontend con un servidor estatico.

```bash
cd src/frontend
python -m http.server 8000
```

Abrir http://localhost:8000 y el frontend consumira la API en http://localhost:5000.

## Ejecutar tests

### Python

```bash
PYTHONPATH=src/backend python -m pytest tests/python/ -v
```

### JavaScript

```bash
node --test tests/javascript/test_app.js
```

### Java

```bash
bash scripts/run_java_tests.sh
```

## Estado esperado de tests

- Python: hay 1 test fallando de forma intencional.
- JavaScript: hay 1 test fallando de forma intencional.
- Java: tests verdes.

## Integracion con FixWithAI

Este repo sigue el mismo contrato que los repositorios previos:

- testConfigFile: ai-tests-config.json
- repoSlug: PabloMartinezIbanez/fullstack-todo-app
- rama de correccion automatica: ai-fix/*

El detalle de los issues intencionales se documenta en INTENTIONAL_SONAR_ISSUES.md.
