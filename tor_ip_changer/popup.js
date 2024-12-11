document.getElementById("change-ip").addEventListener("click", () => {
    chrome.runtime.sendMessage({ command: "change_ip" }, (response) => {
      console.log(response.status);
    });
  });
  