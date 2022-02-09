from flask import Blueprint

todoitem_blue=Blueprint('todoitem',__name__,url_prefix='/todos')
from . import views