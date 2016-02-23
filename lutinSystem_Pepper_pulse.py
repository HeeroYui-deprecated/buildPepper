#!/usr/bin/python
# -*- coding: utf-8 -*-
##
## @author Edouard DUPIN
##
## @copyright 2012, Edouard DUPIN, all right reserved
##
## @license APACHE v2.0 (see license file)
##

from lutin import debug
from lutin import system
from lutin import tools
import os

class System(system.System):
	def __init__(self, target):
		system.System.__init__(self)
		# create some HELP:
		self.help="PULSE : The Linux PulseAudio"
		
		return
		
		# check if the library exist:
		if not os.path.isfile(os.path.join(target.base_path_toolchain, "pulseaudio", "include", "pulse", "pulseaudio.h")):
			# we did not find the library reqiested (just return) (automaticly set at false)
			return;
		self.valid = True
		self.add_export_path(os.path.join(target.base_path_toolchain, "pulseaudio", "include"))
		self.add_export_sources(os.path.join(target.base_path_toolchain, "pulseaudio", "lib", "libpulse-simple.so"))
		self.add_export_sources(os.path.join(target.base_path_toolchain, "pulseaudio", "lib", "libpulse.so"))
		


