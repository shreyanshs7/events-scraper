FROM node:16-slim

WORKDIR /usr/src/app/events_frontend

COPY package*.json ./

RUN npm install -g @angular/cli @angular-devkit/build-angular && npm install

EXPOSE 4200

CMD ["ng", "serve"]