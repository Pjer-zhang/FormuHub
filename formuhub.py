# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 07:42:59 2016

@author: Pjer1
"""
import sys,os
import plot_formular
import get_dir
#import matplotlib as plt
from PyQt4.QtCore import Qt,SIGNAL,SLOT,QSize
import PyQt4.QtGui as qt


class formuhub(qt.QWidget):
    def __init__(self,parent=None):
        qt.QWidget.__init__(self,parent)
#get ready for dictionary      
        self.DataBaseDictionary=self.prepareDict()        
        self.searchDict=self.getdataready()
                
        self.setGeometry(200,200,600,300)
        self.setBackgroundRole(qt.QPalette.Dark)
        self.setWindowTitle('FormuHub')
        self.setStyleSheet("background-color:white;")
#        self.setWindowIcon(qt.QIcon('icons/pjer.ico')) 
        
        
#essentail controls        
        self.evtexit = qt.QAction(qt.QIcon('icon/exit.png'),'Exit',self)
        self.evtexit.setShortcut('Ctrl+Q')
        self.evtexit.setStatusTip('Exit application')
        self.connect(self.evtexit,SIGNAL('triggered()'),SLOT('close()'))
    
        
        self.evtopen = qt.QAction(qt.QIcon('icon/open.png'),'Open Formula(.tex)',self)
        self.evtopen.setShortcut('Ctrl+O')
        self.evtopen.setStatusTip('Open Tex File')
        self.connect(self.evtopen,SIGNAL('triggered()'),self.getTexFile)
        
        
        self.search_btn = qt.QPushButton("Search")
        self.open_btn = qt.QPushButton("Open")
        self.prev_btn = qt.QPushButton("Preview")
        self.save_pdf_btn = qt.QPushButton("->PDF")
        self.save_png_btn = qt.QPushButton("->PNG")
        
        self.search_btn.clicked.connect(self.searchCommand)
        
        self.search_btn.setStyleSheet("color: white;"
                        "background-color: #80c342;"
                        "selection-color: white;"
                        "selection-background-color: #90c342;"
                        "border-style: outset;"
                        "border-width: 2px;"
                        "border-radius: 10px;"
                        "border-color: beige;"
                        "font: bold 12px;"
                        "padding: 6px;"
                        );   
                        
        self.open_btn.setStyleSheet("color: white;"
                        "background-color: #80c342;"
                        "selection-color: white;"
                        "selection-background-color: #90c342;"
                        "border-style: outset;"
                        "border-width: 2px;"
                        "border-radius: 10px;"
                        "border-color: beige;"
                        "font: bold 12px;"
                        "padding: 6px;"
                        "width:30px"
                        );
                        
        self.prev_btn.setStyleSheet("color: white;"
                        "background-color: #80c342;"
                        "selection-color: white;"
                        "selection-background-color: #90c342;"
                        "border-style: outset;"
                        "border-width: 2px;"
                        "border-radius: 10px;"
                        "border-color: beige;"
                        "font: bold 12px;"
                        "padding: 6px;"
                        ); 
                        
        self.save_pdf_btn.setStyleSheet("color: white;"
                        "background-color: #80c342;"
                        "selection-color: white;"
                        "selection-background-color: #90c342;"
                        "border-style: outset;"
                        "border-width: 2px;"
                        "border-radius: 10px;"
                        "border-color: beige;"
                        "font: bold 12px;"
                        "padding: 6px;"
                        );  
                        
        self.save_png_btn.setStyleSheet("color: white;"
                        "background-color: #80c342;"
                        "selection-color: white;"
                        "selection-background-color: #90c342;"
                        "border-style: outset;"
                        "border-width: 2px;"
                        "border-radius: 10px;"
                        "border-color: beige;"
                        "font: bold 12px;"
                        "padding: 6px;"
                        );  
        
        self.texbrowser = qt.QTextBrowser()
        self.searchInput = qt.QLineEdit("Type your wanted formular") 

        self.completer  = qt.QCompleter(self.searchDict)
        self.completer.setCompletionMode(qt.QCompleter.UnfilteredPopupCompletion)
        self.searchInput.setCompleter(self.completer)        
        
        self.latexResult = qt.QFrame()        
        self.latexResult.setFrameStyle(qt.QFrame.StyledPanel|qt.QFrame.Sunken)
        #self.latexResult.setFixedHeight(120)  
        self.tex_layout=qt.QVBoxLayout()        
        self.latexResult.setLayout(self.tex_layout)
        
#build up tree
        self.treev = qt.QTreeView()

#layout manage
        self.main_layout   = qt.QHBoxLayout()      
        self.vlayout_left  = qt.QVBoxLayout()       
        self.vlayout_right = qt.QVBoxLayout()        
        self.hlayout_left_up=qt.QHBoxLayout()        
        self.result_layout = qt.QHBoxLayout()
        self.btn_layout    = qt.QVBoxLayout()
        
        #self.btn_layout.SetMaximumSize(120,50)
                
        self.spac=qt.QSpacerItem(40,10)        
        self.spac1=qt.QSpacerItem(40,10)
        self.vlayout_left.addItem(self.spac)      
        self.vlayout_right.addItem(self.spac1)        
        
        
        self.hlayout_left_up.addWidget(self.searchInput)
        self.hlayout_left_up.addWidget(self.search_btn)   
        self.vlayout_left.addLayout(self.hlayout_left_up)
        self.vlayout_left.addWidget(self.treev)

        self.model = qt.QFileSystemModel()
        self.model.setRootPath('e://')
        self.treev.setModel(self.model)
        #self.treev.header().close()
        self.model.setHeaderData(0,Qt.Horizontal,"king")        
        self.treev.setIconSize(QSize(2,2))
        self.treev.setColumnHidden(2,True)
        self.treev.setColumnHidden(3,True)
        self.treev.setColumnHidden(4,True)        
        self.treev.setColumnHidden(1,True)
        self.treev.setRootIndex(self.model.index(os.getcwd()+os.sep+'DataBase'))
    
        self.vlayout_right.addWidget(self.texbrowser)
        self.vlayout_right.addLayout(self.result_layout)
        self.result_layout.addWidget(self.latexResult,3)
        self.result_layout.addLayout(self.btn_layout,1)
        
        
        mathText=r'$X_k = \sum_{n=0}^{N-1} x_n . e^{\frac{-i2\pi kn}{N}}$'
        self.tex_layout.addWidget(plot_formular.MathTextLabel(mathText, self), alignment=Qt.AlignHCenter)

        
        self.btn_layout.addWidget(self.open_btn)
        self.btn_layout.addWidget(self.prev_btn)
        self.btn_layout.addWidget(self.save_pdf_btn)
        self.btn_layout.addWidget(self.save_png_btn)       
        
        self.main_layout.addLayout(self.vlayout_left,2)
        self.main_layout.addLayout(self.vlayout_right,3)
        
        self.setLayout(self.main_layout)   
        self.searchInput.selectAll() 
        
    def closeEvent(self,event):
        reply = qt.QMessageBox.question(self,
                                           'Message',"Are you sure to quit",
                                           qt.QMessageBox.Yes,
                                           qt.QMessageBox.No)
        if reply == qt.QMessageBox.Yes:
            event.accept
        else:
            event.ignore
    
    def getTexFile(self):
        ## open a '.tex file'
        filename = qt.QFileDialog.getOpenFileName(self,'Open file')
        if filename:
            filestream = open(filename)
            self.texbrowser.setText(filestream.read())
            
    def getdataready(self):
        d={}
        k=[]
        get_dir.traverse(os.getcwd()+os.sep+'DataBase',0,d,k)
        return k

    def prepareDict(self):
        d={}
        k=[]
        get_dir.traverse(os.getcwd()+os.sep+'DataBase',0,d,k)
        return d
        
    def searchCommand(self):
        KEYstr=self.searchInput.text()
        #print KEYstr
        if self.DataBaseDictionary.has_key(KEYstr):
            filename = self.DataBaseDictionary[KEYstr]
            print filename
            if filename:
                filestream = open(filename)
                self.texbrowser.setText(filestream.read())
        else:
            qt.QMessageBox.information(self, 'PyQt', 'No match')
    
    
app = qt.QApplication(sys.argv)

if __name__=='__main__':
    formu=formuhub()
    formu.show()
    sys.exit(app.exec_())
    
    