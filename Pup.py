from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.navigationbar import (MDNavigationBar, MDNavigationItem)
from kivymd.uix.navigationdrawer import (MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText)
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
Window.size = (350, 600)

class BaseMDNavigationItem(MDNavigationItem):
	icon = StringProperty()
	text = StringProperty()

class MyCard(MDCard):
	text = StringProperty()

class Home(MDScreen):
	...

class Cookbook(MDScreen):
	...

class Search(MDScreen):
	...

class About(MDScreen):
	...

class Login(MDScreen):
	...

class BaseScreen(MDScreen):
	...

class Breakfast(MDScreen):
	...

class Lunch(MDScreen):
	...

class Dinner(MDScreen):
	...

class Desserts(MDScreen):
	...

class Drinks(MDScreen):
	...

class Breads(MDScreen):
	...

class Meats(MDScreen):
	...

class Sauces(MDScreen):
	...

class SausagePatties(MDScreen):
	...

class Waffles(MDScreen):
	...

class Pancakes(MDScreen):
	...

class Biscuits(MDScreen):
	...

class BiscuitsGravy(MDScreen):
	...

class LoafBread(MDScreen):
	...

class PizzaBombs(MDScreen):
	...

class PizzaDough(MDScreen):
	...

class Pepperoni(MDScreen):
	...

class Sausage(MDScreen):
	...

class ChilliChicken(MDScreen):
	...

class GarlicAndGingerPaste(MDScreen):
	...

class PizzaGrilledCheese(MDScreen):
	...

class PizzaSauce(MDScreen):
	...

class CreamsicleCookies(MDScreen):
	...

class WhiteCakeMix(MDScreen):
	...

class SearchResults(MDScreen):
	...

class PupCook(MDApp):

	def on_switch_tabs(
		self,
		bar: MDNavigationBar,
		item: MDNavigationItem,
		item_icon: str,
		item_text: str,
	):
		self.root.ids.screen_manager.current = item_text

	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Blue"
		return Builder.load_file("Pup.kv")

	def search(self, search_text):
		if search_text != "":
			self.root.ids.search_label.text = search_text
			self.root.ids.screen_manager.current = "search_results"


		sm = MDScreenManager()
		sm.add_widget(Home(name = "Home"))
		sm.add_widget(Cookbook(name = "Cookbook"))
		sm.add_widget(Search(name = "Search"))
		sm.add_widget(About(name = "About"))
		sm.add_widget(Login(name = "Login"))
		sm.add_widget(SearchResults(name = "SearchResults"))
		sm.add_widget(Breakfast(name = "Breakfast"))
		sm.add_widget(Lunch(name = "Lunch"))
		sm.add_widget(Dinner(name = "Dinner"))
		sm.add_widget(Desserts(name = "Desserts"))
		sm.add_widget(Drinks(name = "Drinks"))
		sm.add_widget(Breads(name = "Breads"))
		sm.add_widget(Meats(name = "Meats"))
		sm.add_widget(Sauces(name = "Sauces"))
		sm.add_widget(SausagePatties(name = "SausagePatties"))
		sm.add_widget(Waffles(name = "Waffles"))
		sm.add_widget(Pancakes(name = "Pancakes"))
		sm.add_widget(Biscuits(name = "Biscuits"))
		sm.add_widget(BiscuitsGravy(name = "BiscuitsGravy"))
		sm.add_widget(LoafBread(name = "LoafBread"))
		sm.add_widget(PizzaBombs(name = "PizzaBombs"))
		sm.add_widget(PizzaDough(name = "PizzaDough"))
		sm.add_widget(Pepperoni(name = "Pepperoni"))
		sm.add_widget(Sausage(name = "Sausage"))
		sm.add_widget(ChilliChicken(name = "ChilliChicken"))
		sm.add_widget(GarlicAndGingerPaste(name = "GarlicAndGingerPaste"))
		sm.add_widget(PizzaGrilledCheese(name = "PizzaGrilledCheese"))
		sm.add_widget(PizzaSauce(name = "PizzaSauce"))
		sm.add_widget(CreamsicleCookies(name = "CreamsicleCookies"))
		sm.add_widget(WhiteCakeMix(name = "WhiteCakeMix"))
		return sm


PupCook().run()
