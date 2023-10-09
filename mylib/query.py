"""Query the database via connection to databricks"""
import os
from databricks import sql
from dotenv import load_dotenv

def complex_query():
    """runs a complex query"""

    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute("""SELECT c.iyear, SUM(c.UK)/SUM(y.fatalities) AS UK_prop_of_tot_fatalities
                    FROM FatalitiesCountryDB as c
                    LEFT JOIN FatalitiesYearDB as y on c.iyear=y.iyear
                    GROUP BY c.iyear
                    ORDER BY UK_prop_of_tot_fatalities 
                  """)
        rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    return "Success"
    