# fastapidocker

This API only selects all users from the database and lists them when calling the root endpoint (/).

For now the only way to add new users is to do it directly to mongodb and it can be done in the mongo shell with the command:
db.<collection name>.insert({"username": "<choose a username>", "password": "<choose a password>"})
in my db it would be something like this:
db.users.insert({"username": "anton", "password": "Sup3rStr0ngPa55WORD"})

the .env-file should be in the /app/ directory and should have two vaiables.
1. the mongodb-uri. (i.e. "mongodb://localhost")
2. the port that mongodb is running on (default is 27017)
