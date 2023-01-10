from PyQt5.QtWidgets import *
import sys
import fins
import fins.udp

fins_instance = fins.udp.UDPFinsConnection()

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()

        self.setFixedWidth(300)

        self.setLayout(layout)
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(360)
        self.dial.setValue(40)
        self.dial.valueChanged.connect(self.sliderMoved)

        self.degreeLabel = QLabel()

        self.initButton = QPushButton()
        self.stopButton = QPushButton()

        self.degreeLabel.setText("empty")

        self.stopButton.setText("Press To stop servo")
        self.initButton.setText("Press to Connect")

        self.stopButton.clicked.connect(self.disconnectPLC)
        self.initButton.clicked.connect(self.connectToPLC)
        layout.addWidget(self.initButton)
        layout.addWidget(self.stopButton)

        layout.addWidget(self.degreeLabel)

        layout.addWidget(self.dial)

        print("method to conenct")

        fins_instance.dest_node_add =41  #node -> the last numbers of the ip addresss
        fins_instance.srce_node_add =46


    def sliderMoved(self):
        print("Dial value = %i" % (self.dial.value()))
        fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x03\x00',b'\x00\x01',1) # to val 1
        fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x04\x00', self.dial.value().to_bytes(2,'big'),1) #set all
        self.degreeLabel.setText(str(self.dial.value()))

    def connectToPLC(self):
        fins_instance.connect('192.168.250.41')
        fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x02\x00',b'\x00\x02',1) #set all

    def disconnectPLC(self):
        print("disconnecting")
        fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x02\x00',b'\x00\x00',1) #set all


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())