'use strict';

// Web Sockets in plain javascript
/*
  var socket = io.connect('http://localhost');
  socket.on('changefeed', function (data) {
    console.log("Server pushed data from rethinkdb:", data);
    // // if you want to send data back via websockets...
    // socket.emit('my other event', { my: 'data' });
  });
*/

angular.module('myApp', [
    'btford.socket-io',
    //'ui.router',
])

.factory('socket', function (socketFactory) {
  return socketFactory({
    // the address where the server is
    // (note: socket.io must be exposed)
    ioSocket: io.connect('http://localhost')
  });
})

.controller('MyCtrl', function ($scope, socket) {
  console.log("Controller loaded");
  $scope.messages = [];

  socket.on('changefeed', function (data) {
    console.log("Server pushed data from rethinkdb:", data);
    $scope.messages.push(data);
  });
})
