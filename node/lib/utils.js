const { parse, format } = require('url');

/**
 * removeTokensFromQuery
 * Given a query string object, replace any access tokens with an asterisk
 *
 * @param {Object} query
 * @return {String}
 */
const removeTokensFromQuery = function(query) {
  Object.keys(query).forEach((param) => {
    if (param.indexOf('token') > -1) {
      query[param] = '*';
    }
  });
  return query;
};
module.exports.removeTokensFromQuery = removeTokensFromQuery;


/**
 * removeTokensFromUrl
 * Given a url, replace any access tokens with an asterisk
 *
 * @param {String} url
 * @return {String}
 */
module.exports.removeTokensFromUrl = function(url) {
  const parts = parse(url, true);
  parts.query = removeTokensFromQuery(parts.query);
  delete parts.search;
  return format(parts);
};

/**
 * capFirst
 * Given a string, return the same string with the first letter capitalized
 *
 * @param {String} string
 * @return {String}
 */
const capFirst = function(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}
module.exports.capFirst = capFirst;

/**
 * getSetMethodName
 * Given a protobuf lowercase underscore field name, return the method name
 *
 * @param {String} field
 * @return {String}
 */
const getSetMethodName = function(field) {
  const fieldFormatted = field.split('_').map(capFirst).join('');
  return `set${fieldFormatted}`;
}
module.exports.getSetMethodName = getSetMethodName;
