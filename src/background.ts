chrome.runtime.onMessage.addListener(async (request) => {
  const res = await fetch(process.env.HOST as string, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(request),
  });
});
