# buffer-js-buffermetrics

[![Build Status](https://travis-ci.com/bufferapp/buffer-js-buffermetrics.svg?token=McM3TsXQL9Hf6QBax2tf&branch=master)](https://travis-ci.com/bufferapp/buffer-js-buffermetrics)

A Node.js library for logging metrics with Express.js middleware.

## Usage

### Install

```
npm install @bufferapp/buffermetrics -SE
```

### Express Middleware

When creating the middleware, give it a `name`. This is used to tag each event's
source.

```js
const buffermetricsMiddleware = require('@bufferapp/buffermetrics')
const app = express()

app.use(buffermetricsMiddleware({ name: 'Marketing-Site' }))
```

Now in other requests or middleware you can use the `BufferMetrics` library's
methods:

```js
app.get('/welcome', (req, res) => {
  req.buffermetrics.trackVisit(req)
  res.render('welcome')
})
```

If you want to add additional metadata (ex. visitor data) for each request,
you should create your own middleware to automatically append this data and
even track all visits:

```js
app.use(buffermetricsMiddleware({ name: 'Marketing-Site' }))
app.use((req, res, next) => {
  req.buffermetrics.setMetadata({ visitor_id: req.session.visitor_id })
  req.buffermetrics.trackVisit(req)
  next()
})
app.get('/welcome', (req, res) => {
  res.render('welcome')
})
```
