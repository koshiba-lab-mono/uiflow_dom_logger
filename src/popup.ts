const input = document.querySelector("#host-input") as HTMLInputElement;
const button = document.querySelector("#submit-btn");

const setStorageValue = async () => {
  const item = await chrome.storage.sync.get("hostName");
  if (item) {
    input.value = item.hostName;
  }
};


setStorageValue();
button?.addEventListener("click", () => {
  if (!input.value) {
    return;
  }

  chrome.storage.sync.set({ hostName: input.value }, () => {
    input.value;
  });
});
