

#  Instructions


### 1. Build the docker image

```
docker build -t elomia-ml-build .
```

### 2. Run the container

```
docker run -d -p 80:80 --name elomia-api elomia-ml-build 
```

### 3. Run Pytest with coverage
```
docker exec -it elomia-api pytest --ignore=tests/ --cov=app tests/ --cov-config=.coveragerc
```

### 4. Go to localhost
http://127.0.0.1/docs


### 5. Try out the post /predict method
body format is:
```
{"data":
        {"text":
            List[str]
        }
}
```
Try to run via python library request:
```
python request.py
```
