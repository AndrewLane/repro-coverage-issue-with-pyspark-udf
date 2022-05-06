# repro-coverage-issue-with-pyspark-udf
An attempt to repro https://github.com/nedbat/coveragepy/issues/658

## Steps to repro issue

1. Clone repo
2. ```docker-compose up -d```
3. ```docker attach protonai-pyspark-container```
4. ```pip install pytest==7.0.1```
5. ```pip install coverage==6.2```
6. ```cd /home/```
7. ```coverage run --source=./src -m pytest tests/test.py --disable-pytest-warnings```
8. ```coverage report```

## Expected Results

Expecting the code in the user-defined function to be "seen" by coverage and therefore have 100% code coverage.

## Actual Results

```
# coverage report
Name          Stmts   Miss  Cover
---------------------------------
src/code.py      11      5    55%
---------------------------------
TOTAL            11      5    55%
```
