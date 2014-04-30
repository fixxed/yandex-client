# #!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from yandex import yandexDisk
from PyQt4 import QtGui, QtCore

class yandexDiskTray(QtGui.QSystemTrayIcon):
	yandexDisk = yandexDisk()
	menuInfoItems = ["error","status", "progress", "size", "free"]
	menuInfoText = {"error": u"Статус","status": u"Статус", "progress": u"Прогресс", "size": u"Всего", "free": u"Свободно"}
	menu = ''
	timerId = ''

	def __init__(self, parent=None):
		QtGui.QSystemTrayIcon.__init__(self, parent)

		icon = QtGui.QIcon('ya.png')

		#Создаем меню
		menu = QtGui.QMenu()
		start = menu.addAction(u'Запустить')#, self.yandexDisk.start)
		stop = menu.addAction(u'Остановить')#, self.yandexDisk.stop)
		if(self.yandexDisk.status == 1):
			start.setDisabled(True)
		else:
			stop.setDisabled(True)

		#Добавляем красивый разделитель
		menu.addSeparator()
		#Строим инфо пункты меню
		for item in self.menuInfoItems:
			action = menu.addAction(item)
			action.setDisabled(True)
			action.setWhatsThis(item)
		#Добавляем красивый разделитель
		menu.addSeparator()

		exit = menu.addAction(u'Выход', sys.exit)

		#Назначаем события пунктам меню
		start.triggered.connect(lambda: stop.setEnabled(1))
		start.triggered.connect(lambda: start.setDisabled(1))

		stop.triggered.connect(lambda: start.setEnabled(1))
		stop.triggered.connect(lambda: stop.setDisabled(1))

		menu.aboutToShow.connect(self.updateMenuInfo)
		menu.aboutToShow.connect(self.goTimer)

		self.menu = menu

		self.setIcon(icon)
		self.setVisible(1)
		self.setContextMenu(menu)

	def updateMenuInfo(self):
		self.yandexDisk.updateInfo()
		for action in self.menu.actions():
			itemName = unicode(action.whatsThis())
			if(itemName in self.menuInfoItems):
				text = self.menuInfoText[itemName]
				text = text + ": "
				method = getattr(self.yandexDisk, "get"+itemName.capitalize())
				if(method() != False):
					text = text + method()
					action.setText(text)
					action.setVisible(1)
				else:
					action.setVisible(0)
	
	def goTimer(self):
		self.timerId = self.startTimer(2000)

	def stopTimer(self):
		self.killTimer(self.timerId)

	def timerEvent(self, event):
		self.updateMenuInfo()

app = QtGui.QApplication(sys.argv)

main = yandexDiskTray()
main.show()

sys.exit(app.exec_())