import streamlit as st
from st_pages import Page, show_pages, add_page_title



st.sidebar.title("Paraview для чайников")
# Заголовок страницы
st.title('ParaView')

# Подзаголовок
st.header('Проект 4')

# Участники
st.subheader('Работу выполнили студенты МГУ Саров из группы ВМ-123:')
st.write('''
- Устюжанин Илья :sunglasses:
- Файн Евгений :sunglasses:
- Шапаренко Владислав :sunglasses:
- Хасанов Максим 👟
''')
