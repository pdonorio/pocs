
# uWSGI + nginx

Starting the stack:
```bash
$ docker-compose up
# attaching to containers log
```

To check directly app logs:
```bash
$ docker-compose exec backend tailf /var/log/uwsgi/app.log
```

To query the server from the client container:
```bash
docker-compose exec client http GET api:3031/hello
```

---

Inspired by the following articles on the web:
http://www.one-tab.com/page/bueKK2aERPu8Y5IdcWnANg
