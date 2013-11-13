# 1 - DESCRIPTION

This is the source code corresponding to OKFN Open Product Data ( http://product-open-data.com/ ) brand manager developped with Python Django framework version 1.6.

# 2 - INSTALLATION

## 21 - DEVELOPMENT ENVIRONMENT

### 211 - PREREQUISITES

**Mandatory :**

* [Python 2.7.5+] [1]
* [Pip 1.3.1+] [2]
* [VirtualEnv 1.9+] [3]

[1]: <http://www.python.org/getit/> "Python install documentation"
[2]: <http://www.pip-installer.org/en/latest/installing.html> "Pip install documentation"
[3]: <https://pypi.python.org/pypi/virtualenv> "VirtualEnv install documentation"

**Optionnal :**

* [VirtualEnvWrapper 3.7+] [4]

[4]: <http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation> "VirtualEnvWrapper install documentation"

### 212 - CONFIGURATION

1. Create a virtual environment using virtualenv (or if you installed it, virtualenvwrapper).
- Activate your virtual environment.
- Clone the current git repository.
- Install the requirements with pip :

  > `pip install -r requirements.txt`

- Add the Django settings in your virtalenv postactivate script :
  
  > `echo 'export DJANGO_SETTINGS_MODULE="pod.manager.settings.dev"' >> ~/pyve/pod/bin/postactivate`

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

You can then navigate to the [hereabove mentionned] [5] address in your browser and will see the web application displayed.

[5]: <http://127.0.0.1:8001> "Localhost Python Django server"
t
