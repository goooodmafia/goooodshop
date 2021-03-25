FROM node:15.11.0-alpine3.13

ENV APP_ROOT /web

WORKDIR ${APP_ROOT}
ADD ./app/ ${APP_ROOT}

RUN apk add --no-cache --virtual .build-deps \
# alpine-sdk \
 make \
 g++ \
 python2 \
# && yarn install --production --cache-folder /dev/.ycache && rm -rf /dev/.ycache \
 && yarn install --production \
 && apk del .build-deps

#RUN apk --no-cache --virtual build-dependencies add \
#    python \
#    make \
#    g++ \
#    && npm install \
#    && apk del build-dependencies

##RUN apk add --no-cache --virtual .gyp \
##        python \
##        make \
##        g++ \
##    && yarn install \
##    && apk del .gyp

RUN yarn install
RUN yarn run build
CMD yarn run start