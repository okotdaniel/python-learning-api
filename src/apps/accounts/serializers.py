from rest_framework import serializers

class TestSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    is_deputy_head_teacher = serializers.BooleanField(required=False, write_only=True)
    is_head_teacher = serializers.BooleanField(required=False, write_only=True)
    is_deputy_principal = serializers.BooleanField(required=False, write_only=True)
    is_principal = serializers.BooleanField(required=False, write_only=True)
    is_director = serializers.BooleanField(required=False, write_only=True)
    is_dos = serializers.BooleanField(required=False, write_only=True)

    # def __init__(self, *args, **kwargs):
    #     super(RegisterSerializer, self).__init__(*args, **kwargs)

    #     if 'email' in self.initial_data:
    #         self.initial_data['username'] = self.initial_data['email']

    # class Meta:
    #     model = Account
    #     fields = ['id', 'email', 'username', 'first_name', 'last_name', 'nin', 'phone_number', 'address', 'image_url', 'date_of_birth', 'gender',
    #               'school', 'is_staff', 'is_school_staff', 'is_verified', 'is_parent', 'is_teacher', 'is_school_admin', 'is_finance', 'is_proprietor',
    #               'is_dean', 'is_principle', 'identification_type', 'passport_number', 'marital_status', 'spouse_name', 'spouse_phone_number',
    #               'highest_level_of_education', 'is_head_teacher', 'is_deputy_head_teacher', 'is_principal', 'next_of_kin', 'nok_contact', 'nok_relationship',
    #               'emergency_contact_name', 'emergency_contact', 'emergency_relationship', 'other_role',
    #               'is_deputy_principal', 'is_director', 'is_dos', 'is_nurse', 'is_security', 'is_warden', 'is_matron', 'is_other',
    #               'password', 'password2']
    #     extra_kwargs = {
    #         'password': {'write_only': True}
    #     }

    # def create(self, validated_data):
    #     validated_data.pop('password2', None)
    #     password = validated_data.pop('password', None)
    #     validated_data.pop('is_deputy_head_teacher', None)
    #     validated_data.pop('is_head_teacher', None)
    #     validated_data.pop('is_deputy_principal', None)
    #     validated_data.pop('is_principal', None)
    #     validated_data.pop('is_director', None)
    #     validated_data.pop('is_dos', None)
    #     account = self.Meta.model(**validated_data)
    #     if password is not None:
    #         account.set_password(password)

    #     try:
    #         account.save()
    #     except IntegrityError as e:
    #         raise serializers.ValidationError({'error': e.args})
    #     return account

    # def validate(self, attrs):
    #     password = attrs['password']
    #     password2 = attrs['password2']

    #     if password != password2:
    #         raise serializers.ValidationError({'password': 'Passwords must match.'})
    #     return attrs