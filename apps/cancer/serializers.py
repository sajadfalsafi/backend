from rest_framework import serializers

class CancerDataSerializer(serializers.Serializer):
    YES_NO_CHOICES = [
        (1, 'YES'),
        (2, 'NO')
    ]
    
    GENDER = serializers.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    AGE = serializers.IntegerField()
    SMOKING = serializers.ChoiceField(choices=YES_NO_CHOICES)
    YELLOW_FINGERS = serializers.ChoiceField(choices=YES_NO_CHOICES)
    ANXIETY = serializers.ChoiceField(choices=YES_NO_CHOICES)
    PEER_PRESSURE = serializers.ChoiceField(choices=YES_NO_CHOICES)
    CHRONIC_DISEASE = serializers.ChoiceField(choices=YES_NO_CHOICES)
    FATIGUE = serializers.ChoiceField(choices=YES_NO_CHOICES)
    ALLERGY = serializers.ChoiceField(choices=YES_NO_CHOICES)
    WHEEZING = serializers.ChoiceField(choices=YES_NO_CHOICES)
    ALCOHOL_CONSUMING = serializers.ChoiceField(choices=YES_NO_CHOICES)
    COUGHING = serializers.ChoiceField(choices=YES_NO_CHOICES)
    SHORTNESS_OF_BREATH = serializers.ChoiceField(choices=YES_NO_CHOICES)
    SWALLOWING_DIFFICULTY = serializers.ChoiceField(choices=YES_NO_CHOICES)
    CHEST_PAIN = serializers.ChoiceField(choices=YES_NO_CHOICES)

