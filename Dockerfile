FROM python:3.12.1

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"


WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install


COPY . /app/


ENV POETRY_VIRTUALENVS_CREATE=false \
    FILE_NAME="test_data.csv" \
    PAGE_SIZE=10 \
    SORT_BY="surname"


CMD ["poetry", "run", "python", "phonebook.py"]

LABEL image_name=phonebook
