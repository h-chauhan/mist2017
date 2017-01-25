window.fbAsyncInit = function () {
    FB.init({
        appId: '1395586523786497',
        xfbml: true,
        version: 'v2.8'
    });
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            $("#play-btn").show();
            $("#login-btn").hide();
        } else {
            $("#play-btn").hide();
            $("#login-btn").show();
        }
    });
    FB.AppEvents.logPageView();
};
(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
        return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

function checkLoginState() {
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
            $("#play-btn").show();
            $("#login-btn").hide();
        } else {
            $("#play-btn").hide();
            $("#login-btn").show();
            alert("Facebook Login Failed!");
        }
    });
}