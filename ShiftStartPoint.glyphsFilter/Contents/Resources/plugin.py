# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog plug-in
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class ShiftStartPoint(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Shift Start Point',
			'de': 'Startpunkt weiterschieben',
			# 'fr': 'Mon filtre',
			# 'es': 'Mi filtro',
			# 'pt': 'Meu filtro',
			# 'jp': '私のフィルター',
			# 'ko': '내 필터',
			# 'zh': '我的过滤器',
			})

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		steps = 1
		if "steps" in customParameters:
			steps = int(customParameters['steps'])
		
		for p in layer.paths:
			if len(p.nodes) > steps:
				for n in p.nodes[steps:]:
					if n.type != OFFCURVE:
						newNode = layer.dividePathAtNode_(n)
						p.removeNode_(newNode)
						p.closed = True
						break
		layer.cleanUpPaths()

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
