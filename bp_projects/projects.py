from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

@app_projects.route('/AMZN/')
def AMZN():
    return render_template("AMZN.html")

@app_projects.route('/TSLA/')
def TSLA():
    return render_template("TSLA.html")

@app_projects.route('/portfoli0/')
def portfoli0():
    return render_template("portfoli0.html")

@app_projects.route('/game/')
def game():
    return render_template("game.html")

@app_projects.route('/rec/')
def rec():
    return render_template("rec.html")

@app_projects.route('/gamee/')
def gamee():
    return render_template("gamee.html")

@app_projects.route('/StockInformation/')
def StockInformation():
    return render_template("StockInformation.html")