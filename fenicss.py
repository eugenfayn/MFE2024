import streamlit as st
from main import wrap
wrap()

st.title('FEniCS')

image = open('pages/img/fee.png', 'rb').read()
st.image(image, use_column_width=True)

st.write('FEniCS — это популярная и мощная вычислительная платформа с открытым исходным кодом для автоматизации решения дифференциальных уравнений, особенно уравнений в частных производных (УЧП), с помощью метода конечных элементов (МКЭ). Он разработан для обеспечения высокопроизводительного моделирования и легко интегрируется с другими научными библиотеками.')
st.header('1. Автоматизация процесса решения УЧП:')

st.write('FEniCS позволяет исследователям и инженерам описывать математические модели напрямую в терминах дифференциальных уравнений.')
st.write('Использует специализированный язык определения уравнений, который позволяет вводить уравнения в форме, очень близкой к математической записи.')
st.header('2. Генерация и оптимизация кода:')

st.write('Отличительной особенностью FEniCS является автоматическая генерация оптимизированного и компилируемого кода из высокоуровневых описаний математических моделей.')
st.write('Это позволяет использовать высокоуровневые абстракции, в то же время получая эффективные и быстрые вычислительные алгоритмы.')
st.header('3. Модульность и расширяемость:')

st.write('FEniCS состоит из нескольких взаимосвязанных компонентов, таких как DOLFIN для вычислительных интерфейсов и UFL (язык формулирования уравнений) для определения уравнений.')
st.write('Платформа позволяет легко интегрировать пользовательские модули и библиотеки для расширения функциональности.')
st.header('4. Совместимость с другими пакетами:')

st.write('FEniCS может быть легко интегрирован с другими математическими и вычислительными пакетами, такими как NumPy, SciPy, и Matplotlib для анализа данных и визуализации.')
st.header('5. Применения:')

st.write('Он применяется в самых разнообразных областях, включая механику сплошных сред, электромагнетизм, биомеханику и многие другие.')
st.title('Процесс работы с FEniCS:')
st.header('1. Моделирование:')

st.write('Разработка математической модели задачи и её перевод в язык, понятный для FEniCS (например, в UFL).')
st.header('2. Сетка:')

st.write('Создание или импорт сетки, на которой будет решаться задача. Сетка делит область на конечные элементы.')
st.header('3. Решение:')

st.write('Реализация численных методов для приближенного решения УЧП. Вычисление решений на каждом конечном элементе сетки.')
with st.expander("Код"):
    st.code("""from dolfin import *
from matplotlib import pyplot
parameters["plotting_backend"] = "matplotlib"
mesh2D = UnitSquareMesh( 16 , 16 )
mesh3D = UnitCubeMesh( 16 , 16 , 16 )
plot(mesh2D)
plot(mesh3D)
pyplot.show ()""")
image = open('pages/pics/mesh.jpg', 'rb').read()

    # Вставка изображения
st.image(image, use_column_width=True)
st.header('4. Постобработка:')

st.write('Анализ полученных решений и их визуализация, возможно, с использованием сторонних инструментов, таких как Paraview.')
st.header('5. Валидация:')

st.write('Проверка корректности решения путём сравнения с аналитическими решениями или экспериментальными данными.')

