from flask import Flask, render_template, request
import absa_model

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def hello():

    if request.method == "POST":
        review_text = request.form["review"]
        sentiment_data = absa_model.review_absa(review_text)
        print(sentiment_data)

        return render_template("index.html", data = sentiment_data)
    
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
    

    