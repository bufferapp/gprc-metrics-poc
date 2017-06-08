// const path = require('path')
const grpc = require('grpc')
const uuidV4 = require('uuid/v4')
const useragent = require('useragent')
const { MetricsCollectorClient } = require('./proto/collector_grpc_pb')
const {
  Visit,
  Utm,
  UserAgent
} = require('./proto/collector_pb')
const {
  capFirst,
  removeTokensFromUrl
} = require('./lib/utils')

class BufferMetrics {

  /**
   * constructor
   */
  constructor ({ host, name, debug }) {
    this.host = host || 'localhost:50051'
    this.eventSource = name
    this.debug = debug || false
    this.client = new MetricsCollectorClient(this.host, grpc.credentials.createInsecure())
  }

  setMetadata (metadata = {}) {
    this.metadata = this.sanitizeMetadata(metadata)
  }

  /**
   * sanitizeMetadata
   * Filters out any invalid metadata parameters
   */
  sanitizeMetadata (rawMetadata = {}) {
    const validMetadata = ['visitor_id', 'experiments']
    const metadata = {}
    validMetadata.forEach((key) => {
      if (rawMetadata.hasOwnProperty(key)) {
        metadata[key] = rawMetadata[key]
      }
    })
    return metadata
  }

  getEvents () {
    return this.events
  }

  /**
   * getBaseEventData
   * The fields that must be logged for each event
   */
  getBaseEventData () {
    return {
      buffermetrics: true,
      timestamp: new Date()
    }
  }

  /**
   * appendMetadataToEvent
   * Adds core metadata to the event
   */
  appendMetadataToEvent (baseData, event) {
    return Object.assign({}, event, this.metadata, baseData)
  }

  //
  sendMetrics () {

  }

  clientResponseHandler (err, res) {
    if (err) {
      process.stderr.write(`Error tracking metric: ${err.message}`)
    } else if (this.debug) {
      console.log(res)
      process.stdout.write(`Tracked metric`)
    }
  }

  /**
   * trackVisit
   * Track a page visit given a http.Request object and extra meta data
   */
  trackVisit (req) {
    const v = new Visit()
    v.setId(uuidV4())
    v.setUri(removeTokensFromUrl(req.url))
    v.setIp(req.headers['x-forwarded-for'] || req.connection.remoteAddress)

    const utm = new Utm()
    const utmParams = ['source', 'medium', 'campaign', 'content']
    utmParams.forEach(key => utm[`set${capFirst(key)}`](req.query[`utm_${key}`]))
    v.setUtm(utm)

    const parsedUA = useragent.parse(req.headers['user-agent'])
    const ua = new UserAgent()
    ua.setBrowser(parsedUA.family)
    ua.setVersion(parsedUA.major)

    this.client.trackVisit(v, this.clientResponseHandler.bind(this))
  }

}

module.exports = BufferMetrics
