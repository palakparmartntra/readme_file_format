## Module Description (ex. user module)
Outline a brief description of your module. user module is the module of handling user relation all the opration.

Module-folder structure
------------

    ├── README.md         
    ├── bussiness
    │   ├── module name
    │   │   ├── DTOs
    │   │   ├── entities
    │   │   ├── exceptions
    │   │   ├── services
    │   │   ├── value_objects
    │   │   └── __init__.py  
    │   └── __init__.py
    │
    ├── enterprise
    │   ├── entities
    │   ├── mixins
    │   ├── validators
    │   ├── value_objects
    │   └── __init__.py
    │
    ├── infrastructure
    │   └──shared
    │
    ├── tests        
    │   │── bussiness
    │   │── enterprise
    │   └── infrasturcture
    │
    ├── __init__.py          
    │
    └── setup.py        

--------

## Module-folder description

### Business
>module_name
>> This folder is for modules of business logic that includes modules exceptions DTOs, entities, exceptions, services, value objects etc.
>> Some configuration and plugins to make the application itself cleaner.

### Enterprise 

> It is used to write client specific modules entities, mixins,validators etc.

### infrastructure

> This part of project is for framework or web service you want to user to deploy your business app and also in shared folder you need to configure dependencies injector for using our modules in web service.

### tests

>This folder will be used to run testcases for business, enterprise and infrastructure to test every module combined.

### setup.py

for setup of this module.



