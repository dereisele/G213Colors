#!/usr/bin/env python3

from __future__ import print_function
import G213Colors
from time import sleep
import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

NAME = "G213 Colors"
PRODUCTS = ["G213", "G203"]

numArguments = len(sys.argv)    # number of arguments given

if numArguments > 1:
    option = str(sys.argv[1]) # option to use
else:
    option = ""


class Window(Gtk.Window):

    def btnGetHex(self, btn):
        color = btn.get_rgba()
        red = int(color.red * 255)
        green = int(color.green * 255)
        blue = int(color.blue * 255)
        hexColor = "%02x%02x%02x" % (red, green, blue)
        return hexColor

    def sbGetValue(self, sb):
        return sb.get_value_as_int()

    def sendStatic(self, product):
        myG = G213Colors
        myG.connectG(product)
        myG.sendColorCommand(self.btnGetHex(self.staticColorButton))
        if product == "G213":
            myG.saveData(myG.colorCommand[product].format(str(format(0, '02x')), self.btnGetHex(self.staticColorButton)))
        myG.disconnectG()

    def sendBreathe(self, product):
        myG = G213Colors
        myG.connectG(product)
        myG.sendBreatheCommand(self.btnGetHex(self.breatheColorButton), self.sbGetValue(self.sbBCycle))
        if product == "G213":
            myG.saveData(myG.breatheCommand[product].format(self.btnGetHex(self.breatheColorButton), str(format(self.sbGetValue(self.sbBCycle), '04x'))))
        myG.disconnectG()

    def sendCycle(self, product):
        myG = G213Colors
        myG.connectG(product)
        myG.sendCycleCommand(self.sbGetValue(self.sbCycle))
        if product == "G213":
            myG.saveData(myG.cycleCommand[product].format(str(format(self.sbGetValue(self.sbCycle), '04x'))))
        myG.disconnectG()

    def sendSegments(self, product):
        myG = G213Colors
        myG.connectG(product)
        data = ""
        for i in range(1, 6):
            print(i)
            print(self.btnGetHex(self.segmentColorBtns[i-1]))
            myG.sendColorCommand(self.btnGetHex(self.segmentColorBtns[i -1]), i)
            data += myG.colorCommand[product].format(str(format(i, '02x')), self.btnGetHex(self.segmentColorBtns[i -1])) + "\n"
            sleep(0.01)
        myG.disconnectG()
        if product == "G213":
            myG.saveData(data)

    def sendManager(self, product):
        if product == "all":
            for p in PRODUCTS:
                self.sendManager(p)
        else:
            self.stackName = self.stack.get_visible_child_name()
            if self.stackName == "static":
                self.sendStatic(product)
            elif self.stackName == "cycle":
                self.sendCycle(product)
            elif self.stackName == "breathe":
                self.sendBreathe(product)
            elif self.stackName == "segments":
                self.sendSegments(product)

    def on_button_clicked(self, button, product):
        global ctime
        global btime
        ctime = self.sbCycle.get_value_as_int()
        btime = self.sbBCycle.get_value_as_int()
        print(ctime)
        print(self.stack.get_visible_child_name())
        self.sendManager(product)

    def __init__(self):

        Gtk.Window.__init__(self, title=NAME)
        self.set_border_width(10)

        vBoxMain = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(vBoxMain)

        ###STACK
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(1000)

        ###STATIC TAB
        vBoxStatic = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.staticColorButton = Gtk.ColorButton()
        vBoxStatic.add(self.staticColorButton)

        self.stack.add_titled(vBoxStatic, "static", "Static")

        ###CYCLE TAB
        vBoxCycle = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.adjCycle = Gtk.Adjustment(5000, 500, 65535, 100, 100, 0)
        self.sbCycle = Gtk.SpinButton()
        self.sbCycle.set_adjustment(self.adjCycle)
        vBoxCycle.add(self.sbCycle)
        self.stack.add_titled(vBoxCycle, "cycle", "Cycle")

        ###BREATHE TAB

        vBoxBreathe = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.breatheColorButton = Gtk.ColorButton()
        vBoxBreathe.add(self.breatheColorButton)
        self.adjBCycle = Gtk.Adjustment(5000, 500, 65535, 100, 100, 0)
        self.sbBCycle = Gtk.SpinButton()
        self.sbBCycle.set_adjustment(self.adjBCycle)
        vBoxBreathe.add(self.sbBCycle)
        self.stack.add_titled(vBoxBreathe, "breathe", "Breathe")

        ###SEGMENTS TAB
        hBoxSegments = Gtk.Box(spacing=5)
        self.segmentColorBtns = [Gtk.ColorButton() for _ in range(5)]
        for btn in self.segmentColorBtns:
            hBoxSegments.pack_start(btn, True, True, 0)
        self.stack.add_titled(hBoxSegments, "segments", "Segments")

        ###STACK
        self.stack_switcher = Gtk.StackSwitcher()
        self.stack_switcher.set_stack(self.stack)
        vBoxMain.pack_start(self.stack_switcher, True, True, 0)
        vBoxMain.pack_start(self.stack, True, True, 0)

        ###SET BUTTONS
        hBoxSetButtons = Gtk.Box(spacing=5)
        self.setColorBtns = []
        for p in PRODUCTS:
            btn = Gtk.Button.new_with_label("Set" + p)
            hBoxSetButtons.pack_start(btn, True, True, 0)
            btn.connect("clicked", self.on_button_clicked, p)
        vBoxMain.pack_start(hBoxSetButtons, True, True, 0)

        ###SET ALL BUTTON
        btnSetAll = Gtk.Button.new_with_label("Set all")
        btnSetAll.connect("clicked", self.on_button_clicked, "all")
        vBoxMain.pack_start(btnSetAll, True, True, 0)


if "-t" in option:
    myG = G213Colors
    myG.connectG("G213")

    with open(myG.confFile, "r") as file:

        for command in file:
            print(command)
            command = command.strip()
            if command and "," not in command:
                myG.sendData(command)
                myG.receiveData()
                sleep(0.01)

            if "," in command:
                print("\",\" is not supported in the config file.")
                print("If you apply a color scheme with segments, please re-apply it or replace all \",\" with new lines in \"/etc/G213Colors.conf\".")

    myG.disconnectG()
    sys.exit(0)

win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
