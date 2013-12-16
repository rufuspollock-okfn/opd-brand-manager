from django.contrib.admin import SimpleListFilter
from .models import BrandProposalReview


class ReviewedFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'reviewed'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'reviewed'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('reviewed', 'Reviewed'),
            ('not reviewed', 'Not reviewed'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or 'other')
        # to decide how to filter the queryset.
        reviewed_list = BrandProposalReview.objects\
            .filter(user=request.user).values_list('proposal_cd', flat=True)
        if self.value() == 'reviewed':
            return queryset.filter(proposal_cd__in=reviewed_list)
        elif self.value() == 'not reviewed':
            return queryset.all().exclude(proposal_cd__in=reviewed_list)
