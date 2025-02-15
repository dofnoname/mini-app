document.getElementById('send-message').addEventListener('click', () => {
    // Отправляем сообщение в Telegram
    Telegram.WebApp.sendData('Hello from Mini App!');
});