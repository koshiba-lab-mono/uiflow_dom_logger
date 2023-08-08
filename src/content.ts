document.addEventListener("click", () => {
  const body = document.querySelector("body");
  if (!body) {
    return;
  }

  chrome.runtime.sendMessage({ body: body.outerHTML }, (res_from_background) =>
    console.log(res_from_background)
  );
});
