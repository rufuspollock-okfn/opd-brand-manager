from haystack import indexes
from .models import Brand
import pytz
from datetime import datetime


class BrandIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    bsin = indexes.CharField(model_attr='bsin')
    brand_nm = indexes.CharField(model_attr='brand_nm')
    brand_link = indexes.CharField(model_attr='brand_link', default='')
    last_modified = indexes.DateTimeField(model_attr='last_modified')

    def get_model(self):
        return Brand

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(
            last_modified__lte=datetime.now(pytz.utc))
