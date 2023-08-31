from users.models import User
from elasticsearch import Elasticsearch
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from django.conf import settings


es = Elasticsearch(hosts=settings.ELASTICSEARCH_DSL['default']['hosts'])
es.indices.put_template(name='default', body={
    "index_patterns": ["user"],
    "settings": {
        "index": {
            "number_of_replicas": 0
        }
    }
})

@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'user'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = User
         fields = [
             'id',
             'username',
             'first_name',
             'last_name',
             'about',
             'email',
             'date_joined',
             'phone_number',
         ]