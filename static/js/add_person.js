var select = document.querySelector('select');
var number1 = document.getElementById('obj_number1');

select.addEventListener('change', () => {
  set_new_obj(select.value);
});

function set_new_obj(value) {
  // задаваемый параметр
  let label1 = document.getElementById('obj_label1');


  if (value == "Читатель"){
    number1.name = "Age";
    number1.placeholder = "Введите возраст читателя";
    label1.textContent = "Возраст";
  } else {
    number1.name= "Experience";
    number1.placeholder = "Введите стаж писателя";
    label1.textContent = "Стаж";

  }

}
