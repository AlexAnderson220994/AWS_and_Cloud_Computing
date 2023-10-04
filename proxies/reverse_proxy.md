# Reverse proxies

## What is a proxy?

- A proxy server is an intermediate server that acts as a gateway between client devices and target servers or services, forwarding requests and responses.
- Proxies sit between client devices (such as computers or smartphones) and target servers (websites or other services).
- They serve as intermediaries, facilitating communication between clients and servers.

## What is a reverse proxy?

- A reverse proxy is a server or software application that sits between client devices (such as web browsers) and one or more backend servers (web servers, application servers, or other services).
- Unlike a forward proxy, which is used by clients to access the internet indirectly, a reverse proxy is used by backend servers to handle client requests.

## Steps on how to set up reverse proxy

1) Navigate to the configuration file where the reverse proxy settings are defined.
````
sudo nano /etc/nginx/sites-available/default
````
2) Inside the opened file, navigate to the "Server" and "Location" sections
3) Change the settings as below:
````
server {
    listen 80;
    server_name your_app_vm_ip;

    location / {
        proxy_pass http://your_app_server_ip:your_app_port;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
````
4) Your public IP goes in both server and location. The port just goes in location.
5) Save the file and exit the text editor.
6) Test the nginx configuration with:
````
sudo nginx -t
````
7) Restart nginx:
````
sudo system restart nginx
````
8) Restart the app (make sure you've navigated to the app folder)
````
node app.js
````
