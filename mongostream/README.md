
# mongo changes stream

Testing on rc6 of mongo4.

It seems that mongo needs to have a replica set, usually for a cluster:
```
OperationFailure: The $changeStream stage is only supported on replica sets
```

That's why I've looked up to:
https://gist.github.com/davisford/bb37079900888c44d2bbcb2c52a5d6e8

So far my test:

```bash

docker-compose up -d

# mongo shell
docker-compose exec db bash
mongo
rs.initiate({_id: "replocal", members: [{_id: 0, host: "127.0.0.1:27017"}] })
rs.status

# ipython first shell
docker-compose exec py ash
pip3 install --upgrade ipython pymongo
ipython

from pymongo import MongoClient
client = MongoClient('db')
db = client.MyTest
cursor = db.MyCollection.watch()
## Current issue: 
## OperationFailure: Storage engine does not support read concern: { readConcern: { level: "majority" } }

# ipython second shell
docker-compose exec py ash
ipython

from pymongo import MongoClient
client = MongoClient('db')
db = client.MyTest
db.MyCollection.insert_one({'a': 5, 'b':7})
```
