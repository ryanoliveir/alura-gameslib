
const logoutButton = document.getElementById('logout');


logoutButton.addEventListener('click', () => {
    console.log('click');
    fetch('/logout', { method: 'GET'});
})