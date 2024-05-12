from flask import Flask, render_template, request, redirect, url_for
import pyshorteners

app = Flask(__name__)
# This dictionary will store mappings between short URLs and their corresponding long URLs
shortener = pyshorteners.Shortener()


@app.route("/")
def home():
    return render_template("web.html")


@app.route('/', methods=['GET', 'POST'])
def shorten():
    if request.method == 'POST':
        print("Form submitted successfully!")
        url = request.form['url']
        shortened_url = shortener.tinyurl.short(url)
        return render_template('web.html', original_url=url, shortened_url=shortened_url)
    return render_template('web.html')


if __name__ == "__main__":
    app.run(debug=True)
