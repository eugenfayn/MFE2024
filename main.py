import streamlit as st
from st_pages import Page, show_pages, add_page_title

def main():
        st.set_page_config(
                page_title='ParaView',
                page_icon='🔮',
        )
        st.sidebar.title("Paraview для чайников")
        # Заголовок страницы
        st.title('ParaView')

        # Подзаголовок
        st.header('Проект 4. ParaView. ')



        show_pages(
         [
            Page("main.py", "Введение", "🏠"),
            Page("base_info.py", "Общая_характеристика", ":flag-np:"),
            Page("prep_data.py", "Подготовка данных для визуализации", ":one:"),
            Page("get_start.py", "Основы работы ParaView", ":one:"),
            Page("filters.py", "Фильтры", ":one:"),           
            Page("2D.py", "Обработка двухмерных данных", ":one:"),
            Page("3D.py", "Визуализация трёхмерных данных", ":two:"),
            Page("timee.py", "Анимация нестационарных данных", ":three:"),
            Page("fenicss.py", "FEniCS", ":four:"),
            Page("add_info.py", "Другие возможности ParaView", ":one:"), 
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

if __name__ == "__main__":
    main()
