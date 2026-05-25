import graphene
from graphene_django import DjangoObjectType
from food.models import FoodItem
from meal.models import MealLog

class FoodItemType(DjangoObjectType):
    class Meta:
        model = FoodItem

class MealLogType(DjangoObjectType):
    class Meta:
        model = MealLog

class Query(graphene.ObjectType):
    all_food_items = graphene.List(FoodItemType)
    all_meal_logs = graphene.List(MealLogType)

    def resolve_all_food_items(root, info):
        user = info.context.user
        return FoodItem.objects.filter(image__user=user)

    def resolve_all_meal_logs(root, info):
        user = info.context.user
        return MealLog.objects.filter(user=user)

schema = graphene.Schema(query=Query)