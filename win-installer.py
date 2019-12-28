import subprocess
import sys

pycryptodome_wheels = [
    'pycryptodome-3.9.4-cp27-cp27m-win_amd64.whl',
    'pycryptodome-3.9.4-cp27-cp27m-win32.whl',
    'pycryptodome-3.9.4-cp34-cp34m-win_amd64.whl',
    'pycryptodome-3.9.4-cp34-cp34m-win32.whl',
    'pycryptodome-3.9.4-cp35-cp35m-win_amd64.whl',
    'pycryptodome-3.9.4-cp35-cp35m-win32.whl',
    'pycryptodome-3.9.4-cp36-cp36m-win_amd64.whl',
    'pycryptodome-3.9.4-cp36-cp36m-win32.whl',
    'pycryptodome-3.9.4-cp37-cp37m-win_amd64.whl',
    'pycryptodome-3.9.4-cp37-cp37m-win32.whl',
    'pycryptodome-3.9.4-cp38-cp38-win_amd64.whl',
    'pycryptodome-3.9.4-cp38-cp38-win32.whl'
]

lz4_wheels = [
    'lz4-2.2.1-cp27-cp27m-win_amd64.whl',
    'lz4-2.2.1-cp27-cp27m-win32.whl',
    'lz4-2.2.1-cp34-cp34m-win_amd64.whl',
    'lz4-2.2.1-cp34-cp34m-win32.whl',
    'lz4-2.2.1-cp35-cp35m-win_amd64.whl',
    'lz4-2.2.1-cp35-cp35m-win32.whl',
    'lz4-2.2.1-cp36-cp36m-win_amd64.whl',
    'lz4-2.2.1-cp36-cp36m-win32.whl',
    'lz4-2.2.1-cp37-cp37m-win_amd64.whl',
    'lz4-2.2.1-cp37-cp37m-win32.whl',
    # Not Created yet...
    # 'lz4-2.2.1-cp38-cp38-win_amd64.whl',
    # 'lz4-2.2.1-cp38-cp38-win32.whl'
]

for i in pycryptodome_wheels:
    subprocess.Popen([sys.executable, "-m", "pip", "install", 'win-wheels\\'+i], ).communicate()

for j in lz4_wheels:
    subprocess.Popen([sys.executable, "-m", "pip", "install", 'win-wheels\\'+j], ).communicate()

subprocess.Popen([sys.executable, "-m", "pip", "install", 'win-wheels\\'+'keyring-21.0.0-py2.py3-none-any.whl'], )\
    .communicate()


# subprocess.Popen([sys.executable, "-m", "pip", "install", "-r", 'requirments.txt'], ).communicate()

# Python 3.8's lz4 libs wheel has not been made yet, so it will not support lz4 as Microsoft Visual C++ Build Tools
# if not installed, and VS C++ is over 7+ GB of data to be installed so we will have to wait till the creation of the
# 3.8's wheel

try:  # trying to import all the installed modules
    try:
        from Cryptodome.Protocol.KDF import PBKDF2
        from Cryptodome.Cipher import AES
    except ImportError:  # Just in case...
        from Crypto.Protocol.KDF import PBKDF2
        from Crypto.Cipher import AES
    import lz4.block
    import keyring
    print("Installed successfully!\nDont worry about the errors.")
except:
    raise Exception(f"All packages could not be installed, please make sure your using the current virsion of python"
                    f"If nothing works then you need to install VS C++ Tool Kit and then execute:"
                    f"'{sys.executable} -m pip install -r requirments.txt'\n")
