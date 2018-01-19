#based on https://stdout.roman.zone/jenkins-docker-python
FROM python
RUN pip install pytest pytest-cov
COPY . /code/
WORKDIR /code
CMD py.test --junitxml=/data/test_report.xml \
            --cov-report xml:/data/coverage.xml
