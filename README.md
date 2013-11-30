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
* [PostgreSQL] [5]

[2]: <http://www.python.org/getit/> "Python install documentation"
[3]: <http://www.pip-installer.org/en/latest/installing.html> "Pip install documentation"
[4]: <https://pypi.python.org/pypi/virtualenv> "VirtualEnv install documentation"
[5]: <http://www.postgresql.org/download/> "PostgreSQL Download Page"

**Optionnal :**

* [VirtualEnvWrapper 3.7+] [6]

[6]: <http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation> "VirtualEnvWrapper install documentation"

### 212 - CONFIGURATION

1. Create a virtual environment using virtualenv (or if you installed it, virtualenvwrapper).
- Activate your virtual environment.
- Clone the current git repository.
- Install the requirements with pip :

  `pip install -r requirements/dev.txt`

- Add the Django settings in your virtalenv postactivate script :
  
  `echo 'export DJANGO_SETTINGS_MODULE="manager.settings.dev"' >> ~/pyve/pod/bin/postactivate`

- Prepare the test database with the Django dumped data (in the last command replace #### by the latest migration number) :

        # First, we need to create a new role 'pod' with PostgreSQL 
        createuser pod
        # Now, we need to create a new database 'pod_brand' with PostgreSQL
        createdb pod_brand
        # At this point the database configured in settings/dev.py is empty
        python manage.py syncdb --migrate
        # At this point the database contains the Django default tables
        python manage.py sqlflush |psql -h localhost -U <user> <dbname>
        # At this point the database contains the Django default tables emptyied
        python manage.py loaddata sql/django_brand_data_####.json
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

You can then navigate to the [hereabove mentionned] [7] address in your browser and will see the web application displayed.

[7]: <http://127.0.0.1:5000> "Localhost Python Django server"

### 214 - MIGRATE

To migrate the database, only one command is needed :
`python manage.py migrate brand`

If you encounter some problems or your database is corrupted :
`dropdb pod_brand`
Then re-prepare the test database (except the role 'pod', which stays there)

### 215 - UPDATING DATABASE

When you modify the model, you'll need to update the database :
`python manage.py schemamigration --auto brand`

If there was no problem, update the dump (replace #### by the migration number) :
`python manage.py dumpdata > sql/django_brand_data_####.json`

### 216 - Contribute

To contribute to the brand manager, you must :

1. Download and read the specifications from the [docs folder] [8] at the repository's root.
- Leave a message on the "[Who wants to contribute] [9]" issue #9 ticket.
- Wait to be assigned an issue or take an unasigned issue dropping a comment on it.
- Fork the repository, do your modifications, push them and create a pull request on GitHub. More information about how to contribute in [GitHub documentation] [10].

As much as possible, your changes must validate [PEP8] [11] coding standards. You can also check your contributions using [Pylint] [12].

[8]: <https://github.com/okfn/brand-manager/tree/master/docs> "Documentation folder"
[9]: <https://github.com/okfn/brand-manager/issues/9> "Who wants to contribute"
[10]: <https://help.github.com/articles/fork-a-repo> "GitHub documentation to contribute to a project"
[11]: <http://www.python.org/dev/peps/pep-0008/> "PEP8 coding convention"
[12]: <http://www.pylint.org/> "Pylint"
