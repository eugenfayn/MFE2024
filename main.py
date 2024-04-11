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
           Page("base_info.py", "Общая_характеристика", ":flag-np:"),
           Page("numpy_creation.py", "Создание массивов", ":one:"),
           Page("numpy_operations.py", "Операции в NumPy", ":two:"),
           Page("numpy_linear_algebra.py", "Линейная алгебра", ":three:"),
           Page("numpy_polynomials.py", "Работа с полиномами", ":four:"), 
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
