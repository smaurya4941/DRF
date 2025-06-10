from rest_framework import serializers
from .models import Student

#Validators
def start_with_s(value):
    if value[0].lower() !='s':
        raise serializers.ValidationError("Name should start with 'S'")
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[start_with_s])
    roll = serializers.IntegerField()
    city=serializers.CharField(max_length=100)



    #creating data into api
    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    #update data 
    def update(self,instance,validated_data):
        print(instance.name)#old data
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)#new data or updated data
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    

    # FIeld level validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Roll number should be less than 200")
        return value


    # #object level validation
    # def validate(self,value):
    #     print(value)
    #     name=value.get('name')
    #     roll=value.get('roll')
    #     city=value.get('city')
    #     if name is  None or city is  None:
    #         raise serializers.ValidationError("Both 'roll' and 'city' are required.")
    #     if name=="Sachin" and city!="Lucknow":
    #         raise serializers.ValidationError("City should be Lucknow")
    #     return value
