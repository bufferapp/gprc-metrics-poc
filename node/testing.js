const BufferMetrics = require('./index')

const b = new BufferMetrics({ name: 'testing-app', debug: true })

const getFakeRequest = (idx) => ({
  url: `https://buffer.com/alright?i=${idx}t=${new Date().valueOf()}`,
  headers: {
    'x-forwarded-for': '204.148.13.62',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
  },
  connection: { remoteAddress: '172.0.0.1' },
  query: { utm_source: 'social' }
})

const VISITS = 1//0

for (var i = 0; i < VISITS; i++) {
  b.trackVisit(getFakeRequest(i))
}

console.log(`Tracked ${VISITS} visits`)
