
# Utilisation de l'image NGINX comme base
FROM nginx:alpine
# Copier le fichier index.html dans le conteneur
COPY index.html /usr/share/nginx/html/index.html
# Exposer le port 80
EXPOSE 80
# Lancer NGINX
CMD ["nginx", "-g", "daemon off;"]