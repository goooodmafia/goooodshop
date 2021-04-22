from enum import Enum

import graphene


class OrderEnum(Enum):
    Random = 'random'
    Order = 'order'
    PriceInc = 'price_inc'
    PriceDec = 'price_dec'
    Sale = 'sale'


GrapheneOrderEnum = graphene.Enum.from_enum(OrderEnum)
