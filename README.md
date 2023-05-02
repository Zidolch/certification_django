Пользователь стандартный, требуется создать админа командой
`python manage.py createsuperuser` \
сборка контейнера с приложением:
`docker-compose build`
`docker-compose up -d`

Приложение с элементами сети поставок расположено в `./suppliers_network`,
Вся иерархия реализована в виде одной модели `NetworkObject`