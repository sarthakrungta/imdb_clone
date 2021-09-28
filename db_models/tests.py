from django.test import TransactionTestCase
from db_models.models import *
from django.db.utils import IntegrityError

class ModelTestCase(TransactionTestCase):

	def test_add_production_company(self):
		proco = ProductionCompany()
		proco.proco_id = 1
		proco.proco_name = "Test Company"
		proco.save()

	def test_add_show(self):
		proco = ProductionCompany()
		proco.proco_id = 1
		proco.proco_name = "Test Company"
		proco.save()
		show = Show()
		show.showid = 1
		show.show_title = "Test_Title"
		show.genre = "Action"
		show.length = 2.3
		show.movie = 1
		show.series = 0
		show.proco = proco
		show.year = 2019
		show.image_url = ""
		show.status = 1
		show.save()

	def test_add_show_raise_integrity_error(self):
		proco = ProductionCompany()
		proco.proco_id = 1000
		proco.proco_name = "Test Company"
		show = Show()
		show.showid = 1
		show.show_title = "Test_Title"
		show.genre = "Action"
		show.length = 2.3
		show.movie = 1
		show.series = 0
		show.proco = proco
		show.year = 2019
		show.image_url = ""
		show.status = 1
		self.assertRaises(IntegrityError,show.save)

