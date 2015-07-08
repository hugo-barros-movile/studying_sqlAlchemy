# studying_sqlAlchemy

This can be tested running:

```
$ make test
```
If you want to run your own server, just run:

```
$ make run
```
Some examples for you try:

```
$ curl -X POST "http://localhost:5000/?user=hugo&pass=senha"
```
```
$ curl -X POST "http://localhost:5000/login/?user=hugo&pass=senha"
```
(doesnt do anything really, just checks the password)

```
$ curl -X GET "http://localhost:5000/?user=hugo"
```