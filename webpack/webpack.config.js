const makeConfig = require('sc-recipe-staticresources');
const CopyWebpackPlugin = require('copy-webpack-plugin');


module.exports = makeConfig(
  // name
  'brasil.gov.timeline',

  // shortName
  'brasilgovtimeline',

  // path
  `${__dirname}/../src/brasil/gov/timeline/browser/static`,

  //publicPath
  '++resource++brasil.gov.timeline/',
  
);
