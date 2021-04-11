import graphene
from graphene_django import DjangoObjectType

from django.contrib.auth import get_user_model

from graphql_auth import mutations

from django_graphene_permissions import permissions_checker
from django_graphene_permissions.permissions import IsAuthenticated


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()


class Mutations(AuthMutation, graphene.ObjectType):
    pass


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    @permissions_checker([IsAuthenticated])
    def resolve_users(self, info):
        print(info.context.user)
        return get_user_model().objects.all()
