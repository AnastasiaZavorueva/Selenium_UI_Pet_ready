FROM python:3.10

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY .. /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "C:\Users\DELL\PycharmProjects\Selenium_UI_Pets_ready"]