yandex-client
=============

Simply GUI interface for yandex-disk synchronisation

Простой GUI-интерфейс для просмотра статуса синхронизации с яндекс диском для Ubuntu

Порядок установки:

1. Скачиваем отсюда нужную версию консольного клиента яндекс-диска:
http://help.yandex.ru/disk/cli-clients.xml#cli-setup

2. Открываем терминал, выполняем:
sudo yandex-disk setup

3. Следуя указаниям установщика, настраиваем яндекс-диск.

4. Создаем папку, куда хотим установить GUI.

5. Копируем туда три файла из репозитория.

6. Открываем терминал, выполняем:
sudo apt-get install python-qt4

7. Не закрываем терминал, переходим в созданную в шаге 4 папку.

8. Выполняем в терминале:
python yandex_disk_tray.py

9. Наслаждаемся видом значка яндекс-диска в трее и менюшки :)
