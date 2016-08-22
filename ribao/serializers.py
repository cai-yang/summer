from rest_framework import serializers
from ribao.models import Article, Daily
from django.contrib.auth.models import User

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Article
        fields = ('url','daily','raw_url','title','date_add','comment')

class DailySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Daily
        fields = ('url','date_add','status')



#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    patient = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='patient-detail')
#    test = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='dateandvalue-detail')
#    class Meta:
#        model = User
#        fields = ('url','username','patient','test')
