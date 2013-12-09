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
* [PostgreSQL 9.1.9] [5]
* [libffi 3.0.13+] [6]

[2]: <http://www.python.org/getit/> "Python install documentation"
[3]: <http://www.pip-installer.org/en/latest/installing.html> "Pip install documentation"
[4]: <https://pypi.python.org/pypi/virtualenv> "VirtualEnv install documentation"
[5]: <http://www.postgresql.org/download/> "PostgreSQL download Page"
[6]: <https://sourceware.org/libffi/> "libffi download page"

**Optionnal :**

* [VirtualEnvWrapper 3.7+] [7]

[7]: <http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation> "VirtualEnvWrapper install documentation"

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

You can then navigate to the [hereabove mentionned] [8] address in your browser and will see the web application displayed.

[8]: <http://127.0.0.1:5000> "Localhost Python Django server"

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

## 21 - PRODUCTION ENVIRONMENT

Heroku needs a custom buildpack to integrate [libffi] [6]. This one was created to fit brand-manager needs : [Mibou/heroku-buildpack-python] [9]

[9]: <https://github.com/Mibou/heroku-buildpack-python> "brand-manager Heroku buildpack"

To use it, Heroku buildpack url must be configured as follow :

    heroku config:add BUILDPACK_URL=git://github.com/Mibou/heroku-buildpack-python.git

To take daily dumps, on Heroku, it is needed to add the scheduler add-on :

    heroku addons:add scheduler

## 3 - CONTRIBUTE

To contribute to the brand manager, you must :

1. Download and read the specifications from the [docs folder] [10] at the repository's root.
- Leave a message on the "[Who wants to contribute] [11]" issue #9 ticket.
- Wait to be assigned an issue or take an unasigned issue dropping a comment on it.
- Fork the repository, do your modifications, push them and create a pull request on GitHub. More information about how to contribute in [GitHub documentation] [12].

As much as possible, your changes must validate [PEP8] [13] coding standards. You can also check your contributions using [Pylint] [14].

[10]: <https://github.com/okfn/brand-manager/tree/master/docs> "Documentation folder"
[11]: <https://github.com/okfn/brand-manager/issues/9> "Who wants to contribute"
[12]: <https://help.github.com/articles/fork-a-repo> "GitHub documentation to contribute to a project"
[13]: <http://www.python.org/dev/peps/pep-0008/> "PEP8 coding convention"
[14]: <http://www.pylint.org/> "Pylint"
