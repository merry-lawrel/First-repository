# Stores REST API

### Introduction

Stores REST API is an open source platform that enable users to view details about stores and the items in them, and also to insert further details if required.

### Project Support Features

* Users can register and log in to their accounts.
* Public (non-authenticated) users can access details of stores, view all items, insert, delete or update informatiom about them, on the platform.
* Authenticated users can also view details about specific items in a store.

### Installation Guide

* Clone this repository [here](https://github.com/merry-lawrel/First-repository.git)
```
pip install Flask
python app.py

```

### Usage

* Run the previous command to start the application.
* Connect to the API using Postman on port 5000.

### API Endpoints

| HTTP Verbs | Endpoints | Action |
| --- | --------- | --- |
| POST | /register | To sign up a new user account |
| POST | /auth |To authenticate an existing user account |
| GET | /items | To view every item and it's price, in each store |
| GET | /item/<id> | To view details of the required item |
| GET | /store/<name> | To view details of the required store |
| POST | /store/<name> | To insert details of a new store|
| DELETE | /store/<name> | To delete a specific store |
| GET | /stores | To view details of all the stores |
| POST | /item/<id> | To insert details of an item in a specific store using store ID |
| PUT | /item/<id> | To update details of an item in a specific store using store ID |
| DELETE | /item/<id> | To delete an item in a specific store using store ID |

### Technologies Used
* [Flask](https://flask.palletsprojects.com/) Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
* [REST API](https://restfulapi.net/) A REST API is an API that conforms to the design principles of the REST, or representational state transfer architectural style.
* [JWT](https://jwt.io/) JSON Web Token is a proposed Internet standard for creating data with optional signature and/or optional encryption whose payload holds JSON that asserts some number of claims.

