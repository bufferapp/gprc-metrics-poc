const onFinished = require('on-finished')
const BufferMetrics = require('./index')

/**
 * metricsMiddleware
 * Logging middleware which logs to stdout for metrics tracking
 *
 * @param {Object.<String>} name
 * @return {Function}
 */
module.exports = function metricsMiddleware ({ name }) {
  return function logMetrics (req, res, next) {
    req.buffermetrics = new BufferMetrics({ name })
    onFinished(res, () => req.buffermetrics.sendMetrics())
    next()
  }
}
