# 1 - DESCRIPTION

This is the source code corresponding to [Open Knowledge Foundation Open Product Data] [1] brand manager developped with Python Django framework version 1.6.

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

  `pip install -r requirements/dev.txt`

- Add the Django settings in your virtalenv postactivate script :
  
  `echo 'export DJANGO_SETTINGS_MODULE="manager.settings.dev"' >> ~/pyve/pod/bin/postactivate`

- Prepare the test database with the Django dumped data :

        # At this point the database configured in settings/dev.py is empty
        python manage.py syncdb
        # At this point the database contains the Django default tables
        python manage.py sqlflush |psql -h localhost -U <user> <dbname>
        # At this point the database contains the Django default tables emptyied
        python manage.py loaddata sql/django_brand_data_2013.11.18_01.json
        # At this point the database contains the Django testing data

### 213 - RUN

To run the server, from your virtual environment, only one command is needed :

`foreman start`

This command should return something like :

    11:41:18 web.1  | started with pid 1839
    11:41:19 web.1  | 2013-11-18 11:41:19 [1842] [INFO] Starting gunicorn 18.0
    11:41:19 web.1  | 2013-11-18 11:41:19 [1842] [INFO] Listening at: http://0.0.0.0:5000 (1842)
    11:41:19 web.1  | 2013-11-18 11:41:19 [1842] [INFO] Using worker: sync
    11:41:19 web.1  | 2013-11-18 11:41:19 [1847] [INFO] Booting worker with pid: 1847

You can then navigate to the [hereabove mentionned] [6] address in your browser and will see the web application displayed.

[6]: <http://127.0.0.1:8001> "Localhost Python Django server"

