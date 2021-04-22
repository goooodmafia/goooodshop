
from parler.managers import TranslatableManager, TranslatableQuerySet
from mptt.managers import TreeManager
from mptt.querysets import TreeQuerySet


# from django_random_queryset.queryset import RandomQuerySet
# from django_random_queryset import RandomManager


class CategoryQuerySet(TranslatableQuerySet, TreeQuerySet):

    def as_manager(cls):
        # make sure creating managers from querysets works.
        manager = CategoryManager.from_queryset(cls)()
        manager._built_with_as_manager = True
        return manager
    as_manager.queryset_only = True
    as_manager = classmethod(as_manager)


class CategoryManager(TreeManager, TranslatableManager):
    _queryset_class = CategoryQuerySet

# class ProductQuerySet(TranslatableQuerySet, RandomQuerySet):
#     def as_manager(cls):
#         # make sure creating managers from querysets works.
#         manager = ProductManager.from_queryset(cls)()
#         manager._built_with_as_manager = True
#         return manager
#     as_manager.queryset_only = True
#     as_manager = classmethod(as_manager)
#
# class ProductManager(RandomManager, TranslatableManager):
#     # _queryset_class = ProductQuerySet
#     pass