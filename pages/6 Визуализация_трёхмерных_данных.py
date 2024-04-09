import streamlit as st

st.title('Визуализация трехмерных данных')
st.write('Трёхмерные данные визуализируются аналогично')
st.markdown("""
1. Импорт данных:  Это может быть файл данных в формате VTK, STL, PLY, OBJ, и других форматах, поддерживаемых ParaView.

2. Построение сетки:  Необходимо построить или загрузить сетку.

3. Применение фильтров:  Используйте фильтры, чтобы обрабатывать и визуализировать данные, такие как фильтры сглаживания, выделения определенных областей интереса, векторное поле и другие.

4. Настройка визуализации:  Настройка параметров визуализации, таких как цвет, прозрачность, размер, форма, отображение осей и других параметров.

5. Анимация данных:  Если данные имеют временную зависимость, можно создать анимацию для визуализации изменений данных со временем.

6. Анализ результатов:  Оценка визуализации и анализ результатов.

""")

#st.video('C:\ParaView\Gif 2.mp4', caption='Local Video')

video_file = open('pages/img/volcano.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes,caption='Пример анимации вулканического дыма')
