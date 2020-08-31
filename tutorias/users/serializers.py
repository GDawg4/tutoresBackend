from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'lastname',
            'email',
            'password',
            'type'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        print(self.data)
        user = User(email=self.validated_data['email'],
                        name=self.validated_data['name'],
                        lastname=self.validated_data['lastname'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
