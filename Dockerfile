FROM python:3.9

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501

COPY models .
COPY scripts .
COPY apps .
COPY features_schema.sql .

CMD streamlit run apps/main.py
