import graphene
import datetime
from django_parler_graphql.fields import TranslatedInstanceFields
from graphene.types.generic import GenericScalar
from graphene_django_extras import DjangoObjectType

from news.models import News
from shop.translatable import myresolver


class NewsType(DjangoObjectType):
    description = TranslatedInstanceFields(graphene.String, resolver=myresolver)
    image = graphene.Field(graphene.String)
    view_date = graphene.Field(graphene.String)

    def resolve_image(self, info):
        if self.image:
            return self.image.link
        else:
            return ''

    def resolve_view_date(self, info):
        return self.view_date.strftime('%d/%m/%Y')

    class Meta:
        model = News
        # fields = {
        #     "model": ("icontains", "iexact"),
        #     "sku": ("icontains", "iexact"),
        # }
