<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"crossorigin="anonymous"></script>

{% include "asm2204/st25/header.tpl" ignore missing %}
<center>
{{s}} {{selfurl}}
<br>
<br><a href="/">Return</a>

{% block content %} {% endblock %}</center>

{% include "asm2204/st25/footer.tpl" ignore missing %}