# sea_battle

Добрый день!

В данный момент есть две версии Морского боя.

sea_battle - версия, которая работает, но код функций расстановки кораблей, проверки окрестностей и стрельбы сильно неоптимизированны, много дублирующего кода. 
В целом предварительная проверка показала, что игра работает как задумано 

sea_battle_v2 - я переписал функции добавления кораблей, они стали намного лаконичнее и надеюсь понятнее. К сожалению, не успел отладить, работает с ошибками.
Хотел отметить, что первоначально поле заполняется символами "о" о маленькое, и в процессе расстановки кораблей окрестности меняются на "О" большое. Для того, чтобы избежать дополнительных проверок на близость кораблей во время расстановки.

Также поле генерируется шире не 6, а 8 клеток. Для того, чтобы избежать лишних проверок при расстановки кораблей и отображения окрестностей когда они затонули. Но отрисовка происходит 6 на 6 как и требуется.
