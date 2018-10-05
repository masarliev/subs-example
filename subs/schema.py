import graphene
from graphene_django.debug import DjangoDebug
from .subscriptions import UserSubscription


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


class Subscriptions(graphene.ObjectType):
    user_subscription = UserSubscription.Field()


schema = graphene.Schema(
    query=Query,
    subscription=Subscriptions
)
