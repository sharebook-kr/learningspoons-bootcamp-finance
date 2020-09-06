
import sqlite3

con = sqlite3.connect('project.db')
cur = con.cursor()

query = "select ticker.ticker, ticker.name, fundamental.per from fundamental left join ticker on ticker.ticker = fundamental.ticker order by per ASC limit 5"
cur.execute(query)

for item in cur:
    print(item)

con.commit()
con.close()