### Windows package for better installation experience

# Path: windows.md
### Windows package for better installation experience

## Installation

### Install from Chocolatey

```bash 
pip install pyinstaller
# Now you can use pyinstaller to build your application
pyinstaller --onefile yourscript.py
# it will create a folder dist with your executable inside it.You can distribute this executable file to your Windows users, and they can run it without needing to install any dependencies or set up a Python environment
# If you want to create a .exe file, you can use the following command
pyinstaller --onefile --windowed yourscript.py
# The --windowed option will hide the console window when the application is running
```

### My Generated .exe file 

 ## [app.exe](/Flask-app/dist/app)


## How to use

### 1. Open the app.exe file

### 2. Enter the name of the file you want to convert

### 3. Enter the name of the file you want to save

### 4. Click on the convert button

### 5. The converted file will be saved in the same folder as the app.exe file

### 6. You can open the converted file with any text editor

### 7. You can also open the converted file with any spreadsheet editor

### 8. You can also open the converted file with any database editor

### Logs
    
```bash

117 INFO: PyInstaller: 5.8.0

117 INFO: Python: 3.8.10

136 INFO: Platform: Linux-5.15.

0-67-generic-x86_64-with-glibc2.29

137 INFO: wrote /home/avijit69/Desktop/Projects/

flask-windows-package/Flask-app/app.spec

142 INFO: UPX is not available.

143 INFO: Extending PYTHONPATH with paths

['/home/avijit69/Desktop/Projects/flask-windows-package/Flask-app']

605 INFO: checking Analysis

616 INFO: checking PYZ

623 INFO: checking PKG

624 INFO: Bootloader /home/avijit69/.local/lib/python3.8/site-packages/PyInstaller/bootloader/Linux-64bit-intel/run

625 INFO: checking EXE

626 INFO: Building because console changed

626 INFO: Building EXE from EXE-00.toc

631 INFO: Copying bootloader EXE to /home/avijit69/Desktop/Projects/flask-windows-package/Flask-app/dist/app

632 INFO: Appending PKG archive to custom ELF section in EXE

691 INFO: Building EXE from EXE-00.toc completed successfully.

```

              