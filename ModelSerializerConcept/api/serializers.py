from rest_framework import serializers
from .models import Student


#Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    #if we want to apply any properties or validation on the fields then we have to define it explicitekly
     #the the name fields will not change but roll and city can change
    name=serializers.CharField(read_only=True)
    class Meta:
        model=Student
        fields=['id','name','roll','city']
        # read_only_fields=['id','name'] #id and name are read only fields

        

























#Normal serializer
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city=serializers.CharField(max_length=100)



    #creating data into api
    # def create(self,validated_data):
    #     return Student.objects.create(**validated_data)

    # #update data 
    # def update(self,instance,validated_data):
    #     print(instance.name)#old data
    #     instance.name=validated_data.get('name',instance.name)
    #     print(instance.name)#new data or updated data
    #     instance.roll=validated_data.get('roll',instance.roll)
    #     instance.city=validated_data.get('city',instance.city)
    #     instance.save()
    #     return instance
    
