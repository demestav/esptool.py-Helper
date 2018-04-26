import os
import pathlib
import inquirer
import serial.tools.list_ports

if __name__ == "__main__":

    CWD = pathlib.Path.cwd()

    firmware_files = dict()

    for f in CWD.rglob('*.bin'):
        firmware_files[str(f.relative_to(CWD))] = f

    questions = [
        inquirer.List('port',
            message="Choose port",
            choices=[s[0] for s in serial.tools.list_ports.comports()],
    ),
    inquirer.List('firmware',
            message="Choose firmware",
            choices=firmware_files.keys(),
    ),
    ]
answers = inquirer.prompt(questions)

os.system("esptool.py --port {port} erase_flash".format(port=answers['port']))
os.system("esptool.py --port {port} --baud 460800 write_flash --flash_size=detect 0 {firmware}".format(
        port=answers['port'],
        firmware=firmware_files[answers['firmware']])
    )