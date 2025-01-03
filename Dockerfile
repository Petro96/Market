FROM python:3.12.2
 
ENV DIRPATH=/user/src/app

WORKDIR ${DIRPATH}

RUN apt-get update && apt-get install -y build-essential libffi-dev libc-dev python3-dev
RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt ./
RUN pip install --upgrade -r requirements.txt
COPY . .

CMD [ "python", "./run.py" ]