
# uWSGI + nginx

Note:
I started the first prototype with the mode emperor/vassals.

I then went back to a master typical multi-thread as the former was
too complicated for just one app, and also difficult to debug.

---

## Test it

Starting the stack:
```bash
$ docker-compose up
# attaching to containers log
```

To see the load of workers like unix top:
```bash
docker-compose exec backend uwsgitop localhost:9191
# press 'q' to quit
```

To query the server from the client container:
```bash
docker-compose exec client http GET api/hello
```

---

## Sources

Inspired by the following articles (in that particular order):

http://www.one-tab.com/page/proi2hD7TRWXsy858iIzzA

The docker image for the server was built here:

https://hub.docker.com/r/pdonorio/py3apil/~/dockerfile/
