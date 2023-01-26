# coding:utf-8

import flask
import references as r

app = flask.Flask(__name__)

# common_html = "http://127.0.0.1:5000"
common_html = "https://nomuras.github.io"


@app.route("/")
def index():
    return flask.render_template("index.html", title="")


@app.route("/pages/")
def about():
    return flask.render_template("/pages/about.html", title="about")


# @app.route('/pages/<page_num>.html', methods=['GET'])
# def trans_page(page_num):
#     return flask.render_template(
#         '/pages/'+page_num+'.html',
#         page_num=page_num,
#         )


# ancient
@app.route("/pages/ancient/<page_num>.html", methods=["GET"])
def trans_ancient(page_num):
    return flask.render_template(
        "/pages/ancient/%s.html" % page_num,
        title="古代哲学",
        prev_page=common_html + "/pages/ancient/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/ancient/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# medieval
@app.route("/pages/medieval/<page_num>.html", methods=["GET"])
def trans_medieval(page_num):
    return flask.render_template(
        "/pages/medieval/%s.html" % page_num,
        title="中世哲学",
        prev_page=common_html + "/pages/medieval/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/medieval/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# modern
@app.route("/pages/modern/<page_num>.html", methods=["GET"])
def trans_modern(page_num):
    return flask.render_template(
        "/pages/modern/" + page_num + ".html",
        title="近代哲学",
        prev_page=common_html + "/pages/modern/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/modern/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# contemporary
@app.route("/pages/contemporary/<page_num>.html", methods=["GET"])
def trans_contemporary(page_num):
    return flask.render_template(
        "/pages/contemporary/" + page_num + ".html",
        title="現代哲学",
        prev_page=common_html + "/pages/contemporary/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/contemporary/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# phenomenology
@app.route("/pages/phenomenology/<page_num>.html", methods=["GET"])
def trans_phenomenology(page_num):
    return flask.render_template(
        "/pages/phenomenology/" + page_num + ".html",
        title="現象学",
        prev_page=common_html + "/pages/phenomenology/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/phenomenology/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# # existential
# @app.route('/pages/existential/<page_num>.html', methods=['GET'])
# def trans_existential(page_num):
#     return flask.render_template(
#         '/pages/existential/'+page_num+'.html',
#         title= '実存主義',
#         prev_page= common_html + "/pages/existential/%s.html" % (int(page_num)-1),
#         next_page= common_html + "/pages/existential/%s.html" % (int(page_num)+1),
#         reference=r.REFERENCE,
#         )

# fr
@app.route("/pages/fr/<page_num>.html", methods=["GET"])
def trans_fr(page_num):
    return flask.render_template(
        "/pages/fr/" + page_num + ".html",
        title="現代フランス哲学",
        prev_page=common_html + "/pages/fr/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/fr/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# en
@app.route("/pages/en/<page_num>.html", methods=["GET"])
def trans_en(page_num):
    return flask.render_template(
        "/pages/en/" + page_num + ".html",
        title="現代イギリス哲学",
        prev_page=common_html + "/pages/en/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/en/%s.html" % (int(page_num) + 1),
        last_page=common_html + "/pages/en/14.html",
        reference=r.REFERENCE,
    )


# us
@app.route("/pages/us/<page_num>.html", methods=["GET"])
def trans_us(page_num):
    return flask.render_template(
        "/pages/us/" + page_num + ".html",
        page_num=page_num,
        title="現代アメリカ哲学",
        prev_page=common_html + "/pages/us/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/us/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# lang
@app.route("/pages/lang/<page_num>.html", methods=["GET"])
def trans_lang(page_num):
    return flask.render_template(
        "/pages/lang/" + page_num + ".html",
        page_num=page_num,
        title="言語哲学",
        prev_page=common_html + "/pages/lang/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/lang/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# science
@app.route("/pages/science/<page_num>.html", methods=["GET"])
def trans_science(page_num):
    return flask.render_template(
        "/pages/science/" + page_num + ".html",
        title="科学哲学",
        prev_page=common_html + "/pages/science/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/science/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# mind
@app.route("/pages/mind/<page_num>.html", methods=["GET"])
def trans_mind(page_num):
    return flask.render_template(
        "/pages/mind/" + page_num + ".html",
        title="心の哲学",
        prev_page=common_html + "/pages/mind/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/mind/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# epist
@app.route("/pages/epistemology/<page_num>.html", methods=["GET"])
def trans_epistemology(page_num):
    return flask.render_template(
        "/pages/epistemology/" + page_num + ".html",
        title="認識論",
        prev_page=common_html + "/pages/epistemology/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/epistemology/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# logic
@app.route("/pages/logic/<page_num>.html", methods=["GET"])
def trans_logic(page_num):
    return flask.render_template(
        "/pages/logic/" + page_num + ".html",
        title="論理学",
        prev_page=common_html + "/logic/medieval/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/logic/medieval/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# east
@app.route("/pages/east/<page_num>.html", methods=["GET"])
def trans_east(page_num):
    return flask.render_template(
        "/pages/east/%s.html" % page_num,
        title="東洋哲学",
        prev_page=common_html + "/pages/east/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/east/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# others
@app.route("/pages/others/<page_num>.html", methods=["GET"])
def trans_others(page_num):
    return flask.render_template(
        "/pages/others/" + page_num + ".html",
        title="others",
        prev_page=common_html + "/pages/others/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/pages/others/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


if __name__ == "__main__":
    app.run(debug=True)
