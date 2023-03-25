# Монторинг приложения в kubernetes
* Создаем кластер в GCP
* Устанавливаем ingress контроллер
 `helm install nginx-ingress ingress-nginx/ingress-nginx --create-namespace --namespace ingress-nginx`
 * Устанвливаем istio
 * Устанавливаем аддоны для istio: prometeus, grafana
 * Собираем docker образ (app/Dockerfile) и деплоим манифесты (kuber/*) в кубер
 * Настраиваем дашборд и алерт в grafana

 Пример дашборда показывающего статистику http ответов:
 ![grafana](grafana.png)

 Пример сработавшего алерта:
 ![grafana](alert.png)

 ### #TODO
 * Разработать разворачивание кубера на terraform
 * Автоматизировать разворачивание сервисов в кубер
 * Настроить мониторинг средствами обака (Metrics Explorer в GCP)