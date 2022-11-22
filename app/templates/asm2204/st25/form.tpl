<form action = '{{selfurl}}/st5/add' method=POST>

        <script>
        function changeFlag() {
          var checkBox = document.getElementById("flag");
          var text = document.getElementById("experience_level");
          var text2 = document.getElementById("skills_level");
          if (checkBox.checked == true){
            text.disabled = false;
            text2.disabled = true
          } else {
             text.disabled = true;
             text2.disabled=false
          }
        }
        </script>

        <input type="checkbox" id="flag" onclick="changeFlag()"> Аналитик
        <div><label><b>Имя: </b></label><input style="margin-left:2%"  type=text placeholder='Введите имя' name=first_name required value={{object.first_name}}></div>
        <div><label><b>Фамилия: </b></label><input style="margin-left:2%"  type=text placeholder='Введите фамилию' name=surname required value={{object.surname}}></div>
        <div><label"><b>Зарплата: </b></label><input style="margin-left:2%"  type=text placeholder='Введите зарплату' name=salary required value={{object.salary}}></div>
        <div><label><b>Сфера деятельности: </b></label><input style="margin-left:2%"  type=text placeholder='Введите сферу деятельности' name=activity_scope required value={{object.activity_scope}}></div>
        <div><label><b>Уровень навыков: </b></label><input style="margin-left:2%"  type=text placeholder='Введите уровень навыков' id=skills_level  name=skills_level value={{object.skills_level}}></div>
        <div><label><b>Опыт: </b></label><input disabled style="margin-left:2%" type=text  placeholder='Введите опыт' id=experience_level name=experience_level value={{object.experience_level}}></div>
        <br><input type=submit name="submit" value="Добавить разработчика">
        <br><input style="margin-top:1%" type=submit name="submit"value="Добавить аналитика">
</form>
