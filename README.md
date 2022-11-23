# fastapidocker

### This API only selects all users from the database and lists them when calling the root endpoint (/).<br><br>
For now the only way to add new users is to do it directly to mongodb and it can be done in the mongo shell with the command:<br>
`db.???.insert({"username": "???", "password": "???"})`<br><br>
in my db it would be something like this:<br>
`db.users.insert({"username": "anton", "password": "Sup3rStr0ngPa55WORD"})`<br><br>
the .env-file should be in the /app/ directory and should have two vaiables.<br>
1. the mongodb-uri. (i.e. "mongodb://localhost")<br>
2. the port that mongodb is running on (default is 27017)<br>
