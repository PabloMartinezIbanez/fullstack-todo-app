# SonarQube Issues Intencionales

Este repositorio incluye code smells y fallos de test intencionales para medir el comportamiento de la etapa FixWithAI sobre un proyecto fullstack mediano.

## Python

- src/backend/task_service.py
  - Variable local no usada en create_task.
  - Retorno booleano redundante en is_overdue.
  - Ramas redundantes en _priority_weight.
- src/backend/task_utils.py
  - Retorno booleano redundante en validate_priority.
  - Logica duplicada en truncate_description.

## JavaScript

- src/frontend/app.js
  - Retorno booleano redundante y else innecesario tras return en isUrgentTask.
  - Logica duplicada en taskStatusBadge.
  - Uso de == en lugar de === en formatDate.

## Java

- src/java/com/example/task/TaskPriorityEngine.java
  - Variable local no usada en computePriorityScore.
  - Retorno booleano redundante en needsEscalation.
  - Logica duplicada en assignQueue.

## Tests con fallo intencional

- tests/python/test_task_service.py
  - test_is_overdue_with_past_date espera False cuando el resultado real deberia ser True.
- tests/javascript/test_app.js
  - formatDate formats date for UI cards espera un formato distinto al implementado.

## Uso esperado en experimentos

- Abrir un PR normal para que Jenkins ejecute Scan, Quality Gate y Fix Issues with AI.
- Revisar en SonarQube que los hallazgos aparezcan sobre la rama analizada.
- Verificar que la rama ai-fix/* creada por IA intenta corregir code smells y ajustar tests.
- Comparar tiempo de remediacion y numero de iteraciones necesarias.
