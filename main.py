# coding:utf-8

import flask
import references as r

app = flask.Flask(__name__)

# common_html = "http://127.0.0.1:5000"
common_html = "https://nomuras.github.io"


@app.route("/")
def index():
    return flask.render_template("index.html", title="")


@app.route("/")
def about():
    return flask.render_template("/about.html", title="about")


# @app.route('/<page_num>.html', methods=['GET'])
# def trans_page(page_num):
#     return flask.render_template(
#         '/'+page_num+'.html',
#         page_num=page_num,
#         )


# ancient
@app.route("/ancient/<page_num>.html", methods=["GET"])
def trans_ancient(page_num):
    return flask.render_template(
        "/ancient/%s.html" % page_num,
        title="古代哲学",
        prev_page=common_html + "/ancient/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/ancient/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# medieval
@app.route("/medieval/<page_num>.html", methods=["GET"])
def trans_medieval(page_num):
    return flask.render_template(
        "/medieval/%s.html" % page_num,
        title="中世哲学",
        prev_page=common_html + "/medieval/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/medieval/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# modern
@app.route("/modern/<page_num>.html", methods=["GET"])
def trans_modern(page_num):
    return flask.render_template(
        "/modern/" + page_num + ".html",
        title="近代哲学",
        prev_page=common_html + "/modern/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/modern/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# contemporary
@app.route("/contemporary/<page_num>.html", methods=["GET"])
def trans_contemporary(page_num):
    return flask.render_template(
        "/contemporary/" + page_num + ".html",
        title="現代哲学",
        prev_page=common_html + "/contemporary/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/contemporary/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# phenomenology
@app.route("/phenomenology/<page_num>.html", methods=["GET"])
def trans_phenomenology(page_num):
    return flask.render_template(
        "/phenomenology/" + page_num + ".html",
        title="現象学",
        prev_page=common_html + "/phenomenology/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/phenomenology/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# # existential
# @app.route('/existential/<page_num>.html', methods=['GET'])
# def trans_existential(page_num):
#     return flask.render_template(
#         '/existential/'+page_num+'.html',
#         title= '実存主義',
#         prev_page= common_html + "/existential/%s.html" % (int(page_num)-1),
#         next_page= common_html + "/existential/%s.html" % (int(page_num)+1),
#         reference=r.REFERENCE,
#         )

# fr
@app.route("/fr/<page_num>.html", methods=["GET"])
def trans_fr(page_num):
    return flask.render_template(
        "/fr/" + page_num + ".html",
        title="現代フランス哲学",
        prev_page=common_html + "/fr/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/fr/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# en
@app.route("/en/<page_num>.html", methods=["GET"])
def trans_en(page_num):
    return flask.render_template(
        "/en/" + page_num + ".html",
        title="現代イギリス哲学",
        prev_page=common_html + "/en/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/en/%s.html" % (int(page_num) + 1),
        last_page=common_html + "/en/14.html",
        reference=r.REFERENCE,
    )


# us
@app.route("/us/<page_num>.html", methods=["GET"])
def trans_us(page_num):
    return flask.render_template(
        "/us/" + page_num + ".html",
        page_num=page_num,
        title="現代アメリカ哲学",
        prev_page=common_html + "/us/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/us/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# lang
@app.route("/lang/<page_num>.html", methods=["GET"])
def trans_lang(page_num):
    return flask.render_template(
        "/lang/" + page_num + ".html",
        page_num=page_num,
        title="言語哲学",
        prev_page=common_html + "/lang/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/lang/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# science
@app.route("/science/<page_num>.html", methods=["GET"])
def trans_science(page_num):
    return flask.render_template(
        "/science/" + page_num + ".html",
        title="科学哲学",
        prev_page=common_html + "/science/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/science/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# mind
@app.route("/mind/<page_num>.html", methods=["GET"])
def trans_mind(page_num):
    return flask.render_template(
        "/mind/" + page_num + ".html",
        title="心の哲学",
        prev_page=common_html + "/mind/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/mind/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# epist
@app.route("/epistemology/<page_num>.html", methods=["GET"])
def trans_epistemology(page_num):
    return flask.render_template(
        "/epistemology/" + page_num + ".html",
        title="認識論",
        prev_page=common_html + "/epistemology/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/epistemology/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# logic
# @app.route ("/logic/<page_num>.html", methods=["GET"])
# def trans_logic(page_num):
#     return flask.render_template(
#         "/logic/" + page_num + ".html",
#         title="論理学",
#         prev_page=common_html + "/logic/medieval/%s.html" % (int(page_num) - 1),
#         next_page=common_html + "/logic/medieval/%s.html" % (int(page_num) + 1),
#         reference=r.REFERENCE,
#     )


# east
@app.route("/east/<page_num>.html", methods=["GET"])
def trans_east(page_num):
    return flask.render_template(
        "/east/%s.html" % page_num,
        title="東洋哲学",
        prev_page=common_html + "/east/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/east/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


# others
@app.route("/others/<page_num>.html", methods=["GET"])
def trans_others(page_num):
    return flask.render_template(
        "/others/" + page_num + ".html",
        title="others",
        prev_page=common_html + "/others/%s.html" % (int(page_num) - 1),
        next_page=common_html + "/others/%s.html" % (int(page_num) + 1),
        reference=r.REFERENCE,
    )


if __name__ == "__main__":
    app.run(debug=True)
