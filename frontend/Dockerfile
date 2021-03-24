FROM node:15.11.0-alpine3.13

ENV APP_ROOT /web

WORKDIR ${APP_ROOT}
ADD ./app/ ${APP_ROOT}

RUN yarn install
RUN yarn run build
CMD yarn run start