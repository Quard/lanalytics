var LAnalytics = {
	'init': function(base_url, key){
		LAnalytics.NODE = null;
		LAnalytics.CALLBACK_FUNC = 'LAnalytics.statResult';
		LAnalytics.isSecure = location.protocol == 'https:' ? true : false;
		LAnalytics.API_REQUEST_URL = (LAnalytics.isSecure ? 
							'https://' : 'http://') + base_url + '/api/analytics.json?';

		// get window width/height
		var windowWidth = self.innerWidth ? self.innerWidth : (document.documentElement && document.documentElement.clientWidth ? document.documentElement.clientWidth : (document.body ? document.body.clientWidth : 0))
		var windowHeight = self.innerHeight ? self.innerHeight : (document.documentElement && document.documentElement.clientHeight ? document.documentElement.clientHeight : (document.body ? document.body.clientWidth : 0))
		var timezone = determine_timezone().timezone;
		
		LAnalytics.config = {
			'path': location.pathname,
			'browser': BrowserDetect.browser,
			'browser_version': BrowserDetect.version,
			'platform': BrowserDetect.OS,
			'screen_resolution': window.screen.width + 'x' + window.screen.height,
			'window_dimensions': windowWidth + 'x' + windowHeight,
			'enabled_cookie': areCookiesEnabled() ? '1' : '',
			'flash': LAnalytics.haveFlashTrigger(),
			'have_java': navigator.javaEnabled(),
			'referrer': document.referrer,
			'time_zone': timezone.utc_offset,
			'key': key,
			'callback': LAnalytics.CALLBACK_FUNC
		};
		LAnalytics.stat(LAnalytics.config);
	},
	// check flash availability
	'haveFlashTrigger': function(){
		var flashVer = swfobject.getFlashPlayerVersion();
		if(flashVer && flashVer.minor && flashVer.major && flashVer.release){
			return flashVer.major + '.' + flashVer.minor + '.' + flashVer.release;
		}
		return '';
	},
	// build request from array into GET
	'buildReq': function(config){
		var pairs = [];
		for(var key in config){
			pairs.push(encodeURI(key) + '=' + encodeURIComponent(config[key]));
		}
		return pairs.join("&");
	},
	// push stat to remote host
	'stat': function(config){
		var headID = document.getElementsByTagName("head")[0];
		var scriptNode = document.createElement('script');

		// cleanup
		if(LAnalytics.NODE){
			var oldNode = LAnalytics.NODE;
			oldNode.parentNode.removeChild(oldNode);
		}

		scriptNode.type = 'text/javascript';
		scriptNode.src = LAnalytics.API_REQUEST_URL + LAnalytics.buildReq(config);
		headID.appendChild(scriptNode);
		LAnalytics.NODE = scriptNode;
	},
	'statResult': function(result){
		// should continue stat behaviour of the visitor
	}
}