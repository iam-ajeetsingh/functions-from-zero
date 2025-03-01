# functions-from-zero

[![Python application test with Github Actions](https://github.com/iam-ajeetsingh/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/iam-ajeetsingh/functions-from-zero/actions/workflows/main.yml)

### To call Microservice 

something like this
```bash
curl -X 'POST' \
  'https://iam-ajeetsingh-functions-from-zero-r7g59wcxx6x-8080.githubpreview.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build container

`docker build .`
`docker image ls`



### Run Docker container

something like this/ Update the image id before running

`docker run -p 127.0.0.1:8080:8080 a81ce4f35866`



### Invoke POST request

run `invoke.sh`



