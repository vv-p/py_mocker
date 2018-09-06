FROM python:3.7
LABEL maintainer="vvp@protonmail.ch"

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python3 -m pip install --index-url https://test.pypi.org/simple/ py_mocker

EXPOSE 8080
ENTRYPOINT ["python", "-m", "py_mocker" ]
