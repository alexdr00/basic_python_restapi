from flask import Blueprint, request
from flask_restful import Resource, Api, fields, marshal, marshal_with

from common.utils import resource_or_not_found
import common.queries as query
from models import Post as PostModel

RESOURCE_NAME = 'post'

post_fields = {
    'title': fields.String,
    'description': fields.String,
    'tags': fields.List(fields.String)
}


class Post(Resource):
    def get(self, _id):
        post_found = query.find_by_id(PostModel, _id)

        return resource_or_not_found(RESOURCE_NAME, post_found, post_fields)

    def put(self, _id):
        data = request.get_json()
        post_updated = query.update_by_id(PostModel, _id, **data)

        return resource_or_not_found(RESOURCE_NAME, post_updated, post_fields)

    def delete(self, _id):
        post_deleted = query.delete_by_id(PostModel, _id)

        return resource_or_not_found(
            RESOURCE_NAME,
            post_deleted,
            post_fields,
            delete=True
        )


class PostList(Resource):
    def get(self):
        posts = [marshal(post, post_fields)
                 for post in PostModel.objects]

        return posts

    def post(self):
        data = request.get_json()
        post_created = query.create_resource(PostModel, **data)

        return marshal(post_created, post_fields), 201


posts_api = Blueprint('resources.posts', __name__)

api = Api(posts_api)

api.add_resource(
    Post,
    '/posts/<string:_id>',
    endpoint='post'
)

api.add_resource(
    PostList,
    '/posts/',
    endpoint='posts'
)
