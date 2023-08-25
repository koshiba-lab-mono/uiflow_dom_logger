import { ContentType } from "./stores/contentStore";
import { indexedDBStore } from "./stores/indexedDBStore";
import { wrapDivSvg } from "./utils/utils";
import "./popup.css";

const deleteButton = document.querySelector("#delete")!;
const downloadButton = document.querySelector("#download")!;
const incrementButton = document.querySelector("#increment")!;
const decrementButton = document.querySelector("#decrement")!;
const rewindArea = document.querySelector("#rewind-area")!;

deleteButton?.addEventListener("click", async () => {
  await indexedDBStore.deleteAll();
});

downloadButton.addEventListener("click", async () => {
  const data = await indexedDBStore.getAll();
  const blob = new Blob([JSON.stringify(data)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = "blocks.json";
  anchor.click();
  URL.revokeObjectURL(url);
});

let lastIndex = 0;
let maxIndex = 0;
let data: ContentType[] = [];

const onPopUP = async () => {
  data = await indexedDBStore.getAll();
  maxIndex = data.length - 1;
  if (!data.length) {
    return;
  }

  renderRewindArea();
};

const renderRewindArea = () => {
  const content = data[lastIndex];
  rewindArea.innerHTML = "";
  const title = document.createElement("h1");
  const date = new Date(content.date);
  const formattedDate = date.toLocaleDateString("ja", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });

  title.textContent = formattedDate;

  rewindArea.appendChild(title);

  const svg = document.querySelector("svg")!;
  svg.innerHTML = content.html;
  const blocklyCanvas = svg.children[0];
  Array.from(svg.children).map((el) => el.removeAttribute("transform"));

  Array.from(blocklyCanvas.children).map((blockChunkDom) => {
    blockChunkDom.removeAttribute("transform");
    const wrapDiv = wrapDivSvg(blockChunkDom);
    rewindArea.appendChild(wrapDiv);
  });
};

const incrementLastIndex = () => {
  if (lastIndex === maxIndex || !data.length) {
    return;
  }
  lastIndex += 1;
};

const decrementLastIndex = () => {
  if (lastIndex <= 0 || !data.length) {
    return;
  }
  lastIndex -= 1;
};

incrementButton.addEventListener("click", () => {
  incrementLastIndex();
  renderRewindArea();
});

decrementButton.addEventListener("click", () => {
  decrementLastIndex();
  renderRewindArea();
});

onPopUP();
