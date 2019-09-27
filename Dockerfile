FROM python:alpine
LABEL maintainer="Nick <linickx.com>"
LABEL version="0.1"

RUN apk add --no-cache gcc libc-dev python3 python3-dev net-snmp net-snmp-dev

RUN pip install easysnmp

WORKDIR /app
ENTRYPOINT ["python3"]
