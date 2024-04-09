import streamlit as st

# Список элементов
filters = {
    'Выделение границ (Extract Edges)': 'Извлекает только граничные элементы из входных данных.',
    'Сглаживание (Smooth)': 'Применяет различные методы сглаживания к данным для уменьшения шумов и улучшения визуализации.',
    'Ресемплинг (Resample To Image)': 'Изменяет разрешение данных путем ресемплинга на новую сетку.',
    'Объединение (Append)': 'Объединяет несколько наборов данных в один.',
    'Интегрирование (Integrate Variables)': 'Вычисляет интегралы данных вдоль определенных направлений.',
    'Объемный выделитель (Volume Selector)': 'Выделяет определенные области в объемных данных для дальнейшего анализа.',
    'Проекция на плоскость (Project On Plane)': 'Проецирует данные на плоскость для упрощения визуализации.',
    'Разбиение на блоки (Block Splitting)': 'Разбивает данные на блоки для обработки на параллельных архитектурах.',
    'Градиент (Gradient)': 'Вычисляет градиенты данных для анализа направления изменения значений.',
    'Камера (Camera)': 'Управляет положением и ориентацией камеры для создания определенных видов.',
    'Извлечение краев (Extract Boundary Cells)': 'Извлекает только граничные ячейки из объемных данных.',
    'Производные (Divergence, Curl)': 'Вычисляет производные данных для анализа потоков и вихрей.',
}
f_images = {
    "41" : ["Contour","Извлекает точки, кривые или поверхности, скалярное поле которых равно определяемому пользователем значению. Эту поверхность часто также называют изоповерхностью."],
    "42" : ["Clip","Пересекает геометрию полупространством. В результате вся геометрия удаляется с одной стороны пользовательской плоскости."],
    "43" : ["Slice","Пересекает геометрию плоскостью. Эффект аналогичен обрезке, за исключением того, что остается только геометрия, в которой расположена плоскость."],
    "44" : ["Threshold","Извлекает ячейки, которые находятся в пределах заданного диапазона скалярного поля."],
    "45" : ["Extract Subset","Извлекает подмножество сетки, определяя либо интересующий объем, либо частоту дискретизации."],
    "46" : ["Glyph","Помещает глиф простой формы в каждую точку сетки. Глифы могут быть ориентированы по вектору и масштабироваться с помощью вектора или скаляра."],
    "47" : ["Stream Tracer","Заполняет векторное поле точками, а затем прослеживает эти начальные точки через векторное поле (стационарное)."],
    "48" : ["Warp (vector)","Смещает каждую точку сетки на заданное векторное поле."],
    "49" : ["Group Datasets","Объединяет выходные данные нескольких объектов конвейера в единый многоблочный набор данных."],
    "410" : ["Extract Level","Извлеките один или несколько элементов из многоблочного набора данных."],
}

# Заголовок страницы
st.title('Фильтры')

st.write('**Фильтры** - это инструменты для обработки и преобразования данных перед их визуализацией. Они предназначены для выполнения различных операций над данными с целью подготовки их к анализу или визуализации.')
st.write('К некоторым фильтрам есть быстрый доступ в панели инструментов:')
for file_, filter in f_images.items():
    if file_=="49":
        image = open(f'pages/img/{file_}.svg', 'rb').read()
        st.image(image,end='')
        st.write(f"**{filter[0]}:** {filter[1]}")

st.write("Но в панели **Filters** есть и некоторые другие:")

# Отображение списка элементов
for filter_name, filter_description in filters.items():
    st.write(f'**{filter_name}:** {filter_description}')
