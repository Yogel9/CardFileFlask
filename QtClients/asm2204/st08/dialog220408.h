#ifndef DIALOG220408_H
#define DIALOG220408_H

#include <QDialog>
#include <QAbstractButton>
#include <QNetworkReply>
#include <QDialog>
#include <QListWidgetItem>
#include "../../qrest.h"
#include "group220408.h"
#include <iostream>
#include <string>
#include <regex>


namespace Ui {
class Dialog220408;
}

class Dialog220408 : public QDialog
{
    Q_OBJECT

public:
    explicit Dialog220408(QWidget *parent = nullptr);
    ~Dialog220408();
    QJsonDocument JsonData;
    QString MY_NAME = "[2204-08] Довиденков 2204";

private slots:
    void onManagerFinished(QNetworkReply *reply);

    void on_buttonBox_accepted();

    void on_buttonBox_clicked(QAbstractButton *button);

    void on_ADD_Button_clicked();

    void on_EDIT_Button_clicked();

    void on_DEL_Button_clicked();

    void on_pushButton_clicked();

    void UpdateObj();

    void on_listWidget_itemClicked(QListWidgetItem *item);

    void on_CloseButton_clicked();

    void on_type_box_currentTextChanged(const QString &arg1);

    void on_WriterList_itemClicked(QListWidgetItem *item);

    void on_ReaderList_itemClicked(QListWidgetItem *item);

    void filling_in_the_fields(int number, QString type, QString ID);

    QString get_id_by_str(QString QString_item);

    void on_ADD_Button_2_clicked();

private:
    Ui::Dialog220408 *ui;
    QRest rest;
    QNetworkAccessManager manager;

    ST220408::Group group;
};

#endif // DIALOG220408_H
