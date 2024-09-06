from marketplaces.models import Marketplace
from products.models import Product  # TODO: import other classes in the models.py file
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = [
            "url",
            "name",
            "opening_hours",
            "location",
            "size",
            "province",
            "canton",
            "district",
            "postal_code",
            "address",
            "phone",
            "email",
            "website",
            "facebook",
            "instagram",
            "opening_date",
            "operator",
            "branch",
            "marketplace_type",
            "parking",
            "bicycle_parking",
            "fairground",
            "indoor",
            "toilets",
            "handwashing",
            "drinking_water",
            "food",
            "drinks",
            "handicrafts",
            "butcher",
            "dairy",
            "seafood",
            "spices",
            "garden_centre",
            "florist",
            "other_services",
        ]


class GeoMarketplaceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Marketplace
        geo_field = "location"
        fields = (
            "name",
            "province",
            "canton",
            "district",
            "postal_code",
            "address",
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "product_url",
            "category",
            "common_name",
            "common_name_alternate",
            "description",
            "icon",
            "name_origin",
            "center_origin",
            "center_origin_notes",
            "food_basket",
            "nutrition_notes",
            "preparation",
            "preparation_notes",
            "storage",
            "storage_notes",
        ]
