{% extends "asm2204/st25/base.tpl" %}
{% block content %}
      <h3 style="margin-top:3%">Члены команды</h1>
          {% for i in members %}
        {% include "team_member.tpl" ignore missing %}
    {% else %}
        <label>
            Команда пуста
        </label>
    {% endfor %}

              <hr style="margin-top:3%">
              <form  action = "{{selfurl}}/st5/load_from_file" method=POST>
        <br><input style="margin-top:1%" type=submit name="submit"value="Загрузить из файла">
</form>
              <form  action = "{{selfurl}}/st5/load_to_file" method=POST>
        <br><input style="margin-top:1%" type=submit name="submit"value="Сохранить в файл">
</form>
    <div style="margin-top:3%">
      {% include "form.tpl" ignore missing %}
      </div>
{% endblock %}