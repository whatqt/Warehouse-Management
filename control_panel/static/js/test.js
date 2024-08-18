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

    // Отправляем данные на сервер
    fetch('http://127.0.0.1:8000/control_panel/delete_item', {
    
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
        },
        body: jsonData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}