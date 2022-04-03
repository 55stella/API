from rest_framework  import serializers
from Accounts.models import CustomUser

class Signupserializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username","email","password", 'password', 're_password']
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField(max_length=300)      
