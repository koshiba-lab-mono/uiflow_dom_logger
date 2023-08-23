import Dexie from "dexie";
import { ContentStore, ContentType } from "./contentStore";

type BlockDexie = Dexie & {
  blocks: Dexie.Table<ContentType, number>;
};

class IndexedDBStore extends ContentStore {
  private readonly db: BlockDexie;

  public constructor() {
    super();
    this.db = new Dexie("blockdb") as BlockDexie;
    this.db.version(1).stores({
      blocks: "date,content",
    });
  }

  public async add(content: ContentType): Promise<ContentType> {
    const res = await this.db.blocks.put(content).catch((err) => {
      throw err;
    });

    return content;
  }

  public async getAll() {
    return await this.db.blocks.toArray().catch((err) => {
      throw err;
    });
  }

  public async deleteAll(): Promise<void> {
    return await this.db.blocks.clear().catch((err) => {
      throw err;
    });
  }
}

export const indexedDBStore = new IndexedDBStore();
