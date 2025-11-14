
        title = request.form.get("postTitle")
        text = request.form.get("postArticle")

        article = title + " " + text
        pred = model.predict([article])
        estimation = str(pred[0])

    return render_template("index.html", estimation=estimation)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
