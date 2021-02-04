import graphene
from graphene_django import DjangoObjectType
from .models import Content
from .models import CONTENT_POSITIONS

from graphene_django_optimizer.types import OptimizedDjangoObjectType
from django_parler_graphql.fields import TranslatedInstanceFields


def resolver(instance, _info, language_code):
    return instance.safe_translation_getter("data", language_code=language_code)


PositionEnum = graphene.Enum(
    "Position",
    [(pos[0],pos[0]) for pos in CONTENT_POSITIONS]
    # [(lang[0].replace("-", "_").upper(), lang[0]) for lang in CONTENT_POSITIONS],
    # [('NEWHOPE', 4), ('EMPIRE', 5), ('JEDI', 6)]
)


class ContentType(DjangoObjectType):


    data = TranslatedInstanceFields(graphene.String, resolver=resolver)

    class Meta:
        model = Content
