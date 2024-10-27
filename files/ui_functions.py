from main import *
import json
import os

f = open("settings.json")
Data = json.load(f) 

theme_load = open(f"files/themes/copilot-light.json")
Theme = json.load(theme_load) 

defaultTheme = Data["app-info"]["theme"]
default_font = Theme["default-font"]
color_1 = Theme["colors"]["color-1"]
color_2 = Theme["colors"]["color-2"]
main_border = Theme["colors"]["main-border"]
main_bg_color = Theme["colors"]["main-bg-color"]
default_font_color = Theme["default-font-color"]

import random

score = 0
user_input = "None"
ai_input = "None"

class UIFunctions(MainWindow):

	def SetTheme(self):
		
		str = open(f"files/themes/{defaultTheme}.qss", 'r').read()
		self.ui.centralwidget.setStyleSheet(str)
		

	def SwitchTheme(self):

		global defaultTheme
		
		if defaultTheme == "light":
			str = open(f"files/themes/dark.qss", 'r').read()
			self.ui.centralwidget.setStyleSheet(str)

			defaultTheme = "dark"

		elif defaultTheme == "dark":
			str = open(f"files/themes/light.qss", 'r').read()
			self.ui.centralwidget.setStyleSheet(str)

			defaultTheme = "light"



	def SwitchTheme(self):
		global defaultTheme

		# Directory where your .qss files are located
		qss_directory = "files/themes"

		# Get a list of all .qss files in the directory
		qss_files = [file for file in os.listdir(qss_directory) if file.endswith(".qss")]

		# Find the index of the current theme
		try:
			current_index = qss_files.index(defaultTheme + ".qss")
		except ValueError:
			current_index = -1

		# Calculate the next theme index
		next_index = (current_index + 1) % len(qss_files)
		next_theme = qss_files[next_index].replace(".qss", "")

		# Read and apply the next theme
		with open(os.path.join(qss_directory, qss_files[next_index]), 'r') as f:
			stylesheet = f.read()
		self.ui.centralwidget.setStyleSheet(stylesheet)
		defaultTheme = next_theme


	def ToggleMenu(self, min, max):

		presentWidth = self.ui.leftMenu.width()

		startToggle = ""
		endToggle = ""

		if presentWidth == min:
			startToggle = min
			endToggle = max
			
			self.ui.home_btn.setText("Home")
			self.ui.settings_btn.setText("Settings")
			self.ui.theme_btn.setText("Theme")

		elif presentWidth == max:
			startToggle = max
			endToggle = min

			self.ui.home_btn.setText("")
			self.ui.settings_btn.setText("")
			self.ui.theme_btn.setText("")


		self.animation = QPropertyAnimation(self.ui.leftMenu, b"minimumWidth")
		self.animation.setDuration(200)
		self.animation.setStartValue(startToggle)
		self.animation.setEndValue(endToggle)
		self.animation.setEasingCurve(QEasingCurve.InOutQuart)
		self.animation.start()

	def Replay(self):
		score = 0
		self.ui.label.setText(f"Score : {score}")
		self.ui.result_lbl.setText("Yet to Begin")
		self.ui.player_choice_lbl.setStyleSheet(f"")
		self.ui.ai_choice_lbl.setStyleSheet(f"")
		

	def AI_Move(self):
		global ai_input
		ai_input = random.choice(["stone", "paper", "scissor"])  # AI randomly picks move

	def Game(self, user_input):
		UIFunctions.AI_Move(self)
		global score

		outcome_map = {
			("stone", "paper"): "AI Won!",
			("stone", "scissor"): "You Won!",
			("paper", "scissor"): "AI Won!",
			("paper", "stone"): "You Won!",
			("scissor", "stone"): "AI Won!",
			("scissor", "paper"): "You Won!"
		}
		
		if user_input == ai_input:
			result = "It's a Tie!"
		else:
			result = outcome_map.get((user_input, ai_input), "")
			if result == "You Won!":
				score += 1
				self.ui.label.setText(f"Score : {score}")
		
		print(result)
		self.ui.player_choice_lbl.setStyleSheet(f"image: url(:/dark img/dark/img/{user_input}.png);")
		self.ui.ai_choice_lbl.setStyleSheet(f"image: url(:/dark img/dark/img/{ai_input}.png);")
		self.ui.result_lbl.setText(result)
		


	def Setup_GUI(self):

		# set window title
		self.setWindowTitle(Data["app-info"]["name"])

		# UIFunctions.AboutApp(self)

		# set windows default size
		self.resize(Data["app-info"]["window-size"]["default"][0], Data["app-info"]["window-size"]["default"][1])

		# set window min size
		if Data["app-info"]["window-size"]["isMin"] != False:
			self.setMinimumSize(Data["app-info"]["window-size"]["min"][0], Data["app-info"]["window-size"]["min"][1])
		
		# set window max size
		if Data["app-info"]["window-size"]["isMax"] != False:
			self.setMaximumSize(Data["app-info"]["window-size"]["max"][0], Data["app-info"]["window-size"]["max"][1])
			

		self.ui.home_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(0))
		self.ui.settings_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(1))

		self.ui.theme_btn.clicked.connect(lambda : UIFunctions.SwitchTheme(self))

		self.ui.menu_btn.clicked.connect(lambda : UIFunctions.ToggleMenu(self, 50, 300))

		import os
		self.ui.exit_btn.clicked.connect(self.close)

		# WindowIcon = QIcon()
		# WindowIcon.addFile("files/assest/icon.png")
		# self.setWindowIcon(WindowIcon)

		

		


		self.ui.stone_btn.clicked.connect(lambda : UIFunctions.Game(self, "stone"))
		self.ui.paper_btn.clicked.connect(lambda : UIFunctions.Game(self, "paper"))
		self.ui.scissor_btn.clicked.connect(lambda : UIFunctions.Game(self, "scissor"))	

		self.ui.replay_btn.clicked.connect(lambda : UIFunctions.Replay(self))