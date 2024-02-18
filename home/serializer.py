from rest_framework import serializers
from home.models import Person, Team

class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Team
        fields = ['team_name']


class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Person
        fields = '__all__'
        depth = 1
        
    def get_team_info(self, obj):
        return "extra field" 
    
    def validate(self, data):
        spl_char = "!@#$%^&*()_+-=<>?/"
        
        if any(c in spl_char for c in data['name']):
            raise serializers.ValidationError("Name should not have special characters")
        
        if data['age'] < 18:
            raise serializers.ValidationError("Age should not be less than 18")
        return data