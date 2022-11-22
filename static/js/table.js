document.addEventListener('DOMContentLoaded', () => {

    const getSort = ({ target }) => {
        const order = (target.dataset.order = -(target.dataset.order || -1));
        const index = [...target.parentNode.cells].indexOf(target);
        const collator = new Intl.Collator(['en', 'ru'], { numeric: true });
        const comparator = (index, order) => (a, b) => order * collator.compare(
            a.children[index].innerHTML,
            b.children[index].innerHTML
        );

        for(const tBody of target.closest('table').tBodies)
            tBody.append(...[...tBody.rows].sort(comparator(index, order)));

        for(const cell of target.parentNode.cells)
            cell.classList.toggle('sorted', cell === target);
    };

    document.querySelectorAll('.table_sort thead').forEach(tableTH => tableTH.addEventListener('click', () => getSort(event)));

});

function validate(){
   //Считаем значения из полей name и email в переменные x и y
   var name=document.forms["employee_add_form"]["имя"].value;
   var surname=document.forms["employee_add_form"]["фамилия"].value;
   var email=document.forms["employee_add_form"]["e-mail"].value;

   //Если поле name пустое выведем сообщение и предотвратим отправку формы
   if (name.length==0){
      alert("Поле 'Имя' обязательно для заполнения");
      return false;
   }
   //Если поле email пустое выведем сообщение и предотвратим отправку формы
   if (surname.length==0){
      alert("Поле 'Фамилия' обязательно для заполнения");
      return false;
   }
   //Проверим содержит ли значение введенное в поле email символы @ и .
   at=email.indexOf("@");
   dot=email.indexOf(".");
   //Если поле не содержит эти символы знач email введен не верно
   if (at<1 || dot <1){
      alert("email введен не верно");
      return false;
   }
}