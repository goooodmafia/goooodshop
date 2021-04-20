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
    # register = mutations.Register.Field()
    # send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    # password_reset = mutations.PasswordReset.Field()
    #
    # token_auth = mutations.ObtainJSONWebToken.Field()
    # verify_token = mutations.VerifyToken.Field()
    # refresh_token = mutations.RefreshToken.Field()

    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field()  # For passwordless registration
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Mutations(AuthMutation, graphene.ObjectType):
    pass


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    @permissions_checker([IsAuthenticated])
    def resolve_users(self, info):
        print(info.context.user)
        return get_user_model().objects.all()
