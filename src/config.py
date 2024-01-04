import pymysql
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
connection_string = 'mysql+pymysql://root:@localhost:3306/carehealth'
engine = create_engine(connection_string)