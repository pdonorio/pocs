
///////////////////////////////////
// Create the nodejs server app

var port = process.env.PORT || 3000;
var path = require('path');
var express = require('express');

var app = express();
var server = app.listen(port)
var io = require('socket.io')(server);
server.listen(port);

///////////////////////////////////
// serve the index web page to clients
app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.use('/static', express.static('/usr/lib/node_modules'));
app.use('/js', express.static(path.join(__dirname, 'app')));

///////////////////////////////////
// Connect to rethinkdb
// https://www.rethinkdb.com/docs/nodejs/

r = require('rethinkdb')

var myDb = 'test'; // test db already exists when starting fresh rethinkdb
var myTable = 'subscriptions';
var query = r.table(myTable);

r.connect({ host: 'rethink', port: 28015 }, function(err, conn) {
  if(err) throw err;

  r.db(myDb).tableCreate(myTable).run(conn, function(err, res) {
    console.log("Created table", myTable);

    // I don't specify db, searching my table in the global namespace
    query.insert({name: 'Testing the connection'}).run(conn, function(err, res)
    {
        if(err) throw err;
        console.log(res);

        io.on('connection', function (socket) {
          // socket.on('ferret', function (name, fn) {
          //   fn('woot');
          // });

          ///////////////////////////////////
          // do socket.io operations
          console.log("Registering for changes");
          query.changes().run(conn, function(err, cursor) {
              cursor.each(function(err, item) {
                // I should emit this items to socket.io clients
                console.log("Received an update:", item);
                socket.emit('changefeed', item);
              });
          });
        });

    });
  });

});
