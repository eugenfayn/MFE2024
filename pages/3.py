import streamlit as st

def show_ozn():
    st.title("Ознакомление с Интерфейсом")
    st.write("""
После запуска ParaView перед вами откроется главное окно программы, состоящее из нескольких ключевых областей:
    """)
    st.markdown("""
- **Панель инструментов (Toolbar):**
Содержит кнопки для выполнения часто используемых команд, таких как открытие файла, сохранение сцены и запуск визуализации.
- **Область объектов (Pipeline Browser):** 
Показывает структуру вашей визуализационной сессии, включая загруженные наборы данных и примененные фильтры.
- **Область свойств (Properties):** 
Здесь отображаются параметры для выбранного в Pipeline Browser объекта или фильтра. Это может быть, например, выбор компоненты векторного поля для визуализации или настройка параметров фильтра.
- **Основная область визуализации (Render View):** 
Здесь отображается результат ваших визуализаций. Вы можете взаимодействовать с этой областью, используя мышь, для вращения, масштабирования и перемещения сцены.
""")
    image = open('pages/pics/3.png', 'rb').read()

    # Вставка изображения
    st.image(image, use_column_width=True)

def show_import():
    st.title("Импорт и Подготовка Данных")
    st.markdown("""
- **1.	Выберите "File" -> "Open" и найдите файл данных, который хотите визуализировать. ParaView поддерживает множество форматов данных.**
- **2.	После открытия файла, выбранный набор данных появится в области Pipeline Browser. В этот момент данные загружены, но еще не визуализированы.** 
- **3.	Нажмите кнопку "Apply" в области Properties, чтобы отобразить данные в основной области визуализации. В зависимости от типа данных, ParaView автоматически выберет базовый метод визуализации.** 
""")


def show_filtr():
    st.title("Применение Фильтров")
    st.write("""
ParaView предоставляет множество фильтров для обработки и анализа данных:
    """)
    st.markdown("""
- **1.	С выбранным в Pipeline Browser набором данных, перейдите в меню "Filters" для просмотра доступных фильтров.**
- **2.	Выберите нужный фильтр, настройте его параметры в области Properties и нажмите "Apply" для применения.** 
- **3.	Примененный фильтр появится в Pipeline Browser как новый объект, связанный с исходными данными.** 
""")

def show_viz():
    st.title("Настройка Визуализации")
    st.write("""
После импорта данных и применения фильтров вы можете настроить визуализацию:
    """)
    st.markdown("""
- **Изменение способа визуализации:**
В области Properties вы можете изменить тип визуализации (например, на изолинии, стримлайны или объемную визуализацию) для выбранного объекта.
- **Настройка внешнего вида:** 
Здесь же можно настроить цвета, прозрачность и другие параметры визуализации, чтобы лучше выделить важные аспекты данных.
""")

def show_analiz():
    st.title("Анализ и Интерпретация")
    st.write("""
Пользуйтесь инструментами ParaView для детального анализа и исследования данных:
    """)
    st.markdown("""
- **Интерактивное исследование:**
Используйте мышь для вращения, масштабирования и перемещения визуализации в пространстве, что позволит вам изучить данные с разных сторон и под разными углами.
- **Измерение и количественный анализ:** 
ParaView предлагает инструменты для измерения расстояний, площадей, а также другие средства для количественного анализа данных. Эти функции могут быть особенно полезными для технического анализа и оценки параметров ваших исследований.
- **Создание аннотаций и маркеров:**
Добавление текстовых аннотаций, маркеров и легенд поможет сделать ваши визуализации более понятными для других пользователей, а также облегчит интерпретацию результатов.
""")

# Создание боковой панели для навигации по разделам
st.sidebar.title("Основы работы с Paraview")
page = st.sidebar.radio("Выберите страницу:", ("Ознакомление с Интерфейсом", "Импорт и Подготовка Данных", "Применение Фильтров","Настройка Визуализации","Анализ и Интерпретация" ))

if page == "Ознакомление с Интерфейсом":
    show_ozn()

elif page == "Импорт и Подготовка Данных":
    show_import()
elif page == "Применение Фильтров":
    show_filtr()
elif page == "Настройка Визуализации":
    show_viz()
elif page == "Анализ и Интерпретация":
    show_analiz()
