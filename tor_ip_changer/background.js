function sendChangeIPCommand() {
  // Connect to the native messaging host
  const port = chrome.runtime.connectNative("tor_ip_changer");

  port.postMessage({ command: "change_ip" });

  port.onMessage.addListener((response) => {
    console.log("Response from native host:", response);
    if (response.success) {
      alert("IP address changed successfully!");
    } else {
      alert("Failed to change IP address. Check Tor setup.");
    }
  });

  port.onDisconnect.addListener(() => {
    console.error("Disconnected from native host.");
  });
}

// Listen for messages from popup
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.command === "change_ip") {
    sendChangeIPCommand();
    sendResponse({ status: "IP change command sent." });
  }
});
