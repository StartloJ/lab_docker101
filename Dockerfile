FROM python:2
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
ENV NAME webapp
CMD ["python", "./webapp.py"]