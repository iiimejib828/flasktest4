from flask import render_template, request, redirect, url_for

from app import app

friends = []

@app.route("/", methods=["GET", "POST"])

def index():
#использует метод POST, так как информация будет отправляться. Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
    #функция request.form извлекает значение из соответствующих полей
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        #создаёт условие для проверки наличия данных в полях name и content
        if name and age and hobby and city:
            friends.append({'name': name, 'age': age, 'city': city, 'hobby': hobby})
        #использует для обновления страницы и предотвращения повторной отправки формы.
        return redirect(url_for('index'))
        #возвращает отрендеренный шаблон с переданными данными постов
    return render_template('friendlist.html', friends=friends)