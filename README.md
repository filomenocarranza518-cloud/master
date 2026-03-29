# Mi Proyecto

Proyecto Python con una estructura profesional para desarrollo, pruebas, documentación y control de versiones.

## Arquitectura General

```text
ChatGPT -> piensa / diseña
Codex -> crea codigo
VS Code -> editas y ejecutas
GitHub -> guarda versiones
Markdown -> documenta
```

## Estructura del Proyecto

```text
mi-proyecto/
|-- src/
|   |-- main.py
|   `-- sum_two_numbers/
|       |-- __init__.py
|       |-- __main__.py
|       `-- cli.py
|-- docs/
|   |-- README.md
|   `-- usage.md
|-- tests/
|   `-- test_sum_two_numbers.py
|-- .gitignore
|-- pyproject.toml
|-- README.md
|-- requirements.txt
`-- sum_two_numbers.py
```

## Descripcion

Este proyecto suma dos numeros usando Python desde la linea de comandos. Tambien deja una base ordenada para seguir creciendo con nuevas funciones, pruebas y documentacion.

## Uso

Ejecuta la aplicacion principal:

```bash
python src/main.py 3 4
```

Tambien puedes usar el wrapper del proyecto:

```bash
python sum_two_numbers.py 3 4
```

Si instalas el proyecto en modo editable:

```bash
pip install -e .
sum-two-numbers 3 4
```

## Pruebas

```bash
python -m unittest discover -s tests -v
```

## Tecnologias

- Python
- Codex
- VS Code
- GitHub
- Markdown

## Flujo de Trabajo con IA

### ChatGPT

Se usa para pensar la idea, definir requisitos y planear la solucion.

Ejemplo:

```text
disena una app de calculadora avanzada
```

### Codex

Se usa para implementar el codigo y automatizar cambios.

Ejemplo:

```text
implement the calculator in python inside src/main.py
```

### VS Code

Se usa para editar, ejecutar y revisar el proyecto localmente.

### GitHub

Se usa para guardar versiones del proyecto.

```bash
git add .
git commit -m "add calculator"
git push
```

### Markdown

Se usa para documentar el proyecto y su uso.

## Documentacion

La guia detallada esta en [docs/README.md](docs/README.md) y el uso rapido en [docs/usage.md](docs/usage.md).
