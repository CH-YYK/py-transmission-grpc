FROM python:3.6-slim
COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
# RUN make install

CMD python3 transmission_call_server.py