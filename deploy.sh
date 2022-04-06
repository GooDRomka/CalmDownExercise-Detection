docker build -t elomia-ml-build .
docker run -d -p 80:80 --name elomia-api elomia-ml-build