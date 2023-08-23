import { indexedDBStore } from "./stores/indexedDBStore";
const deleteButton = document.querySelector("#delete");
const downloadButton = document.querySelector("#download");

deleteButton?.addEventListener("click", async () => {
  await indexedDBStore.deleteAll();
});

downloadButton?.addEventListener("click", async () => {
  const data = await indexedDBStore.getAll();
  const blob = new Blob([JSON.stringify(data)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = "blocks.json";
  anchor.click();
  URL.revokeObjectURL(url);
});

const onPopUP = async () => {
  const data = await indexedDBStore.getAll();
  if (!data.length) {
    return;
  }

  const content = data[data.length - 1];
  const svg = document.querySelector("svg")!;
  svg.innerHTML = content.html;
  const blocklyCanvas = document.querySelector(".blocklyBlockCanvas")!;
  blocklyCanvas.removeAttribute("transform")!;
  let rect: null | DOMRect = null;
  Array.from(blocklyCanvas.children).map((g) => {
    g.removeAttribute("transform");
  });
};

onPopUP();
