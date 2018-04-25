# A simple helper script for esptool.py
The script allows the user to easily choose the port and the `bin` file for flashing the ESP module.

## Usage
Place the bin files in the current directory.

Install the dependencies in `Pipenv` file.
```
pipenv lock
pipenv sync
```

Connect the module to PC and run
```
python esptoolhelper.py
```

## Comments
This version is a quick and dirty solution since I had to flash many modules with different Micropython. Hopefully to be improved in the future!

## TODO
- Provide option to download firmware directly from micropython.org

## Dependencies
- inquirer
- pyserial
- esptool