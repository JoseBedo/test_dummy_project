FROM node:16.13.1
WORKDIR /usr/src/holistiqumweb/

COPY --chown=node:node package.json .
COPY --chown=node:node package-lock.json .

ARG REACT_APP_IS_PRODUCTION
ENV REACT_APP_IS_PRODUCTION=$REACT_APP_IS_PRODUCTION

RUN npm install
RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache


COPY --chown=node:node . .

USER node

EXPOSE 3000

CMD [ "npm", "start" ]