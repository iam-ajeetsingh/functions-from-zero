#FROM public.ecr.aws/lambda/python:3.8       # this image is commented because it gave following error: 

# ImportError: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2k-fips  26 Jan 2017'.
# use below image instead it worked. 

FROM python:3.8-slim

RUN mkdir -p /app
COPY ./main.py /app/
COPY mylib/ /app/mylib/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]