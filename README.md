# Монторинг приложения в kubernetes
* Создаем кластер в GCP
* Устанавливаем ingress контроллер
 `helm install nginx-ingress ingress-nginx/ingress-nginx --create-namespace --namespace ingress-nginx`
 * Устанвливаем istio
 * Устанавливаем аддоны для istio: prometeus, grafana
 * Собираем docker образ и деплоим манифесты в кубер
 * Настраиваем дашборд и алерт в grafana