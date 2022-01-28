## User module)
User module is the module of handling user related all the operations.

User Module Structure
------------

    ├── README.md         
    ├── bussiness
    │   ├── user_module
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

## Module-Folder Description

### Business
>user_module
>> This folder is for modules of business logic that includes modules exceptions DTOs, entities, exceptions, services, value objects etc.
>> Some configuration and plugins to make the application itself cleaner.

### Enterprise 

> It is used to write client specific modules entities, mixins,validators etc.

### Infrastructure

> This part of project is for framework or web service you want to user to deploy your business app and also in shared folder you need to configure dependencies injector for using our modules in web service.

### Tests

>This folder will be used to run testcases for business, enterprise and infrastructure to test every module combined.

### setup.py

>It will install all requirements of this module. 



