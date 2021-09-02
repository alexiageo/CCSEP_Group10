from flask import Flask, render_template,url_for

app= Flask(__name__)

posts = [
    {
        'Group_10_topic': 'Web Cache Poisoning',
        'date_posted': '02 Sep 2021'
    }

]
@app.route("/")
def homePage():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return "<h1>This is the about page</h1>"


if __name__=='__main__':
    app.run(debug=True)

