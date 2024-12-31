FROM python:3
ENV DIRPATH=/user/src/app
WORKDIR ${DIRPATH}
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "./app.py" ]