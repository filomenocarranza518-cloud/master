# Sum Two Numbers

`sum-two-numbers` is a small Python command-line application that adds two numbers and prints the result.

## Project Structure

```text
.
|-- docs/
|   `-- usage.md
|-- src/
|   `-- sum_two_numbers/
|       |-- __init__.py
|       |-- __main__.py
|       `-- cli.py
|-- tests/
|   `-- test_sum_two_numbers.py
|-- pyproject.toml
`-- sum_two_numbers.py
```

## Requirements

- Python 3.10 or newer

## Run the Application

From the project root:

```bash
python sum_two_numbers.py 3 4
```

Or install the project in editable mode and use the console command:

```bash
pip install -e .
sum-two-numbers 3 4
```

## Run the Tests

```bash
python -m unittest discover -s tests -v
```

## Documentation

Additional usage notes are available in [docs/usage.md](docs/usage.md).
