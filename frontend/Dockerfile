FROM node:20-alpine

WORKDIR /app
COPY package*.json ./

RUN npm install

COPY . .

RUN npm i express dotenv

CMD ["node", "server.js"]