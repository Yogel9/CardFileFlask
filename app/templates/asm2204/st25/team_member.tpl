<p></p>
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">{{i.first_name}} {{i.surname}}</h5>
    <p class="card-text"><b>Заработная плата:</b> {{i.salary}} рублей</p>
        <p class="card-text"><b>Сфера деятельности:</b> {{i.activity_scope}}</p>
     {% if i.skills_level %}
         <p class="card-text"><b>Уровень навыков:</b> {{i.skills_level}}</p>
{% endif %}
{% if i.experience_level %}
<p class="card-text"><b>Опыт:</b> {{i.experience_level}} лет</p>
{% endif %}
    <a href="{{selfurl}}/st5/delete/{{i.id}}" class="btn btn-primary">Удалить</a>

    <button type="button" class="btn btn-light" data-bs-toggle="modal" data-bs-target="#exampleModal{{i.id}}">Редактировать</button>
    <!-- Modal with info -->
            <div class="modal fade" id="exampleModal{{i.id}}" tabindex="-1" aria-labelledby="rules" aria-hidden="true">
              <div class="modal-dialog modal-l">
                <div class="modal-content">
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  <div class="modal-body">
        <div><label><b>Имя: </b></label><input style="margin-left:2%"  type=text placeholder={{i.first_name}} name=first_name_edit{{i.id}} required value={{i.first_name}}></div>
        <div><label><b>Фамилия: </b></label><input style="margin-left:2%"  type=text placeholder={{i.surname}} name=surname_edit{{i.id}} required value={{i.surname}}></div>
        <div><label"><b>Зарплата: </b></label><input style="margin-left:2%"  type=text placeholder={{i.salary}} name=salary_edit{{i.id}} required value={{i.salary}}></div>
        <div><label><b>Сфера деятельности: </b></label><input style="margin-left:2%"  type=text placeholder={{i.activity_scope}} name=activity_scope_edit{{i.id}} required value={{i.activity_scope}}></div>

         {% if i.skills_level %}
                 <div><label><b>Уровень навыков: </b></label><input style="margin-left:2%"  type=text placeholder={{i.skills_level}} name=skills_level_edit{{i.id}} value={{i.skills_level}}></div>
        <a href="{{selfurl}}/st5/edit/{{i.id}}" class="btn btn-primary">Сохранить</a>
        {% endif %}

                 {% if i.experience_level %}
                 <div><label><b>Опыт: </b></label><input style="margin-left:2%" type=text placeholder={{i.experience_level}} name=experience_level_edit{{i.id}} value={{i.experience_level}}></div>
        <a href="{{selfurl}}/st5/edit/{{i.id}}" class="btn btn-primary">Сохранить</a>
        {% endif %}
              </div>
            </div>
            </div>
            </div>
  </div>
</div>