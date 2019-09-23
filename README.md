# c00kie-stealer

🔪🍪 Extracts cookies from well known browsers 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cookie-stealer.

```bash
pip3 install -r requirments.txt
```

*NOTE: WINDOWS USERS REQUIRE [MS Visual Studio 2015](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx) (Community Edition) with C/C++ compilers, and may need to reinstall pycryptodome. For more info please visit [this link](https://pycryptodome.readthedocs.io/en/latest/src/installation.html#windows-from-sources-python-3-5-and-newer)*

```bash
pip3 install pycryptodomex --no-use-wheel
```

## Usage

This will save all the cookies in 'cookies.json' and will show logs files.

```bash
$ python3 CookieStealer
 
***   RUNNING 'CookieStealer.py'   ***

[!]Getting chrome cookies...
    [+]Got chrome cookies without any exceptions!
[!]Getting chrome firefox...
    [+]Got firefox cookies without any exceptions!
[!]Getting safari cookies...
    [+]Got safari cookies without any exceptions!
[!]Creating dict for all cookies found...
    [!]Creating dict for chrome browser cookies...
        [+]Chrome browser cookie dict created!
    [!]Creating dict for firefox browser cookies...
        [+]Firefox browser cookie dict created!
    [!]Creating dict for safari browser cookies...
        [+]Safari browser cookie dict created!
    [!]Saving the duct in json file...
        [+]Cookie list saved to the 'cookies.json' file!

***  COOKIES ARE SAVED TO 'cookies.json' FILE    ***
***  EXITING PYTHON  ***
```

## Browser Support

* ***Chrome***
* ***Firefox***
* ***Safari***

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU Lesser General Public License v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
