FROM python:3.12.2

WORKDIR /app

COPY . .

RUN pip install -r req.txt
RUN pip install requests 

CMD ["./entry.sh"]
