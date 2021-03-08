const path = require('path')
var markdown = require('markdown-it')


/**
 * `{{ }}` => `<span>{{</span> <span>}}</span>`
 * @param  {string} str
 * @return {string}
 */
var replaceDelimiters = function (str) {
  return str.replace(/({{|}})/g, '<span>$1</span>')
}

/**
 * renderHighlight
 * @param  {string} str
 * @param  {string} lang
 */
var renderHighlight = function (str, lang) {
  if (!(lang && hljs.getLanguage(lang))) {
    return ''
  }

  try {
    return replaceDelimiters(hljs.highlight(lang, str, true).value)
  } catch (err) {
  }
}


/**
 * Resolves plguins passed as string
 * @param {String|Object} plugin
 * @return {Object}
 */
var resolvePlugin = function (plugin) {
  if (typeof plugin === 'string') {
    return require(plugin)
  }
  return plugin
}

export default function MarkdownModule(moduleOptions) {

  var parser
  const _options = Object.assign({}, moduleOptions, this.options.markdown)
  var opts = Object.assign({}, _options)

  if (typeof (opts.render) === 'function') {
    parser = opts
  } else {
    opts = Object.assign({
      preset: 'default',
      html: true,
      highlight: renderHighlight
    }, opts)

    var plugins = opts.use
    var preprocess = opts.preprocess

    delete opts.use
    delete opts.preprocess

    parser = markdown(opts.preset, opts)
    if (plugins) {
      plugins.forEach(function (plugin) {
        if (Array.isArray(plugin)) {
          plugin[0] = resolvePlugin(plugin[0])
          parser.use.apply(parser, plugin)
        } else {
          parser.use(resolvePlugin(plugin))
        }
      })
    }
  }


  const markDownLoader = {
    loader: 'frontmatter-markdown-loader',
    options: {
      markdown: (body) => {
        return parser.render(body)
      }
    }
  };

  this.extendBuild(config => {

    config.module.rules.push({
      test: /\.md$/,
      use: [
        // 'raw-loader',
        markDownLoader
      ]
    })

  })

  if (_options.injected === true) {
    delete _options.injected
    // Register plugin
    this.addPlugin({
      src: path.resolve(__dirname, 'plugin.js'),
      fileName: 'markdown-it.js',
      options: _options
    })
  }
}
