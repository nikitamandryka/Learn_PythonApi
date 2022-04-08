From python
WORKDIR /tests_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
cmd python -m pytest -s --alluredir=tests_result/ /tests_project/tests/