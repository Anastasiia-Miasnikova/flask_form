from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

# Create a Flask Instance
app = Flask(__name__)
# app.config['SECRET_KEY'] = "my super secret key that no one is suppoused to know"
#
# # Create a Form Class
# class NamerForm(FlaskForm):
#     name = StringField("What's Your Name", validators=[DataRequired()])
#     submit = SubmitField("Submit")


# Create a route decorator
@app.route('/')
def index():
    first_name = "John"
    stuff = "This is bold text"

    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)
# localhost:5000/user/John


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


#     return render_template("user.html", )

# FILTERS!!! - пишуться в {{ з розділювачем | }}
# safe - дозволяє використовувати теги в Python файлі
# capitalize - перша літера велика
# lower - всі маленькі літери
# upper - всі великі літери
# title - всі слова з великої літери
# trim
# striptags - прибирає теги і відображає тільки текст в Python файлі

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run()
