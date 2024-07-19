chrome.tabs.onActivated.addListener(activeInfo => {
    chrome.tabs.get(activeInfo.tabId, (tab) => {
      console.log(`Sending URL onActivated: ${tab.url}`);  // Debug logging
      fetch('http://localhost:5000/current_url', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: tab.url })
      }).then(response => response.json())
        .then(data => console.log(`Response: ${JSON.stringify(data)}`))
        .catch(error => console.error('Error:', error));
    });
  });
  
  chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete') {
      console.log(`Sending URL onUpdated: ${tab.url}`);  // Debug logging
      fetch('http://localhost:5000/current_url', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: tab.url })
      }).then(response => response.json())
        .then(data => console.log(`Response: ${JSON.stringify(data)}`))
        .catch(error => console.error('Error:', error));
    }
  });