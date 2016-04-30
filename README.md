
Please follow the below steps:

- Create a python virtual env

- To activate the virtualenv

$ source virtualenvname/bin/activate

- install the tools(in requirements.txt) 

- To runserver

$ cd mozbe

$ python manage.py runserver                            ---> Default running at 8000


The below APIs can be used to create/update, bulk create/bulk update providers and polygon areas

## For Providers 

Providers List 				- ": "http://127.0.0.1:8000/api/account/providers/"

Create Provider 			- ": "http://127.0.0.1:8000/api/account/provider/createprovider"

Provider Detail				- ": "http://127.0.0.1:8000/api/account/provider/{{provider_id}}/"

PROVIDER Batch operations: post/put/del	- ": "http://127.0.0.1:8000/api/account/provider-batch-operate/"


## For Areas

Areas List 				- ": "http://127.0.0.1:8000/api/account/areas/"

Create Area 				- ": "http://127.0.0.1:8000/api/account/area/create-area"

Area Detail 				- ": "http://127.0.0.1:8000/api/account/area/{{area_id}}"

AREA Batch operations: post/put/del 	- ": "http://127.0.0.1:8000/api/account/area-batch-operate/"



