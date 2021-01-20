# Use the nginx image
FROM nginx

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf 

# Replace with your own nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf 