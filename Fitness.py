#App that will aim to track fitness using SQLite - first time using SQLite although I have used pymysql. This is cool as it is a local db.
#Specifically: I want to create tables to track food intake/calories and exercises that will have a time input
#potentally try to calculate calories burned
#This will all be outputted to a daily summary
#Personal note - use program if you ever need to log something calorie/exercise related this so you dont waste paper
import sqlite3
from datetime import date

DB_NAME = "fitness.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = get_connection()
    cur = conn.cursor()
    #setup tables for food and exercises to store data 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS food (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                log_date VARCHAR(10) not null,
                name VARCHAR(75) not null,
                calories INTEGER not null
                )
            """)
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                log_date VARCHAR(10) not null,
                name VARCHAR(50) not null,
                minutes INTEGER,
                calories_burned INTEGER
                )
            """)
    conn.commit()
    conn.close()

#apparently in programming there is a popular standardized format for dates: year-month-date

def add_cals():
    name = input("Meal description: ")
    calories = int(input("Total calories:"))
    today = date.today()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO food (log_date, name, calories) VALUES (?, ?, ?)"
        (today, name, calories)
    )

    conn.commit()
    conn.close()
    print("Food and calories tracked for this meal")

def add_exercises():
    name = input("Exercise name: ")
    minutes = int(input("Please enter durration in minutes of exercise: "))
    calories_burned = int(input("Please enter estimated calorie burn"))
    today = date.today()

    conn = get_connection()
    cur = conn.cursor()
#remember to use ? instead of %s
    cur.execute(
        "INSERT INTO exercises (log_date, name, minutes, calories_burner) VALUES (?, ?, ?, ?)"
        (today, name, minutes, calories_burned)
    )

    conn.commit()
    conn.close()
    print("Exercise has been added")

def summary():
    today = date.today()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT SUM(calories) FROM food WHERE log_date = ?", 
        (today,)
    )
    calorie_intake = cur.fetchone()[0]
    if calorie_intake is None:
        calorie_intake = 0

#covered edge case of 0 calories inputed, and properly indexed fetchone as it is slecting just the sum from the day logged
    
    cur.execute(
        "SELECT SUM(calories_burned) FROM exercise WHERE log_date = ?",
        (today,)
    )

    calories_burnt = cur.fetchone()[0]
    if calories_burnt is None:
        calories_burnt = 0
    
    conn.close()

    net_calories = calorie_intake - calories_burnt

    print("Daily intake summary")
    print("**********************************")
    print(f"Calorie intake: {calorie_intake}")
    print(f"Net calories after exercise: {net_calories}")

def main():
    pass