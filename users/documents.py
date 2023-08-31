from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from users.models import User, UserConfirmation



@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = 'user'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = User
         fields = [
             'username',
             'first_name',
             'last_name',
             'about',
             'email',
             'date_joined',
             'phone_number',
         ]