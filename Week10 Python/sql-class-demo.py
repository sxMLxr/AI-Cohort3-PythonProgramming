# -*- coding: utf-8 -*-
"""
See chinook example database and description:
    https://www.sqlitetutorial.net/sqlite-sample-database/
"""
# import the SQLAlchemy libraries required
import sqlalchemy, sqlalchemy.orm, sqlalchemy.ext.automap

# create the automap base object
db_base = sqlalchemy.ext.automap.automap_base()

# define our database connection
db_engine = sqlalchemy.create_engine("sqlite+pysqlite:///chinook.db", 
                      echo=False) # set to True for logging/debugging

# connect to the database, retrieve table mappings to Classes
db_base.prepare(db_engine, reflect=True)

# create a session object to use for querries
DBSession = sqlalchemy.orm.sessionmaker(bind=db_engine)
db_session = DBSession()

# Get the employees class that was created.
Employees = db_base.classes["employees"]

# find employee with highest EmployeeId
employee1 = db_session.query(Employees) \
                .order_by(sqlalchemy.desc(Employees.EmployeeId)) \
                    .first()

# show some output
print(f"{employee1.LastName} has id {employee1.EmployeeId} and reports to...")

manager = db_session.query(Employees) \
            .filter(Employees.EmployeeId == employee1.ReportsTo) \
                .first()

print(f"{manager.LastName} with id {manager.EmployeeId} ", end='')

print("who has all the following employees as direct reports:")

reports_list = db_session.query(Employees) \
            .filter(Employees.ReportsTo == manager.EmployeeId) \
                .order_by(sqlalchemy.desc('EmployeeId')) \
                    .all()

for emp in reports_list:
    print(f"\t{emp.LastName} id {emp.EmployeeId}")

