btnElement = document.querySelector(".button");

btnElement.addEventListener("click", function(){
    var newDiv = document.createElement("div");
    newDiv.innerHTML = "<img src=img/meme.jpg>";
    newDiv.style.blockSize = "500px";
    newDiv.style.display = "flex";
    newDiv.style.justifyContent = "center";
    document.body.appendChild(newDiv);
})