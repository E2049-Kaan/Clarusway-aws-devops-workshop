from flask import Flask, render_template, request

app = Flask(__name__)

def convert(entry):
    def to_second(i, j):
        nonlocal sonuc, z
        a = z // i
        b = z % i
        if a == 0:
            sonuc += ""
            z = b
        else:
            sonuc += str(a) + j
            z -= a*i
    sonuc = ""
    sayi = {3600000 : " hour/s ", 60000 : " minute/s ", 1000 : " second/s "}
    if int(entry) < 1000:
        sonuc = "just " + entry + " millisecond/s "
    else:
        z = int(entry)
        for i in sayi:
            to_second(i, sayi[i])
    return sonuc

@app.route("/", methods=["GET"])
def main_get():
    return render_template("index.html", developer_name="Walt Harris", not_valid=False)

@app.route("/", methods=["POST"])
def main_post():
    alpha = request.form["number"]
    if not alpha.isdecimal():
        return render_template("index.html", developer_name = "Walt Harris", not_valid = True)
    number = int(alpha)
    if number < 1:
        return render_template("index.html", developer_name = "Walt Harris", not_valid = True)

    return render_template("result.html", milliseconds = number, result = convert(number), developer_name = "Walt Harris")


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host = "0.0.0.0", port=80)