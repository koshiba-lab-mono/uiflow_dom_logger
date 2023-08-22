import { ContentStore, ContentType } from "./stores/contentStore";
import { IndexedDBStore } from "./stores/indexedDBStore";

const main = async () => {
  const store = await IndexedDBStore.createInstance();
  chrome.runtime.onMessage.addListener(async (content: ContentType) => {
    await store.add(content);
    console.log(await store.getAll());
  });
};

main();
