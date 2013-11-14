# 1 - DESCRIPTION

This is the source code corresponding to [OKFN Open Product Data] [1] brand manager developped with Python Django framework version 1.6.

[1]: <http://product.okfn.org> "OKFN Open Product Data website"

# 2 - INSTALLATION

## 21 - DEVELOPMENT ENVIRONMENT

### 211 - PREREQUISITES

**Mandatory :**

* [Python 2.7.5+] [2]
* [Pip 1.3.1+] [3]
* [VirtualEnv 1.9+] [4]

[2]: <http://www.python.org/getit/> "Python install documentation"
[3]: <http://www.pip-installer.org/en/latest/installing.html> "Pip install documentation"
[4]: <https://pypi.python.org/pypi/virtualenv> "VirtualEnv install documentation"

**Optionnal :**

* [VirtualEnvWrapper 3.7+] [5]

[5]: <http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation> "VirtualEnvWrapper install documentation"

### 212 - CONFIGURATION

1. Create a virtual environment using virtualenv (or if you installed it, virtualenvwrapper).
- Activate your virtual environment.
- Clone the current git repository.
- Install the requirements with pip :

  > `pip install -r requirements.txt`

- Add the Django settings in your virtalenv postactivate script :
  
  > `echo 'export DJANGO_SETTINGS_MODULE="manager.settings.dev"' >> ~/pyve/pod/bin/postactivate`

### 213 - RUN

To run the server, from your virtual environment, only one command is needed :

> `python manage.py runserver 0.0.0.0:8001`

This command should return :

        Validating models...
        
        0 errors found
        November 13, 2013 - 20:17:27
        Django version 1.6, using settings 'manager.settings'
        Starting development server at http://0.0.0.0:8001/
        Quit the server with CONTROL-C.

You can then navigate to the [hereabove mentionned] [6] address in your browser and will see the web application displayed.

[6]: <http://127.0.0.1:8001> "Localhost Python Django server"

