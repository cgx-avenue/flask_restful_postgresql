from flask_restful import Resource
from resources.todoitem import todoitem_blue


class TodoItem(Resource):
    @todoitem_blue.route('/<int:id>')
    def get(id):
        return {'task': 'say hello falsk_restful'}

    @todoitem_blue.route('/all')
    def getall():
        return {'task1': 'say hello falsk_restful', 'task2': 'say hello falsk_restful', 'task3': 'say hello falsk_restful'}
