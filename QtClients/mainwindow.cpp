#include "mainwindow.h"
#include "ui_mainwindow.h"

#include "asm2204/st08/dialog220408.h"


#pragma GCC diagnostic ignored "-Wunused-variable"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    dlgs["[2204-08] Довиденков 2204"] = new Dialog220408;


    for(auto& [s, dlg]: dlgs)
    {
        ui->listWidget->addItem(s);
    }
    ui->listWidget->setCurrentRow(0);
}

MainWindow::~MainWindow()
{
    delete ui;
    for(auto& [s, dlg]: dlgs)
    {
        delete dlg;
    }
}


void MainWindow::on_runButton_clicked()
{
    QString s = ui->listWidget->currentItem()->text();
    if(auto d = dlgs.find(s); d != dlgs.end())
    {
        d->second->exec();
    }
}
