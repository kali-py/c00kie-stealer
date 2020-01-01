# c00kie-stealer

🔪🍪 Extracts cookies from well known browsers 

***NOTE: THIS PROJECT MAY NOT WORK AS OF 2019***

## Installation

For ***Windows*** users use the file `win-installer.py` to install, make sure you have package manager [pip](https://pip.pypa.io/en/stable/) installed.

```bash
python3 win-installer
```

For ***Linux*** and ***MacOS*** Users use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip3 install -r requirments.txt
```

*Note for Windows users: If the file `win-installer.py` doesnt work then you will need to install [MS Visual Studio 2015](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx) (Community Edition) with C/C++ compilers, and then install requirements using pip with the following command:* `pip3 install -r requirments.txt`

## Usage

*Usage as a executable:* This will save all the cookies in 'cookies.json' and will show logs files.

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

*Usage as a library:* This will use the browsercookie library to get cookiejar objects from the cookie from major browser.

```python
import lib_bc

# Get Chrome browser cookies:
ChromeCookieJar = lib_bc.chrome()

# Get Firefox browser cookies:
FirefoxCookieJar = lib_bc.firefox()

# Get Safari browser cookies:
SafariCookieJar = lib_bc.safari()

''' more code... '''
```


## Browser Support

* ***Chrome***
* ***Firefox***
* ***Safari***

## Acknowledgements

* **bin0x00** - For initializing the this project.
* **richardpenman** - For making the [browsercookie library](https://bitbucket.org/richardpenman/browsercookie)
  * More acknowledgements at richardpenman repo
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU Lesser General Public License v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
