FROM python:3
RUN  mkdir WORK_REPO
RUN  cd  WORK_REPO
WORKDIR  /WORK_REPO
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY normalization.py .
ENTRYPOINT ["python", "normalization.py"]