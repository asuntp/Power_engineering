from flask import Blueprint, render_template
from webapp.news.models import News

blueprint = Blueprint('news', __name__)


@blueprint.route("/")
def index():
    news_list = News.query.all()
    return render_template("news/index.html", news_list=news_list)
