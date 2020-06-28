## Where to go
Simple web application on Django, VueJS to help you searching interesting places.
All places have marks on the map and show you information about themselves with a click.


Project was created as first lesson in [module Django](https://dvmn.org/modules/django/) by [Devman](https://dvmn.org)

Test data from [kudago.com](https://kudago.com/)
***
### Demo
Demo: [where-to-go](http://koshkinaleksey.pythonanywhere.com/ "Site demo on pythonanywhere.com")

Administrator panel: [where-to-go/admin](http://koshkinaleksey.pythonanywhere.com/admin)

Administrator login: ``admin`` password: ``1``     
Content Manager login  ``manager`` password: ``2``
***
### How to install
Before installation create and activate [virtualenv](https://virtualenv.pypa.io/en/latest/) for your project.

```
venv/bin/pip install -r requirements.txt
venv/bin/python manage.py create_env
venv/bin/python makemigrations
venv/bin/python migrate
venv/bin/python createsuperuser
venv/bin/python manage.py load_place
venv/bin/python collectstatic
venv/bin/python manage.py runserver
```
