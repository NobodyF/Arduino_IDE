function update() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("content").innerHTML =
        this.responseText;
      }
    };
    xhttp.open("GET", "/update");
    xhttp.send();
  }
setTimeout(() => {
    setInterval(update,5000);
}, 2000);