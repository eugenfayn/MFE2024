import streamlit as st
from st_pages import Page


st.sidebar.title("Paraview для чайников")
# Заголовок страницы
st.title('ParaView')

# Подзаголовок
st.header('Проект 4. ParaView. ')

from st_pages import Page, show_pages, add_page_title

show_pages(
        [
           Page("main.py", "Введение", "🏠"),
           Page("pages/base_info.py", "Общая_характеристика", ":flag-np:"),
           Page("pages/prep_data.py", "Подготовка данных для визуализации", ":one:"),
           Page("pages/get_start.py", "Основы работы ParaView", ":one:"),
           Page("pages/filters.py", "Фильтры", ":one:"),           
           Page("pages/2D.py", "Обработка двухмерных данных", ":one:"),
           Page("pages/3D.py", "Визуализация трёхмерных данных", ":two:"),
           Page("pages/timee.py", "Анимация нестационарных данных", ":three:"),
           Page("pages/fenicss.py", "FEniCS", ":four:"),
           Page("pages/add_info.py", "Другие возможности ParaView", ":one:"), 
        ]
)  

# Участники
st.subheader('Работу выполнили студенты МГУ Саров из группы ВМ-123:')
st.write('''
- Устюжанин Илья :sunglasses:
- Файн Евгений :sunglasses:
- Шапаренко Владислав :sunglasses:
- Хасанов Максим 👟
''')
