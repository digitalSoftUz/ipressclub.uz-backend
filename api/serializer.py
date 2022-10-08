from rest_framework import serializers
from main.models import *


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class JamoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jamoa
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = News
        fields = "__all__"


class ProjectsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Projects
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = "__all__"


class AboutXPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutXPK
        fields = "__all__"


class CategoryProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProjects
        fields = "__all__"


class StreamingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streaming
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = "__all__"


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = "__all__"
