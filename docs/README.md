# Documentacion del Proyecto

## Resumen

Este proyecto implementa una aplicacion de linea de comandos en Python para sumar dos numeros. La estructura esta organizada para facilitar mantenimiento, pruebas, documentacion y versionado.

## Flujo Profesional

```text
Idea -> ChatGPT
Codigo -> Codex
Edicion -> VS Code
Control -> GitHub
Docs -> Markdown
```

## Carpetas Principales

### `src/`

Contiene el codigo fuente principal.

- `main.py`: punto de entrada simple para ejecutar la app.
- `sum_two_numbers/cli.py`: logica principal de la interfaz por linea de comandos.

### `docs/`

Contiene la documentacion del proyecto.

- `README.md`: guia general.
- `usage.md`: guia de ejecucion rapida.

### `tests/`

Contiene pruebas automatizadas para validar la aplicacion.

## Comandos Utiles

Inicializar entorno:

```bash
pip install -e .
```

Ejecutar la aplicacion:

```bash
python src/main.py 3 4
```

Ejecutar pruebas:

```bash
python -m unittest discover -s tests -v
```

## Git y GitHub

Comandos basicos:

```bash
git add .
git commit -m "actualiza proyecto"
git push
```

## Extensiones Futuras

- Agregar mas operaciones matematicas.
- Incorporar `argparse` avanzado con subcomandos.
- Agregar cobertura de pruebas y CI.
