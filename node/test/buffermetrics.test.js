/* global jest describe test expect */
const BufferMetrics = require('../index')

describe('constructor', () => {
  test('it should instantiate', () => {
    const buffermetrics = new BufferMetrics({ name: 'Test' })
    expect(buffermetrics).toBeInstanceOf(BufferMetrics)
  })
})

describe('sanitizeMetadata', () => {
  test('allow only valid metadata fields', () => {
    const m = new BufferMetrics({ name: 'Test' })
    const sanitizedMetadata = m.sanitizeMetadata({
      visitor_id: '1234',
      somethingInvalid: 'test'
    })
    expect(sanitizedMetadata).toMatchObject({
      visitor_id: '1234'
    })
  })
})

describe('getEvents', () => {
  test('returns an array ', () => {
    const m = new BufferMetrics({ name: 'Test' })
    expect(m.getEvents()).toBeInstanceOf(Array)
  })
})

describe('getBaseEventData', () => {
  test('include minimum data for logging', () => {
    const m = new BufferMetrics({ name: 'Test' })
    const d = m.getBaseEventData()
    expect(d.buffermetrics).toBe(true)
    expect(d).toHaveProperty('timestamp')
  })
})

describe('transformEventsForStream', () => {
  const events = [
    { type: 'Visit', referrer: 'https://buffer.com' },
    { type: 'TestType', field: 'value' }
  ]

  test('returns  string', () => {
    const m = new BufferMetrics({ name: 'Test' })
    const eventsForStream = m.transformEventsForStream(events)
    expect(typeof eventsForStream).toBe('string')
  })

  test('formats events as separate json log lines', () => {
    const m = new BufferMetrics({ name: 'Test' })
    const eventsForStream = m.transformEventsForStream(events)
    const lines = eventsForStream.split('\n')
    expect(lines).toHaveLength(2)

    const parsedEvent1 = JSON.parse(lines[0])
    const parsedEvent2 = JSON.parse(lines[1])
    expect(parsedEvent1.buffermetrics).toBe(true)
    expect(parsedEvent1).toHaveProperty('timestamp')
    expect(parsedEvent1.type).toBe('Visit')
    expect(parsedEvent1.referrer).toBe('https://buffer.com')
    expect(parsedEvent2.buffermetrics).toBe(true)
    expect(parsedEvent2).toHaveProperty('timestamp')
    expect(parsedEvent2.type).toBe('TestType')
    expect(parsedEvent2.field).toBe('value')
  })
})

describe('writeEvents', () => {
  test('should write to the given stream successfully', () => {
    const fakeStream = { write: jest.fn() }
    const m = new BufferMetrics({ name: 'Test', writeStream: fakeStream })
    const events = [
      { type: 'Visit', referrer: 'https://buffer.com' }
    ]
    // NOTE - We may not want to test using an internal property in this way - DF
    m.events = events
    m.writeEvents()
    expect(typeof fakeStream.write.mock.calls[0][0]).toBe('string')
    expect(fakeStream.write.mock.calls[0][0]).toMatch(/"type":"Visit"/)
  })
})

describe('trackVisit', () => {
  test('event contains correct parameters', () => {
    const m = new BufferMetrics({ name: 'Test' })
    const fakeRequest = {
      url: 'https://buffer.com/test',
      headers: {
        'x-forwarded-for': '204.148.13.62',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
      },
      connection: { remoteAddress: '172.0.0.1' },
      query: { utm_source: 'social' }
    }
    m.trackVisit(fakeRequest)

    expect(m.getEvents()).toHaveLength(1)

    const e = m.getEvents()[0]
    expect(e).toHaveProperty('id')
    expect(e).toHaveProperty('ip', '204.148.13.62')
    expect(e).toHaveProperty('utm_source', 'social')
    expect(e).toHaveProperty('ua_browser', 'Chrome')
    expect(e).toHaveProperty('ua_version', '41')
  })
})
