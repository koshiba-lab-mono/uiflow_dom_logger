type ContentType = {
  Content: Element[];
};



chrome.runtime.onMessage.addListener(async (content: ContentType) => {
  const item = await chrome.storage.sync.get("hostName");
  if (!item) {
    return;
  }

  const res = await fetch(item.hostName, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(content),
  });
});
