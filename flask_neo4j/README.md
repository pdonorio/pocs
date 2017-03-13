
# Use neo4j and neomodel inside Flask

This is a proof of concept based on a discussion inside [this issue](https://github.com/robinedwards/neomodel/issues/244).

The idea is to test a neomodel flask extension written by us inside a much more real scenario than the usual Flask quickstart. To do so I've implemented this poc with the [Application Factories pattern](http://flask.pocoo.org/docs/0.12/patterns/appfactories/).

## Use it

I always use docker to test databases connections.
I've put up a quick YAML file to configure two containers:

1. The latest neo4j graphdb (v3.1) with a password
2. A flask server upon the official alpine python (v3.6) docker image

Variables can be found/set inside the `.env` file.
To bring the stack alive, you just do from this directory:

```
$ docker-compose up

Creating flaskneo4j_flasker_1
Creating flaskneo4j_graphdb_1
Attaching to flaskneo4j_flasker_1, flaskneo4j_graphdb_1
flasker_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
flasker_1  |  * Restarting with stat
flasker_1  |  * Debugger is active!
flasker_1  |  * Debugger PIN: 270-615-037
graphdb_1  | Changed password for user 'neo4j'.
graphdb_1  | Starting Neo4j.
graphdb_1  | 2017-03-13 08:53:17.151+0000 INFO  No SSL certificate found, generating a self-signed certificate..
graphdb_1  | 2017-03-13 08:53:18.062+0000 INFO  Starting...
graphdb_1  | 2017-03-13 08:53:18.942+0000 INFO  Bolt enabled on 0.0.0.0:7687.
graphdb_1  | 2017-03-13 08:53:23.864+0000 INFO  Started.
graphdb_1  | 2017-03-13 08:53:25.408+0000 INFO  Remote interface available at http://localhost:7474/

```

## Query the Flask server

The only endpoint is configured through the blueprint as '/test/'.

The flask container has the flask port mapped to your local 8080 port,
so to access the server, you can execute on your host:

```
# Wait a few seconds after the compose up command
# As neo4j is not really fast a bringing the interface up

$ curl -i localhost:8080/test/

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 11
Server: Werkzeug/0.12 Python/3.6.0
Date: Mon, 13 Mar 2017 21:13:17 GMT

just a test
```

And in the server logs you should read:

```
flasker_1  | --------------------------------------------------------------------------------
flasker_1  | DEBUG in blueprint [/code/blueprint.py:13]:
flasker_1  | graph db object: <neomodel.util.Database object at 0x7f7fa8b912e8>
flasker_1  | --------------------------------------------------------------------------------
flasker_1  | --------------------------------------------------------------------------------
flasker_1  | INFO in blueprint [/code/blueprint.py:16]:
flasker_1  | created test object: {'name': 'just a test', 'id': 0}
flasker_1  | --------------------------------------------------------------------------------
flasker_1  | 172.19.0.1 - - [13/Mar/2017 21:13:17] "GET /test/ HTTP/1.1" 200 -
```


Final note: the graphdb has no docker volume,
so by restarting it you lose all the data.



