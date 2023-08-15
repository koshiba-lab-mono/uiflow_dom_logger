import { IndexedDBStore } from "./stores/indexedDBStore";

const deleteButton = document.querySelector("#delete");
const downloadButton = document.querySelector("#download");

deleteButton?.addEventListener("click", async () => {
  const db = await IndexedDBStore.createInstance();
  await db.deleteAll();
  alert("done");
});

downloadButton?.addEventListener("click", async () => {
  const db = await IndexedDBStore.createInstance();
  alert(await db.getAll());
});
