FROM python:3.7

# working directory
WORKDIR /usr/src/app

# add the python application
ADD demo_app.py .

# copy requirements file to working directory
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "./demo_app.py"]
