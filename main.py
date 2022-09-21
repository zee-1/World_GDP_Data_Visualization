import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QDialog,QComboBox,QStackedWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore

from utilityTools import init_with_countries,init_with_years,show_choropleth,plot_with_plotly,get_country_data,barplot_top_contributors

class mainWin(QDialog):
      """
            mainWin creates a QDialog window and loads the ui file
            Methods Defined:


            -__init__: initializes the window and loads the ui file and connect the buttons to the functions

            -show_choropleth_: shows the choropleth map for the selected year
            
            -reset_queue: resets the queue
            
            -insert_in_queue: inserts the selected country in the queue

            -show_2_clicked: shows the barplot of the top contributors for the selected year

            -plot: plots lineplot of the countries in the queue

      """
      queue = []
      def __init__(self):
            # init the window
            super(mainWin,self).__init__()

            # set the dimensions of the window
            self.setMinimumHeight(600)
            self.setMinimumWidth(800)

            # load the ui file
            loadUi('gdp.ui',self)

            # inititalize the comboBox with the years
            init_with_years(self.comboBox_2)
            init_with_years(self.comboBox_4)

            # inititalize the comboBox with the countries
            init_with_countries(self.comboBox_3)

            # connect the buttons to the functions
            self.yearly.clicked.connect(self.show_choropleth_)
            self.add.clicked.connect(self.insert_in_queue)
            self.reset.clicked.connect(self.reset_queue)
            self.show.clicked.connect(self.plot)
            self.show_2.clicked.connect(self.show_2_clicked)

      def plot(self):
            """
                  plot plots lineplot of the countries in the queue
            """
            data_list = []
            for i in self.queue:
                  data_list.append(get_country_data(i))
            plot_with_plotly(data_list)
            self.reset_queue()

      def show_choropleth_(self):
            """
                  show_choropleth_ shows the choropleth map for the selected year in comboBox
            """
            year = self.comboBox_2.currentText()
            show_choropleth(year)
      
      def reset_queue(self):
            """
                  reset_queue resets the queue
            """
            self.queue = []
            self.count.setText('0 countries added to queue')

      def insert_in_queue(self):
            """
                  insert_in_queue inserts the selected country in comboBox to the queue
            """
            txt = self.comboBox_3.currentText()
            if txt != '--Select Country--' and (txt not in self.queue):
                  self.queue.append(self.comboBox_3.currentText())
                  self.count.setText(str(len(self.queue)) + ' countries added to queue')

      def show_2_clicked(self):
            """
                  show_2_clicked shows the barplot of the top contributors for the selected year in comboBox
            """
            year = self.comboBox_4.currentText()
            barplot_top_contributors(year)

# create the application
app = QtWidgets.QApplication(sys.argv)
# create the instance of the main window
MainWin = mainWin()

# create a stack widget to hold the different pages
stack = QStackedWidget()
# add the main window to the stack
win = mainWin()
stack.addWidget(win)
# show the stack
stack.show()


sys.exit(app.exec_())