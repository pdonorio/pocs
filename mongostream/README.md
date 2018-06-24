
# Mongo changes stream

Available from 3.6.

## 1. start

```bash
# make sure no data is existing from previous tests:
rm -rf data
# start the stack
docker-compose up

# see mongo's logs
[...]
```

## 2. configure mongo

To activate the streams we need mongo configured to be a replica set.

```bash
# mongo shell
docker-compose exec db bash
mongo
rs.initiate({_id: "replocal", members: [{_id: 0, host: "127.0.0.1:27017"}] })
rs.status
```

## 3. register to a stream

Open a first shell in the python container to get an iterator to follow the changes of a collection.

```bash
# python first shell
docker-compose exec py ash
# install missing libraries
pip3 install --upgrade ipython pymongo
# go with interactive python
ipython

from pymongo import MongoClient
client = MongoClient('db')
db = client.MyTest
cursor = db.MyCollection.watch()
```

## 4. add elements to the collection

Open another shell on the same container to push modifications

```bash
# python second shell
docker-compose exec py ash
ipython

from pymongo import MongoClient
client = MongoClient('db')
db = client.MyTest
db.MyCollection.insert_one({'a': 5, 'b':7})
```

You can see in the previous shell that changes are received as well.

## 5. clean up

```bash
docker-compose down -v
```

Cheers
