from flask import Flask
import dbhelpers
import json

app = Flask(__name__)

@app.get("/api/books")
def get_books():
    results = dbhelpers.run_procedure("call all_info", [])
    results_json = json.dumps(results, default=str)
    return results_json

@app.get("/api/books_authored")
def get_books_authored():
    results = dbhelpers.run_procedure("call books_written", [])
    results_json = json.dumps(results, default=str)
    return results_json

@app.get("/api/best_selling_book")
def get_best_selling_book():
    results = dbhelpers.run_procedure("call popular_book", [])
    results_json = json.dumps(results, default=str)
    return results_json

@app.get("/api/best_selling_author")
def get_best_selling_author():
    results = dbhelpers.run_procedure("call popular_authors", [])
    results_json = json.dumps(results, default=str)
    return results_json

app.run(debug=True)