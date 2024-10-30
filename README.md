# ZEUSX-STRING

Small tool to generate the string required to insert days off or work leave into the ***awesome*** new ZeusX.

### Rquirements

- Python 3.10.11
- PyInstaller 6.11.0

### How to use it

It is highly recommended to follow the steps described below **inside a Python virtual environment**.

1. Install needed python packages:

```shell
    python -m pip install --upgrade pip
    pip install -r requirements.txt
```

2. Create an executable that can run on your machine:
```shell
    pyinstaller --onefile --windowed zeusx.py
```

## IMPORTANT NOTE

This tool allows you to insert values that are ​​inconsistent with each other.

If you want to add functionalities or improve it, feel free to do a PR.