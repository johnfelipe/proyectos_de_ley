import datetime

from django.test import TestCase, Client

from pdl.models import Proyecto
from stats.models import Dispensed
from stats.models import ComisionCount
from stats import views


class TestStatsViews(TestCase):
    def setUp(self):
        Proyecto.objects.create(**{
            'numero_proyecto': '02764',
            'time_created': datetime.datetime.now(),
            'fecha_presentacion': '2010-10-10',
        })
        Dispensed.objects.create(**{
            'total_approved': 1444,
            'total_dispensed': 864,
            'dispensed_by_plenary': 23,
            'dispensed_by_spokesmen': 12,
            'dispensed_others': 11,
        })
        ComisionCount.objects.create(**{
            'count': 7,
            'comision': 'Justicia',
        })

    def test_index(self):
        c = Client()
        response = c.get('/stats/')
        self.assertEqual(200, response.status_code)

    def test_dame_sin_tramitar(self):
        numero_de_proyectos = Proyecto.objects.all().count()
        expected = (100.0, 1)
        result = views.dame_sin_tramitar(numero_de_proyectos)
        self.assertEqual(expected, result)
