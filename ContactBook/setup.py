import os

from setuptools import setup


def read(fname: str = None) -> str:
    """read files with in dir"""
    if fname:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Contact Book API",
    version="0.0.1",
    description=read('read.md'),
    packages=(
        'fastapi',
        'sqlalchemy',
        'uvicorn',
        'psycopg2'
        'asyncpg',
        'alembic',
    ),
)
