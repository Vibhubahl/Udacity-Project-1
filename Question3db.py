import psycopg2

DBNAME = "news"


def get_posts():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view status as select date(time) as \
        date1, count(status) as stat from log group by date(time)")
    c.execute("create view status4 as select date(time) \
        as date1 , status from log where status like '404%'")
    c.execute("create view status2 as select date1 , \
        count(status) as notf from status4 group by date1")
    c.execute("create view status3 as select date1 , notf from status2")
    c.execute("create view status5 as select status3.date1 as fdate \
        ,cast(notf as float) , cast(stat as float) from status \
        join status3 on status.date1 = status3.date1")
    c.execute("select fdate , (notf*100)/stat from status5 \
        where (notf*100)/stat > 1")
    posts = c.fetchall()
    db.close()
    return posts
