from rest_framework import serializers
from .models import (
    ContactForm,
    JoinUsForm,
    Building,
    ContractRequestForm,
    BuildingImage,
)


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"


class ContractRequestFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractRequestForm
        fields = "__all__"


class JoinUsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinUsForm
        fields = "__all__"


class BuildingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingImage
        fields = ("image",)


class BuildingSerializer(serializers.ModelSerializer):
    images = BuildingImageSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
    )

    class Meta:
        model = Building
        fields = "__all__"
        read_only_fields = ("user",)

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        building = super().create(validated_data)

        for image in uploaded_images:
            image = BuildingImage(building=building, image=image)
            image.save()
            building.images.add(image)

        return building
