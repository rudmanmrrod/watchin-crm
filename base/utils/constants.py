from django.utils.translation import ugettext_lazy as _

# constants for Catalog Groups Choices
COUNTRY =  _('COUNTRY')
STATE = _('STATE')
MUNICIPALITY = _('MUNICIPALITY')
PARISH =  _('PARISH')

CATALOG_GROUP_CHOICES = (
    (COUNTRY, COUNTRY),
    (STATE, STATE),
    (MUNICIPALITY, MUNICIPALITY),
    (PARISH, PARISH),
    )
