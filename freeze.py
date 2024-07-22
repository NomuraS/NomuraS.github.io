import os
import shutil

from flask_frozen import Freezer

from app import app

freezer = Freezer(app)

app.config["FREEZER_RELATIVE_URLS"] = True

if __name__ == "__main__":
    freezer.freeze()
    try:
        shutil.rmtree("./docs/")
    except:
        print("no build file")
    os.rename("./build", "./docs")
