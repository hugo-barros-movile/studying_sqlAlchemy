# studying_sqlAlchemy

This can be tested running:

make bootstrap ; source venv/bin/activate ; make deps ; make run



CURL command that creates user:
curl -X POST "http://localhost:5000/?user=hugo&pass=senha"

CURL command that login:
curl -X POST "http://localhost:5000/login/?user=hugo&pass=senha"
(doesnt do anything really, just checks the password)

CURL command that checks if user exists:
curl -X GET "http://localhost:5000/?user=hugo"
