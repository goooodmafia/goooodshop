FROM node:15.11.0-alpine3.13 as builder

ENV APP_ROOT /app
ENV NODE_ENV=production

WORKDIR ${APP_ROOT}
#ADD ./app/ ${APP_ROOT}

ADD ./app/package.json ./app/yarn.lock ./

RUN apk add --no-cache --virtual .build-deps \
    # alpine-sdk \`
    make \
    g++ \
    python2 \
    # && yarn install --production --cache-folder /dev/.ycache && rm -rf /dev/.ycache \
    # && yarn install --production \
    && yarn --frozen-lockfile --non-interactive && yarn cache clean \
    && apk del .build-deps




#RUN  apk add --no-cache curl git \
#    && cd /tmp \
#    && curl -#L https://github.com/tj/node-prune/releases/download/v1.0.1/node-prune_1.0.1_linux_amd64.tar.gz | tar -xvzf- \
#    && mv -v node-prune /usr/local/bin && rm -rvf * \
#    && echo "yarn cache clean && node-prune" > /usr/local/bin/node-clean \
#    && chmod +x /usr/local/bin/node-clean

#ADD package.json yarn.lock ./
#RUN yarn --frozen-lockfile --non-interactive && node-clean

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

#RUN yarn install
#RUN yarn build
#CMD yarn run start
#CMD yarn run dev

ADD ./app/ ${APP_ROOT}
RUN yarn run build

FROM node:15.11.0-alpine3.13
WORKDIR ${APP_ROOT}
ENV NODE_ENV=production
ADD ./app/package.json ./
ADD ./app/nuxt.config.js ./
COPY --from=builder ./app/node_modules ./node_modules/
COPY --from=builder ./app/modules ./modules/
COPY --from=builder ./app/.nuxt ./.nuxt/
#COPY --from=builder ./app/static ./static/

CMD yarn run start