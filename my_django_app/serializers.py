from math import ceil
from rest_framework import serializers

from .models import Product, Lesson

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["id", "title", "link", "product"]
        read_only = fields


class ProductSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Product
        fields = ["id", "author", "title", "date_start", "price", "lessons_count", "lessons"]
        read_only = fields

    def get_lessons_count(self, product):
        return product.lessons.count()

    def get_fields(self):
        fields = super().get_fields()
        user = self.context["request"].user
        if getattr(self.instance, "id", None) and user.is_authenticated:
            if self.instance.users.filter(id=user.id).exists():
                fields.pop("lessons_count")
                return fields
        fields.pop("lessons")
        return fields

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if not instance.users.filter(id=user.id).exists():
            instance.users.add(user)
            instance.study_groups.all().delete()
            groups = self.distribute_groups(instance)
            for title, users in self.get_data_groups(groups).items():
                for user in users:
                    instance.study_groups.create(title=title, user=user)
        return instance

    def distribute_groups(self, instance):
        users = instance.users
        min_quantity = instance.quantity.min_quantity
        max_quantity = instance.quantity.max_quantity
        groups_count = ceil(users.count() / max_quantity)
        groups = [[] for _ in range(groups_count)]
        for user in users.all():
            min_len_group = min(groups, key=len)
            if len(min_len_group) < min_quantity:
                min_len_group.append(user)
            elif len(min_len_group) <= max_quantity:
                min_len_group.append(user)
            else:
                groups.append([user])
        return groups

    def get_data_groups(self, groups):
        data_groups = {}
        for i, st_group in enumerate(groups, 1):
            title = f"Группа {i}"
            data_groups[title] = st_group
        return data_groups








