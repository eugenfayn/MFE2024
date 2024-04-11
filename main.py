import streamlit as st
from st_pages import Page, show_pages, add_page_title

def main():
        st.set_page_config(
                page_title='ParaView',
                page_icon='🔮',
        )
        page_bg = """
        <style>
        [data-testid="stSidebarContent"]{
        background-color: #ffffff;
        opacity: 0.4;
        background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #ffffff 40px ), repeating-linear-gradient( #c9a9a955, #c9a9a9 );
        }
        </style>
        """
        # Заголовок страницы
        # Подзаголовок
        st.markdown(page_bg,unsafe_allow_html=True)
        st.title('ParaView')


        st.header('Проект 4. ParaView. ')

        show_pages(
         [
            Page("main.py", "Введение", "🧊"),
            Page("base_info.py", "Общая_характеристика", "🧊"),
            Page("prep_data.py", "Подготовка данных для визуализации", "🧊"),
            Page("get_start.py", "Основы работы ParaView", "🧊"),
            Page("filters.py", "Фильтры", "🧊"),           
            Page("2D.py", "Обработка двухмерных данных", "🧊"),
            Page("3D.py", "Визуализация трёхмерных данных", "🧊"),
            Page("timee.py", "Анимация нестационарных данных", "🧊"),
            Page("fenicss.py", "FEniCS", "🧊"),
            Page("add_info.py", "Другие возможности ParaView", "🧊"), 
         ]
        )  
        

        st.subheader('Работу выполнили студенты МГУ Саров из группы ВМ-123:')
        st.write('''
                - Устюжанин Илья :sunglasses:
                - Файн Евгений :sunglasses:
                - Шапаренко Владислав :sunglasses:
                - Хасанов Максим 👟
                ''')

if __name__ == "__main__":
    main()
