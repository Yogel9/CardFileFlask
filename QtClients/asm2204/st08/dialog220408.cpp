#include "dialog220408.h"
#include "ui_dialog220408.h"


using namespace std;

Dialog220408::Dialog220408(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog220408),
    rest(manager),
    group(rest)
{
    ui->setupUi(this);

    connect(&manager, &QNetworkAccessManager::finished, this, &Dialog220408::onManagerFinished);

    ui->age_box->setDisabled(true);
//    ui->exp_box->setDisabled(true);

    group.GetSts();
}

Dialog220408::~Dialog220408()
{
    delete ui;
}

void Dialog220408::onManagerFinished(QNetworkReply *reply)
{
    QString s = reply->readAll();
    QJsonDocument doc = QJsonDocument::fromJson(s.toUtf8());
    QString strJson(doc.toJson(QJsonDocument::Compact));
//    ui->InfoEdit->setText(strJson); вывод всего ответа в инфо

    // Если содержит список st
    if (doc.isObject() && doc.object().contains("sts"))
    {
        QJsonArray arr = doc.object()["sts"].toArray();

        for (auto items: arr)
        {
            if (items.toArray()[1].toString() == MY_NAME)
            {
                group.SetSt(items.toArray()[0].toInt());
//                ui->InfoEdit->setText(group.stPart);
                break;
            }
        }
        group.GetAllObj();
    }



    // Если содержит данные объектов
    if (doc.isObject() && doc.object().contains("Reader") && doc.object().contains("Writer"))
    {
        JsonData = doc;
        ui->ReaderList->clear();
        ui->WriterList->clear();
        // QString::number(arr1.size())
        //doc.object()["Reader"][i][2].toString()
        auto arr1 = doc.object()["Writer"].toArray();
        auto arr2 = doc.object()["Reader"].toArray();
        for(int i=0;i<arr1.size(); i++){
            ui->WriterList->addItem(
                        "ID:" + QString::number(doc.object()["Writer"][i][0].toInt())+
                        " Имя:" + doc.object()["Writer"][i][1].toString() +
                        " Фамилия:" + doc.object()["Writer"][i][2].toString() +
                        " Опыт:" + QString::number(doc.object()["Writer"][i][3].toInt()) +
                        " Зарплата:"+ QString::number(doc.object()["Writer"][i][4].toInt())  );
        }

        for(int i=0;i<arr2.size(); i++){
            ui->ReaderList->addItem(
                        "ID:" + QString::number(doc.object()["Reader"][i][0].toInt()) +
                        " Имя:" + doc.object()["Reader"][i][1].toString() +
                        " Фамилия:" + doc.object()["Reader"][i][2].toString() +
                        " Возраст:" +  QString::number(doc.object()["Reader"][i][3].toInt()) +
                        " Рейтинг:" + doc.object()["Reader"][i][4].toString()  );
        }


    }

    reply->deleteLater();

}

//запрос на все записи в бд
void Dialog220408::UpdateObj()
{
    group.GetAllObj();
}


void Dialog220408::on_buttonBox_accepted()
{

}


void Dialog220408::on_buttonBox_clicked(QAbstractButton *button)
{

}

//добавляем объект
void Dialog220408::on_ADD_Button_clicked()
{
    QJsonObject obj= {};

    QString type = ui->type_box->currentText();
    QString surname = ui->Surname_line->text();
    QString name = ui->Name_line->text();
    QString exp = ui->exp_box->text();
    QString age = ui->age_box->text();

    obj.insert("type",type);
    obj.insert("Surname",surname);
    obj.insert("Name",name);
    obj.insert("Experience",exp);
    obj.insert("Age",age);

    group.AddObj(obj);
    //Sleep(500); не хватает
    group.GetAllObj();
}

//изменяем объект
void Dialog220408::on_EDIT_Button_clicked()
{
    QJsonObject obj= {};
    QString type = ui->type_box->currentText();
    QString id = ui->ID_line->text();
    QString surname = ui->Surname_line->text();
    QString name = ui->Name_line->text();
    QString exp = ui->exp_box->text();
    QString age = ui->age_box->text();

    obj.insert("type",type);
    obj.insert("id", id);
    obj.insert("Surname",surname);
    obj.insert("Name",name);
    obj.insert("Experience",exp);
    obj.insert("Age",age);

    group.UpdObj(obj);
    group.GetAllObj();
}

//удаляем объект
void Dialog220408::on_DEL_Button_clicked()
{
    QJsonObject obj= {};
    QString type = ui->type_box->currentText();
    QString id = ui->ID_line->text();

    obj.insert("type",type);
    obj.insert("id", id);

    group.DelObj(obj);
    //Sleep(500); не хвататет
    group.GetAllObj();
}


// закрываем окно
void Dialog220408::on_CloseButton_clicked()
{
    this->close();
}


// блокировать ненужные поля
void Dialog220408::on_type_box_currentTextChanged(const QString &arg1)
{
    if(ui->type_box->currentText()=="Писатель")
    {
        ui->exp_box->setDisabled(false);
        ui->age_box->setDisabled(true);
    }
    else
    {
        ui->age_box->setDisabled(false);
        ui->exp_box->setDisabled(true);
    }
}


void Dialog220408::filling_in_the_fields(int number, QString type, QString ID)
{

    ui->Name_line->clear();
    ui->Surname_line->clear();
    ui->age_box->clear();
    ui->exp_box->clear();
    ui->ID_line->clear();

    ui->ID_line->setText(ID);
    ui->Name_line->setText(JsonData.object()[type][number][1].toString());
    ui->Surname_line->setText(JsonData.object()[type][number][2].toString());
    if(type=="Writer")
    {
        ui->exp_box->setValue(JsonData.object()[type][number][3].toInt());
        ui->type_box->setCurrentText("Писатель");
    }else if (type=="Reader")
    {
        ui->age_box->setValue(JsonData.object()[type][number][3].toInt());
        ui->type_box->setCurrentText("Читатель");
    }


}

QString Dialog220408::get_id_by_str(QString QString_item)
{
    // Если вдруг понадобиться забрать ID через регулярные выражения

    const string string_item = QString_item.toStdString();
    ui->InfoEdit->setText(QString::fromStdString(string_item));
    const regex r("ID:([0-9_]*)\\s"
                  );
    smatch m;
    regex_search(string_item, m, r);
    //id выбранного объекта m[1].str()
    return QString::fromStdString(m[1].str());
}

// Лист писателей
void Dialog220408::on_WriterList_itemClicked(QListWidgetItem *item)
{
    QString current_item = ui->WriterList->currentItem()->text();

    // автозаполняет выбранный элемент
    this->filling_in_the_fields(ui->WriterList->currentRow(), "Writer", this->get_id_by_str(current_item));



}

// Лист читателей
void Dialog220408::on_ReaderList_itemClicked(QListWidgetItem *item)
{
    QString current_item = ui->ReaderList->currentItem()->text();

    // автозаполняет выбранный элемент
    this->filling_in_the_fields(ui->ReaderList->currentRow(), "Reader", this->get_id_by_str(current_item));
}


void Dialog220408::on_pushButton_clicked() // не знаю как удалить
{

}

void Dialog220408::on_listWidget_itemClicked(QListWidgetItem *item)
{

}

void Dialog220408::on_ADD_Button_2_clicked()
{
    group.GetAllObj();
}

