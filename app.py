from flask import Flask, render_template , request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


app = Flask(__name__, static_url_path='',
            static_folder="../demo/dist",
            template_folder="../demo/dist")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

class Colors(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    color1 :Mapped[str] = mapped_column(String)
    color2 :Mapped[str] = mapped_column(String)
    color3 :Mapped[str] = mapped_column(String)
    color4 :Mapped[str] = mapped_column(String)
    color5 :Mapped[str] = mapped_column(String)

# Enable CORS
CORS(app)

@app.route("/")
def render_spa():
    return render_template("index.html")

@app.get("/palette")
def get_palette():
    colors = Colors.query.get(1)
    return [colors.color1,colors.color2,colors.color3,colors.color4,colors.color5]

@app.put("/palette")
def update_palette():
    palette = Colors.query.get(1)
    body = request.get_json()
    colors = body.get("colors")
    for idx,hex in enumerate(colors):
        setattr(palette,f"color{idx+1}",hex)
    db.session.commit()
    return body
if __name__ == "__main__":
    app.run(debug=True)