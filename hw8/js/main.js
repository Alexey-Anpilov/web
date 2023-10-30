let socket = new WebSocket("ws://localhost:8080/websocket");


sendMessage = function(){
    msgIn = document.getElementById('messageIn');
    msg = messageIn.value;
    
    socket.send(msg);
};


socket.onopen = function(e){
    console.log("Соединение установлено")    
    document.querySelector(".btn").addEventListener("click", sendMessage)
};


socket.onmessage = function(event){
    msg = document.getElementById('messageOut');
    msg.innerText = `${event.data}`;
};


socket.onclose = function(event){
    if (event.wasClean){
        console.log(`Соединение завершено.\n Код: ${event.code}\n Причина: ${event.reason}`);
    } else{
        console.log("Соединение прервано.");
    }
};

socket.onerror = function(event){
    alert("Ошибка");
};




