import mysql.connector

homedb = mysql.connector.connect(
    host = '',
    user = '',
    password = '',
    database = 'fitness'
)

cursor = homedb.cursor()

# prints the requested table
def printtable(table: str):
    cursor.execute("SELECT * FROM " + table)

    results = cursor.fetchall()

    for x in results:
        print(x)

# gets all fitness information for a specific person
def getfitnessreport(person: str):
    requested = 0

    if ("Jack" in person):
        requested = 1
    elif ("Connor" in person):
        requested = 2
    elif ("Richard" in person):
        requested = 3

    sql = "SELECT * FROM People \
        LEFT JOIN Fitness on People.PID = Fitness.PID \
        LEFT JOIN Vitals on People.PID = Vitals.PID \
        WHERE PID == " + requested

    cursor.execute(sql)

    results = cursor.fetchall()
    for x in results:
        print(x)