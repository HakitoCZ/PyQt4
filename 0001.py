#!/usr/bin/python3
'''
Basic window
'''

import sys
from PyQt4 import QtGui, QtCore, uic

if __name__ == '__main__':
  app = QtGui.QApplication(sys.argv)
  app.setStyle('cleanlooks')

  data = ['one','two','three','four','five']

  listView = QtGui.QListView()
  listView.show()

  model = QtGui.QStringListModel(data)

  listView.setModel(model)


  combobox = QtGui.QComboBox()
  combobox.setModel(model)
  combobox.show()


  sys.exit(app.exec_())
