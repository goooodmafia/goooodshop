from enum import Enum

import graphene


class OrderEnum(Enum):
    Random = 'random'
    OrderInc = 'order_inc'
    OrderDec = 'order_dec'
    PriceInc = 'price_inc'
    PriceDec = 'price_dec'
    SaleInc = 'sale_inc'
    SaleDec = 'sale_dec'
    HitInc = 'hit_inc'
    HitDec = 'hit_dec'


GrapheneOrderEnum = graphene.Enum.from_enum(OrderEnum)
