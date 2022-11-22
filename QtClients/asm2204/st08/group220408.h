#ifndef GROUP_220408_H
#define GROUP_220408_H

#include <QJsonArray>
#include <QNetworkReply>
#include "qrest.h"

QT_BEGIN_NAMESPACE
namespace ST220408
{

    class Group
    {
        QRest& rest;
    public:
        QString stPart = "";
        Group(QRest&);

        void GetSts();
        void SetSt(int st);
        void GetAllObj();
        void AddObj(QJsonObject obj);
        void DelObj(QJsonObject obj);
        void UpdObj(QJsonObject obj);

//        void GetNotes();
//        void AddNote(QJsonObject obj);
//        void UpdateNote(QJsonObject obj);
//        void DeleteNote(int id, QString type);
//        void LoadFromFile();
    };

}
QT_END_NAMESPACE

#endif // DIALOG220421_H
