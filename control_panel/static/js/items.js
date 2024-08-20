function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function sendData(key) {
    // Получаем данные из элемента с id, равным key
    const id_item = document.getElementById(key);
    const id_item_int = parseInt(id_item.textContent, 10); // Преобразование строки в целое число

    console.log(id_item);
    console.log(id_item_int);

    // Создаем объект данных
    const data = {
        id_item: id_item_int,
    };

    // Преобразуем объект в JSON
    const jsonData = JSON.stringify(data);

    // Получаем CSRF-токен из куки
    const csrftoken = getCookie('csrftoken');

    // Отправляем данные на сервер
    fetch('http://127.0.0.1:8000/control_panel/delete_item', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: jsonData
    })
    .then(response => response.json())

    .catch((error) => {
        console.error('Error:', error);
    });
}
