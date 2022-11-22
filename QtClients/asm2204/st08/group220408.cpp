#include "group220408.h"

#include <QMessageBox>
#include <QJsonDocument>
#include <string>
#include <iostream>

namespace ST220408
{

    Group::Group(QRest& r)
        :rest(r)
    {}

    void Group::GetSts()
    {
        rest.DoRequest(HTTP_GET);
    }

    void Group::SetSt(int st)
    {
        stPart = "st"+QString::number(st)+"/";
    }

    void Group::GetAllObj()
    {
        rest.DoRequest(HTTP_GET, stPart,"show");
    }


    void Group::AddObj(QJsonObject obj)
    {
        rest.DoRequest(HTTP_POST,stPart,"add_person",obj);
    }

    void Group::DelObj(QJsonObject obj)
    {
        rest.DoRequest(HTTP_POST,stPart,"del_person",obj);
    }

    void Group::UpdObj(QJsonObject obj)
    {
        rest.DoRequest(HTTP_POST,stPart,"edite_person",obj);
    }

//void Group::UpdateNote(QJsonObject obj)
//{
//    rest.DoRequest(HTTP_PUT,stPart,"",obj);
//}

//void Group::DeleteNote(int id, QString type)
//{
//    rest.DoRequest(HTTP_DELETE,stPart,QString("?id=%1&type=%2").arg(QString::number(id), type),QJsonObject());
//}

//void Group::LoadFromFile()
//{
//    rest.DoRequest(HTTP_GET,stPart,"load_from_file");
//}

}
