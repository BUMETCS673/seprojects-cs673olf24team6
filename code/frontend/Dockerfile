FROM node:14

WORKDIR /src

COPY . /src

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 9000

CMD ["npm", "start"]