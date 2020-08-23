# Scrapy settings for maoyan_movie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyan_movie'

SPIDER_MODULES = ['maoyan_movie.spiders']
NEWSPIDER_MODULE = 'maoyan_movie.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'maoyan_movie (+http://www.yourdomain.com)'
USER_AGENG = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Upgrade-Insecure-Requests':'1',
   'Accept-Language': 'en-us',
   'Host':'maoyan.com',
   'Accept-Encoding:':'br, gzip, deflate',
   'Connection':'keep-alive',
   'Cookie':'_lxsdk_s=1741c429e89-2d2-87c-d1f%7C%7C8; __mta=214850216.1598116322505.1598203599438.1598203608022.21; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598203608; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598116322; mojo-session-id={"id":"e3adf665a475ad21fa1f4b7a0a0fab2b","time":1598201962185}; mojo-trace-id=5; mojo-uuid=e0f9493879e0aaef6dc6d48854c0d8e8; _lxsdk=A6BA1190E49A11EAABC76567ADF9CF83AD8D0E4BF7B940789D7C365A76D47737; _lxsdk_cuid=1741727dca1c8-0ddce8801ffad7-49183500-1fa400-1741727dca2c8; _csrf=9b4515bb7fac8d6121c093f30379a65d670be09849ec6adaebaccea86acb2d9d; uuid=A6BA1190E49A11EAABC76567ADF9CF83AD8D0E4BF7B940789D7C365A76D47737; uuid_n_v=v1'
   }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyan_movie.middlewares.MaoyanMovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maoyan_movie.middlewares.MaoyanMovieDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'maoyan_movie.pipelines.MaoyanMoviePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
