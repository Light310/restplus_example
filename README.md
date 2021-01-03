### RESTPlus example

##### FILE TREE
```
├── api                           #
│   ├── some_service              #  API directory for this service
│   │   ├── business.py           #  methods for CRUD operations on entities in this service
│   │   ├── endpoints             #  API namespaces and REST methods
│   │   │   ├── some_entity.py    # 
│   │   │   ├── another_entity.py #
│   │   │   └── third_entity.py   #
│   │   ├── parsers.py            #  Custom argument parsers (if needed)
│   │   └── serializers.py        #  Output serializers
│   └── restplus.py               #  API bootstrap file
├── app.py                        #  Application bootstrap file
├── database                      #
│   └── models.py                 #  Definition of SQLAlchemy models
├── db.sqlite                     #
└── settings.py                   #  Global app settings
```

##### ENTITIES DESCRIPTION
```
some_entity is a main entity with foreign key to another_entity
another_entity is a key-value dictionary
third_entity is just a random entity with 3 fields (and different type of update methods)
it is definetely not good and should only be used with a client
```

##### ADDING A NEW ENTITY
```
To add a new entity, create a folder in api folder
Inside it :
endpoints folder represents endpoints for each entity
business (methods for CRUD operations), parsers, serializers files provide methods for this endpoints to work

database/models.py stores db models, representing new entities. Add a model for each entity
database/__init__.py - add import here

app.py :
imports :
from api.some_service.endpoints.some_entity import ns as some_entity_namespace

initialize_app :
api.add_namespace(some_entity_namespace)
```

##### INSTALLATION
```
python3 -m venv env
source env/bin/activate
python3 -m pip install -r restplus_example/requirements.txt

in settings.py change FLASK_SERVER_NAME ip to ip of your remote server

To create a database for 1st run:
python restplus_example/run_reset_database.py

To start run this in activated virtual environment : 
python restplus_example/restplus_example/app.py

To recreate a database after model change run script restplus_example/run_reset_database.py
```