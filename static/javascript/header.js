function logout() {
    $.removeCookie('mytoken', { path: '/' });
    window.location.href = '/sign_in';
}