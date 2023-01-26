from flask_frozen import Freezer
from main import app
import shutil
import os

freezer = Freezer(app)

app.config["FREEZER_RELATIVE_URLS"] = True

if __name__ == "__main__":
    freezer.freeze()
    shutil.rmtree("./docs/")
    os.rename("./build", "./docs")
