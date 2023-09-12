# Delivery Cost

### Скрипт для расчета стоимости доставки и добавления ее в заказ в сервисе "Мой склад"
<br><br>
Используемые технологии: `Python 3`, библиотека `Requests`, `API "Мой склад"` <br>
Автор: Евгения Псарева<br>
Контакты: epsareva77@gmail.com<br><br>

## Функционал

1. Скрипт считает стоимость доставки товаров из заказа по формуле `масса/объем*500`
1. Добавляет в заказ услугу «Доставка» в количестве 1 шт и рассчитанной стоимостью


## Взаимодействие с проектом
1. Откройте заказ в Моем складе <https://online.moysklad.ru/app/#customerorder>. В заказе уже содержатся 3 товара.
1. Скачайте скрипт из этого репозитория. Убедитесь, что у вас установлен `Python` и библиотека `Requests`
1. Выполните его в терминале `python3 script.py`
1. Снова откройте заказ или обновите страницу. К заказу добавится услуга "Доставка" в кооличестве 1 и и рассчитанной стоимостью
