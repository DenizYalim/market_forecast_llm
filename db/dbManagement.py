import sqlite3
from datetime import datetime


def pre_req():
    conn = sqlite3.connect("headlines.db")  # id, headline, text, date, website
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS headlines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            headline TEXT NOT NULL,
            text TEXT,
            date DATE NOT NULL,
            source TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn, cursor


def add_headlines_to_db(date, headlines, site_name, text=""):
    conn, cursor = pre_req()

    for headline in headlines:
        cursor.execute(
            """
            INSERT INTO headlines (headline, text, date, source)
            VALUES (?, ?, ?, ?)
            """,
            (headline, text, date, site_name),
        )

    conn.commit()
    conn.close()


""" returns all headlines for a specific date or site

Keyword arguments:
date : DATE
website : String

Return: String[]
"""
def get_headlines(date, website=None):
    conn, cursor = pre_req()

    if website:
        statement = "SELECT headline FROM headlines WHERE date = ? AND source = ?"
        cursor.execute(statement, (date, website))
    else:
        statement = "SELECT headline FROM headlines WHERE date = ?"
        cursor.execute(statement, (date,))
    
    headlines = cursor.fetchall()
    conn.close()

    headlines = [row[0] for row in headlines] # Turns the weird [(headline,),(headline,)] to [headline]

    return headlines
