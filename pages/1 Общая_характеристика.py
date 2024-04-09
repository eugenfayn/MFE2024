import streamlit as st

def show_title():
    st.title("Paraview")
# st.image('path_to_image.png', caption='Описание изображения')
# Функция для отображения раздела "Общая характеристика ПО"
def show_overview():
    st.title("Общая характеристика ПО")
    image = open('pages/img/1.png', 'rb').read()

    # Вставка изображения
    st.image(image, use_column_width=True)
    st.write()
    st.write("""
        ParaView :sunglasses: - это свободно распространяемое программное обеспечение для визуализации данных. Оно используется в различных областях, таких как научные исследования, инженерное моделирование, медицинская диагностика и другие. ParaView предоставляет мощные инструменты для визуализации и анализа различных типов данных, таких как трехмерные модели, объемные данные, изображения и графики.
    """)
    st.subheader("Ключевые характеристики")
    st.markdown("""
- **Открытый исходный код и кроссплатформенность:**
Одной из основных характеристик ParaView является его открытый исходный код, что позволяет сообществу пользователей и разработчиков свободно модифицировать и расширять функциональность программы. ParaView поддерживает основные операционные системы, включая Windows, macOS и Linux, обеспечивая широкий доступ к программе.
- **Масштабируемость и распределённая обработка:** 
ParaView спроектирован для эффективной работы с очень большими объемами данных, которые часто возникают в результате комплексных научных расчетов и симуляций. Благодаря поддержке распределённой обработки данных, ParaView может использоваться для визуализации результатов, полученных на кластерах и суперкомпьютерах, распределяя задачи и ресурсы между множеством вычислительных узлов.
- **Гибкая система визуализации:** 
ParaView предоставляет пользователям широкий спектр инструментов и методик визуализации, таких как объемная рендеринг, визуализация векторных и тензорных полей, изосурфейсы, потоковые линии и многое другое. Это делает ParaView универсальным инструментом для визуализации данных из различных научных дисциплин.
- **Поддержка множества форматов данных:** 
ParaView может работать с разнообразными форматами данных, что облегчает его интеграцию в различные научные и инженерные рабочие процессы. Программа поддерживает популярные форматы, такие как NETCDF, HDF5, а также специализированные форматы, используемые в конкретных областях науки и техники.
- **Интерактивность и автоматизация:** 
ParaView предлагает интерактивный графический интерфейс, который позволяет пользователям легко создавать сложные визуализации, а также адаптировать и изменять их в реальном времени. Кроме того, поддержка скриптов на языке Python открывает возможности для автоматизации задач и разработки пользовательских расширений.

""")

# Функция для отображения раздела "Подготовка данных для визуализации"
def show_data_preparation():
    st.title("2 Подготовка данных для визуализации")
    st.write("""
ParaView поддерживает множество различных форматов данных, включая CSV, JSON, XML, различные форматы изображений, а также специализированные форматы, применяемыми в научных и инженерных исследованиях, например, VTK, VTU, VTP, NETCDF, и HDF5.
Зачастую перед импортом в ParaView требуется предварительная обработка данных. Это может включать:
    """)
    st.markdown("""
- **Очистку данных:**
Удаление шума, исправление ошибок или удаление ненужных частей данных.
- **Преобразование данных:** 
Конвертация данных в формат, оптимально подходящий для визуализации в ParaView. Например, преобразование табличных данных в формат CSV или бинарные данные в формат VTK.
- **Нормализация данных::** 
Приведение всех измерений к общей шкале, что особенно важно при сравнении различных наборов данных.
- **Расчет производных величин:** 
Возможно, для анализа потребуются не только исходные данные, но и производные величины, такие как градиенты, вихри или другие физические величины.
""")

# Функция для отображения раздела "Основы работы с Paraview"
def show_paraview_basics():
    st.title("Основы работы с Paraview")


show_title()


show_overview()

