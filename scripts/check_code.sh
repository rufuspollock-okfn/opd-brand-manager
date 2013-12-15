pep8 --exclude=migrations --ignore=E501,E225 manager
pyflakes -x W manager
python setup.py test
