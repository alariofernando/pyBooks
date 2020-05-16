import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    with open("books.csv", "r") as csvfile:
        readCSV = csv.reader(csvfile)
        for isbn, title, author, year in readCSV:
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn":isbn, "title":title, "author":author, "year":int(year)})
            print(f"Added book {title} into table ")
        db.commit()


if __name__ == "__main__":
    main()