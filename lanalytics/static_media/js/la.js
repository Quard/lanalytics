(function (){
    var d = {
        have_java: navigator.javaEnabled(),
        have_flash: navigator.plugins["Shockwave Flash1"] || "",
        screen_resolution: screen.width + "x" + screen.height,
        enabled_cookie: navigator.cookieEnabled,
        refferrer: document.referrer
    };
    if (typeof navigator.cookieEnabled=="undefined" && !d["cookie"]) {
        document.cookie = "_la_test_cookie";
        d["cookie"] = document.cookie.indexOf("_la_test_cookie") != -1;
    }
    if (typeof window.innerWidth != 'undefined') {
        d['window_dimensions'] = window.innerWidth + "x" + window.innerHeight;
    } else if (typeof document.documentElement != "undefined"
         && typeof document.documentElement.clientWidth !=
         "undefined" && document.documentElement.clientWidth != 0) {
         d["window_dimensions"] = document.documentElement.clientWidth + "x" + document.documentElement.clientHeight;
    } else {
        d["window_dimensions"] = document.getElementsByTagName("body")[0].clientWidth + "x" + document.getElementsByTagName("body")[0].clientHeight;
    }
    var timezone = Date().toString().match(/GMT(.\d{2})/);
    if (timezone.length == 2) {
        d["time_zone"] = timezone[1];
    }
    console.log(d);

    var la_push = document.createElement("script");
    la_push.setAttribute("type", "text/javascript");
    var get = "";
    for (k in d) {
        get += "&" + k + "=" + d[k];
    }
    la_push.setAttribute("src", "http://localhost:8000/la_push.js?key=" + la_key + get);
    document.getElementsByTagName("head")[0].appendChild(la_push);
})();