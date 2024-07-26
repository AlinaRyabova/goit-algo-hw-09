Опис домашнього завдання У конспекті ми розглянули приклад про розбиття суми на
монети. Маємо набір монет [50, 25, 10, 5, 2, 1]. Уявіть, що ви розробляєте
систему для касового апарату, яка повинна визначити оптимальний спосіб видачі
решти покупцеві.

Вам необхідно написати дві функції для касової системи, яка видає решту
покупцеві:

Функція жадібного алгоритму find_coins_greedy. Ця функція повинна приймати суму,
яку потрібно видати покупцеві, і повертати словник із кількістю монет кожного
номіналу, що використовуються для формування цієї суми. Наприклад, для суми 113
це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним,
тобто спочатку вибирати найбільш доступні номінали монет. Функція динамічного
програмування find_min_coins. Ця функція також повинна приймати суму для видачі
решти, але використовувати метод динамічного програмування, щоб знайти
мінімальну кількість монет, необхідних для формування цієї суми. Функція повинна
повертати словник із номіналами монет та їх кількістю для досягнення заданої
суми найефективнішим способом. Наприклад, для суми 113 це буде словник {1: 1, 2:
1, 10: 1, 50: 2} Порівняйте ефективність жадібного алгоритму та алгоритму
динамічного програмування, базуючись на часі їх виконання або О великому та
звертаючи увагу на їхню продуктивність при великих сумах. Висвітліть, як вони
справляються з великими сумами та чому один алгоритм може бути більш ефективним
за інший у певних ситуаціях. Свої висновки додайте у файл readme.md домашнього
завдання.

Як вони справляються з великими сумами?

Жадібний алгоритм працює дуже швидко, навіть для великих сум. Це обумовлено тим,
що він лише раз перевіряє кожен номінал монети та використовує максимальну
кількість кожної монети, поки не буде досягнута необхідна сума.

Приклад для суми 113: Жадібний алгоритм: {50: 2, 10: 1, 2: 1, 1: 1}

Час виконання для великих сум:

Сума: 1000, Час виконання: 0.000000 сек

Сума: 10000, Час виконання: 0.000000 сек

Сума: 50000, Час виконання: 0.000000 сек

Сума: 100000, Час виконання: 0.000000 сек

Жадібний алгоритм демонструє надзвичайно низький час виконання, навіть для
великих сум. Це пояснюється його лінійною складністю

Алгоритм динамічного програмування, хоча й гарантує мінімальну кількість монет
для будь-якої суми, значно повільніший на великих сумах. Це обумовлено тим, що
він перевіряє кожну можливу суму для кожного номіналу монети.

Приклад для суми 113: Алгоритм динамічного програмування: {50: 2, 10: 1, 2: 1,
1: 1}

Час виконання для великих сум:

Сума: 1000, Час виконання: 0.001992 сек

Сума: 10000, Час виконання: 0.103721 сек

Сума: 50000, Час виконання: 0.384972 сек

Сума: 100000, Час виконання: 0.373999 сек

Алгоритм динамічного програмування демонструє значно більший час виконання для
великих сум через його квадратичну складність

Порівняння ефективності

Жадібний алгоритм є дуже ефективним у термінах часу виконання та підходить для
стандартних наборів монет, де він зазвичай знаходить оптимальне рішення. Він є
найкращим вибором для великих сум завдяки його лінійній складності.

Алгоритм динамічного програмування гарантує оптимальне рішення для будь-якого
набору монет, але його квадратична складність робить його менш придатним для
великих сум. Він використовується в тих випадках, коли необхідно забезпечити
мінімальну кількість монет, і коли точність важливіша за продуктивність.

Висновок

Для стандартних наборів монет і великих сум жадібний алгоритм є більш ефективним
через його низьку часову складність. Алгоритм динамічного програмування, хоча й
забезпечує оптимальне рішення, є більш ресурсомістким і менш продуктивним для
великих сум.
